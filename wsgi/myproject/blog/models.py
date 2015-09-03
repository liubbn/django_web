#coding=utf-8
from django.db import models,connection
from django.contrib.auth.models import User

# Create your models here.

###管理器
class ArticleManager(models.Manager):
    def archive(self):
        cursor = connection.cursor()
        ##sqlite 数据库语法
        cursor.execute("""
                    SELECT
                    DISTINCT strftime('%Y',blog_article.publish_time) year,
                    strftime('%m',blog_article.publish_time) month
                    FROM
                    blog_article
                    WHERE
                    blog_article.stats = 'p'
                    and blog_article.is_public='1' 
                    """
                    )
        result_list = []
        for row in cursor.fetchall():
            tm = row[0]+u'年'+row[1]+u'月'
            result_list.append(tm)
        return result_list


#文章
class Article(models.Model):
    #标题
    title = models.CharField(max_length=150,verbose_name=u'文章标题')
    #摘要
    snippet = models.CharField(max_length=500,verbose_name = u'摘要',default=u'请点击查看更详细内容。。。')
    #内容
    content = models.TextField(u'内容',)
    #创建时间
    add_time = models.DateTimeField(auto_now_add = True,verbose_name = u'创建时间')
    #发表时间
    publish_time = models.DateTimeField(null = True,verbose_name = u'发表时间')
    #修改时间
    update_time = models.DateTimeField(auto_now = True,verbose_name = u'修改时间')
    #文章状态（发表，草稿）
    STATUS_CHOICES = (('d',u'草稿'),('p',u'发表'))
    stats = models.CharField(max_length=1 ,choices =STATUS_CHOICES,default= STATUS_CHOICES[0][0],verbose_name = u'文章状态')
    #公开
    is_public = models.BooleanField(u'公开',default = True)
    #置顶
    is_top = models.BooleanField(u'置顶',default= False)
    #浏览量
    access_count = models.IntegerField(u'浏览量',default = 1 ,editable = False)
    #分类
    category = models.ForeignKey('Category',verbose_name = u'分类',null =True ,blank=True)
    #标签
    tags = models.ManyToManyField('Tag',verbose_name = u'标签' , blank=True)
    #作者
    author = models.ForeignKey(User,verbose_name = u'作者' ,null =True ,blank = True)
    
    ##添加新管理器
    objects = models.Manager()
    art_objects = ArticleManager()
    
    def save(self,*args,**kw):
        self.snippet = self.snippet or self.content[:200]
        super(Article,self).save(*args,**kw)
    
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'所有文章'
        ordering = ['-publish_time',]


######分类信息
class Category(models.Model):
    title = models.CharField(max_length = 150 ,unique = True,verbose_name = u'分类名称')
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u'分类信息'
        verbose_name_plural = u'分类信息'

####文章标签

class Tag(models.Model):
    title = models.CharField(max_length = 150 ,unique = True,verbose_name = u'标签名称')
    
    def __unicode__(self):
        return self.title
    
    class Meta :
        verbose_name = u'标签'
        verbose_name_plural = u'标签'
    
        
    







####chart

#===============================================================================
# class MonthlyWeatherByCity(models.Model):
#     month = models.IntegerField()
#     boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
#     houston_temp = models.DecimalField(max_digits=5, decimal_places=1)
#===============================================================================