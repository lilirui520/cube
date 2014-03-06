 #! -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import connection, models
import hashlib
import django_tables2 as tables

# TODO: custome query manager
# class ContentManager(models.Manager):
#     def self_reports(self, author_id):


class Content(models.Model):
    """docstring for Content"""
    start_date = models.DateField(verbose_name='起始日期')
    end_date = models.DateField(verbose_name='结束日期')
    author = models.ForeignKey(User, verbose_name='作者')
    cur_done = models.TextField(verbose_name='上周工作')
    next_goal = models.TextField(verbose_name='下周任务')
    comment	= models.TextField(verbose_name='评论')


class ContentTableForSelf(tables.Table):
    """"""
    class Meta:
        model = Content
        fields = ("start_date", "end_date", "cur_done", "next_goal", "comment")

class ContentTableForOther(tables.Table):
    class Meta:
        model = Content
        fields = ("start_date", "end_date", "author","cur_done", "next_goal")