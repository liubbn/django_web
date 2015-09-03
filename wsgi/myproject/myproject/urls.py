from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.upload import upload_img
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'',include('blog.urls',namespace = 'blog')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$',upload_img,name = 'upload_img'),
    url(r'^uploads/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
)
