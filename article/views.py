from django.contrib.auth.decorators import login_required
from django.shortcuts import render, Http404, redirect, reverse
from django.contrib import messages
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.filter(is_deleted__exact=False).order_by('-id')
    q = request.GET.get('q')
    if q:
        articles = articles.filter(title__icontains=q)
    return render(request, 'article/index.html', {'objects_list': articles})


def detail(request, slug=None):
    context = {}
    if slug:
        article = Article.objects.get(slug=slug)
        context['object'] = article
        return render(request, 'article/detail.html', context)
    return Http404


def create(request):
    form = ArticleForm(request.POST or None, files=request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Article created')
        return redirect('articles:list')

    content = {
        'form': form
    }
    return render(request, 'article/create.html', content)


@login_required(login_url='/auth/login/')
def edit(request, slug):
    article = Article.objects.get(slug=slug)
    form = ArticleForm(instance=article)
    if request.method == 'POST':
        form = ArticleForm(data=request.POST, instance=article, files=request.FILES)
        form.save()
        messages.success(request, 'Article update')
        return redirect(reverse('articles:detail', kwargs={"slug": article.slug}))
    context = {
        'form': form
    }
    return render(request, 'article/edit.html', context)


@login_required(login_url='/auth/login/')
def delete(request, slug):
    article = Article.objects.get(slug=slug)
    if request.method == 'POST':
        article.is_deleted = True
        article.save()
        messages.error(request, f'Article deleted({article.id})')
        return redirect('articles:list')
    context = {
        'object': article
    }
    return render(request, 'article/delete.html', context)
