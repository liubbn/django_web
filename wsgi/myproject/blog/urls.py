#coding=utf-8
'''
Created on 2015年8月17日

@author: LIUBO
'''
from blog import views
from django.conf.urls import patterns , url,include

urlpatterns = patterns('blog.views',
    #url('^$','index',name = 'index'), 
    url('^$',views.ArticleListView.as_view(),name='index'),
    url('^index/$',views.ArticleListView.as_view(),name = 'index'), 
    url('^about/$','about',name = 'about'),                    
    url('^contact/$','contact',name = 'contact'),                    
                       
                       
                       
                       
                       ) 