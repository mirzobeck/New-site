from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)


    def __str__(self) -> str:
        return self.name


class post(models.Model):
    ch = [
        ('draft', 'Draft'),
        ('published', 'Published')
    ]
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cate = models.ForeignKey(category, on_delete=models.PROTECT, null=True)
    body = RichTextUploadingField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=ch, default='draft')
    objects = models.Manager()
    published = PublishedManager()


    class Meta:
        ordering = ('-publish',)
        verbose_name = 'yangilik'
        verbose_name_plural = 'yangiliklar'

    def __str__(self):
        return self.title


