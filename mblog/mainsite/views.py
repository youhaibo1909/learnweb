# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import get_template
from datetime import datetime

from .models import Post

# Create your views here.
import sys

# if sys.getdefaultencoding() != 'utf-8':
#     reload(sys)
#     sys.setdefaultencoding('utf-8')

# def homepage(request):
#     posts = Post.objects.all()
#     post_lists = list()
#     for count, post in enumerate(posts):
#         print (count, post, type(post.body))
#         post_lists.append("No.{}:".format(str(count).decode('utf-8')) + str(post).decode('utf-8')+"<hr>")
#         post_lists.append("<small>" + str(post.body.encode('utf-8')).decode('utf-8') + "</small><br><br>")
#     return HttpResponse(post_lists)

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')