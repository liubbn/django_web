#coding=utf-8
from django.contrib import admin

# Register your models here.
from .models import Article,Category,Tag
from .forms import ArticleForm

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','publish_time','stats','is_public','is_top','access_count','category','author')
    fields = [
              'title',
              'snippet',
              'content',
             ('is_public', 'is_top',),
             'category',
             'stats',
             'tags',
             'author'
              ]
    
    list_filter  = ['publish_time']
    search_fields = ['content']
    ###选择
    filter_horizontal = ['tags'] 
    
    form = ArticleForm
    
    class Media:
        js = (
        '/static/kindeditor/kindeditor-min.js' ,    
        '/static/kindeditor/lang/zh_CN.js' , 
        '/static/kindeditor/config.js' , 
        )


admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)