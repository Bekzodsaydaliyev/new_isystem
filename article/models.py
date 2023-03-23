from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save


class Article(models.Model):
    title = models.CharField(max_length=222, db_index=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='articles', null=True, blank=True, help_text='2MP dan oshmasin')
    content = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    modified_date = models.DateTimeField(auto_now=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    #
    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     if self.slug is None:
    #         self.slug = slugify(self.title)
    #     super().save()


def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = slugify(instance.title)


def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()


# pre_save.connect(article_pre_save, sender=Article)
post_save.connect(article_post_save, sender=Article)
