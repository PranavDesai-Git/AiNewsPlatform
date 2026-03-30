#!/usr/bin/env python3
from django.urls import path, include
from . import views

urlpatterns = [
    path('articles/', views.article_list, name='article-list'),
]
