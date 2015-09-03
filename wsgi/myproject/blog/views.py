#coding=utf-8

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.conf import settings
import logging
from django.views.generic.list import ListView
from .models import Article

#日志记录器
logger = logging.getLogger('blog.views')

#全局上下文
def global_setting(request):
    ##文章归档
    article_archive = Article.art_objects.archive()
    #
    setting = {
               'site_title' : settings.SITE_TITLE,
               'site_name'  : settings.SITE_NAME,
               'site_content' : settings.SITE_CONTENT,
               'site_des' : settings.SITE_DES,
               'site_logo' : settings.SITE_LOGO,
               'archive' : article_archive,
               }
    return setting

####通用查询Article
def _query_article(request,pagenation = False,**kw):
    pass




# Create your views here.
def index(request):
#    return HttpResponse('<h1> hello world ! </h1>')    
    return render(request,'base.html')

###通用视图展现Article /index
class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'
    paginate_by = settings.PAGE_SIZE
    
    ### 判断文章是否为发布,公开 .order_by('-publish_time')
    def get_queryset(self):
        return Article.objects.filter(stats='p',is_public='1')








def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')












#===============================================================================
# from chartit import DataPool, Chart
# import simplejson
# def weather_chart_view(request):
#     #Step 1: Create a DataPool with the data we want to retrieve.
#     weatherdata = \
#         DataPool(
#            series=
#             [{'options': {
#                'source': MonthlyWeatherByCity.objects.all()},
#               'terms': [
#                 'month',
#                 'houston_temp',
#                 'boston_temp']}
#              ])
# 
#     #Step 2: Create the Chart object
#     cht = Chart(
#             datasource = weatherdata,
#             series_options =
#               [{'options':{
#                   'type': 'line',
#                   'stacking': False},
#                 'terms':{
#                   'month': [
#                     'boston_temp',
#                     'houston_temp']
#                   }}],
#             chart_options =
#               {'title': {
#                    'text': 'Weather Data of Boston and Houston'},
#                'xAxis': {
#                     'title': {
#                        'text': 'Month number'}}})
# 
#     #Step 3: Send the chart object to the template.
#     return render_to_response('chart.html',{'weatherchart': cht})
#===============================================================================