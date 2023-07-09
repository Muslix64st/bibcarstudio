
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound, Http404, request
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import *
from .models import *



menu = [{'title': 'На главную', 'url_name': 'home'},
        {'title': 'Наши работы', 'url_name': 'gallery'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'О нас', 'url_name': 'about'}, #  {'title': 'Войти/регистрация', 'url_name': 'login'}
        ]

jobs = [{'jobs': 'Полировка', 'url_name': 'home'},
        {'jobs': 'Химчистка', 'url_name': 'gallery'},
        {'jobs': 'Керамика', 'url_name': 'contact'},
        {'jobs': 'Плёнка', 'url_name': 'about'}
        ]


form = AddPostForm()
post = Content.objects.all()
cats = CategoryContent.objects.all()

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['jobs'] = jobs
        context['cats'] = cats
        context['form'] = form
        context['post'] = post
        return context



