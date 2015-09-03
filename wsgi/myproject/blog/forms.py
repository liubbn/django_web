#coding=utf-8
'''
Created on 2015年8月24日

@author: LIUBO
'''
from django import forms
from .models import Article
from datetime import datetime


class ArticleForm(forms.ModelForm):
    #===========================================================================
    # title = forms.CharField(label= 'title',max_length = 150)
    # snippet = forms.CharField(lable = 'snippet',widget = forms.Textarea(attrs={'cols':85,'rows':7}) ,required = False)
    #===========================================================================
    class Meta:
        model = Article
        fields = [
              'title',
              'snippet',
              'content',
             'is_public', 'is_top',
             'stats',
              ]
        widgets = {
                   'title' :forms.TextInput(attrs = {'size' : 148}),
                    'snippet' : forms.Textarea(attrs={'cols':100,'rows':6}),
                   }
        requires ={
                   'snippet' : False
                   }
        
    def save(self,commit = True):
        instance = super(ArticleForm,self).save(commit=False)
        if instance.stats == 'p' and instance.publish_time is None :
            instance.publish_time = datetime.utcnow()
        if commit :
            instance.save()
        return instance
        
