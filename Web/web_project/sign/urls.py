# coding = utf-8
"""
@All-project: Web
@author: ZWNONG
@file: urls.py
@time: 2020-08-31 12:10:15
"""
from django.urls import path
import sign.views
urlpatterns = [
    path('hello_world/', sign.views.hello_world)
]
