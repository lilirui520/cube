 #! -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
import hashlib

class Content(models.Model):
    """docstring for Content"""
    start_date = models.DateField()
    end_date = models.DateField()
    author = models.ForeignKey(User)
    cur_done = models.TextField()
    next_goal = models.TextField()
    comment	= models.TextField()
