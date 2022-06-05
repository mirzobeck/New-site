from django.contrib import admin
from .models import post, category
# Register your models here.

@admin.register(post)
class postadmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'cate', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(category)
class cats(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


