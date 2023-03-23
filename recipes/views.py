from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Recipes, Tag
from .forms import RecipeCreateForm, RecipeUpdateForm, TagForm


def recipe_list(request):
    recipes = Recipes.objects.filter(is_activate=True).order_by('-id')
    ctx = {
        "objects_list": recipes
    }
    return render(request, 'recipe/list.html', ctx)


def _recipe_list(request):
    recipes = Recipes.objects.all()
    return render(request, 'recipe/list.html', {"object": recipes})


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipes, slug=slug)
    ctx = {
        'object': recipe
    }
    return render(request, 'recipe/detail.html', ctx)


@login_required
def recipe_create(request, *args, **kwargs):
    form = RecipeCreateForm()
    if request.method == "POST":
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.is_activate = True
            obj.save()
            form.save_m2m()
            return redirect(reverse('recipes:detail', kwargs={'slug': obj.slug}))
    ctx = {
        'form': form
    }
    return render(request, 'recipe/create.html', ctx)


@login_required
def recipe_update(request, slug):
    obj = get_object_or_404(Recipes, slug=slug)
    form = RecipeUpdateForm(instance=obj)
    if request.method == "POST":
        form = RecipeUpdateForm(data=request.POST, instance=obj)
        return redirect(reverse('recipes:detail', kwargs={'slug': slug}))
    ctx = {
        'form': form
    }
    return render(request, 'recipe/update.html', ctx)


@login_required
def recipe_delete(request, slug):
    obj = get_object_or_404(Recipes, slug=slug)
    if request.method == "POST":
        obj.delete()
        messages.error(request, f"{obj.title} o'chirdingiz!")
        return redirect('recipes:list')
    ctx = {
        'object': obj
    }
    return render(request, 'recipe/delete.html', ctx)


def tag_list(request):
    tag = Tag.objects.order_by('-id')
    ctx = {
        'objects_list': tag
    }
    return render(request, 'recipe/tag/list.html', ctx)


@login_required
def tag_create(request, *args, **kwargs):
    form = TagForm()
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect(reverse('recipes:tag_detail', kwargs={'pk': obj.id}))
    ctx = {
        'form': form
    }
    return render(request, 'recipe/tag/create.html', ctx)


def tag_detail(request, pk):
    tag = get_object_or_404(Tag, id=pk)
    ctx = {
        'object': tag
    }
    return render(request, 'recipe/tag/detail.html', ctx)


@login_required
def tag_update(request, pk):
    obj = get_object_or_404(Tag, id=pk)
    form = TagForm(instance=obj)
    if request.method == "POST":
        form = TagForm(data=request.POST, instance=obj)
        return redirect(reverse('recipes:tag_detail', kwargs={'pk': id}))
    ctx = {
        'form': form
    }
    return render(request, 'recipe/tag/update.html', ctx)


@login_required
def tag_delete(request, pk):
    obj = get_object_or_404(Recipes, id=pk)
    if request.method == "POST":
        obj.delete()
        messages.error(request, f"{obj.title} o'chirdingiz!")
        return redirect('recipes:tag_list')
    ctx = {
        'object': obj
    }
    return render(request, 'recipe/tag/delete.html', ctx)
