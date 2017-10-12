# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField


class ToDoWork(models.Model):
    title=models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    date_end=models.DateTimeField(auto_now_add=False, null=True, blank=True)
    date_start= models.DateTimeField(auto_now_add=False, null=True, blank=True)
    done=models.BooleanField(default='False')
    content=models.TextField()
    def __unicode__(self):
        return  "{}-{}".format(self.title,self.date_start)



class DoingWork(models.Model):
    content= RichTextUploadingField(config_name='default')
