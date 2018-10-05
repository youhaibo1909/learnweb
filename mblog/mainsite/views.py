# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
import sys

# if sys.getdefaultencoding() != 'utf-8':
#     reload(sys)
#     sys.setdefaultencoding('utf-8')

def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        print (count, post, type(post.body))
        post_lists.append("No.{}:".format(str(count).decode('utf-8')) + str(post).decode('utf-8')+"<hr>")
        post_lists.append("<small>" + str(post.body.encode('utf-8')).decode('utf-8') + "</small><br><br>")
    return HttpResponse(post_lists)