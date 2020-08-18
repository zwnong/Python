# coding = utf-8
"""
@project: Django
@author: ZWNONG
@file: views.py
@time: 2020-07-29 20:32:29
"""
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world")