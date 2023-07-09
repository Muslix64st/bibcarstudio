from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.decorators.cache import cache_page



urlpatterns = [
    path('', Home.as_view(), name='home'), # path('', cache_page(1)(Home.as_view()), name='home'),
    path('gallery', Gallery.as_view(), name='gallery'), #     path('gallery', cache_page(1)(Gallery.as_view()), name='gallery'),
    # path('single/<int:single_pk>/', Single.as_view(), name='single'),
    path('single/<int:single_id>/', single, name='single'),
    path('contact', Contact.as_view(), name='contact'),
    path('about', About.as_view(), name='about'),
    # path('login', Login.as_view(), name='login'),
    # path('login', Login.as_view(), name='login'),
    path('User', UserForm, name='UserForm'),
]
