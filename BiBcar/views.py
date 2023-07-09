from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound, Http404, request
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView, CreateView, DetailView

from BiBcar.forms import *
from BiBcar.models import *

from .utils import *


class Home(DataMixin, ListView):
    model = Content
    template_name = 'BiBcar/index.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='BiBcar')
        return dict(list(context.items()) + list(c_def.items()))


# class Single(DataMixin, DetailView):
#     model = Content
#     template_name = 'BiBcar/single.html'
#     # context_object_name = 'post'
#     pk_url_kwarg = 'single_pk'
#     # content = get_object_or_404(Content, pk=single_pk)
#
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='BiBcar')
#         return dict(list(context.items()) + list(c_def.items()))


def single(request, single_id):
    content = get_object_or_404(Content, pk=single_id)
    # slow = Content.objects.all()
    post = Content.objects.all()

    context = {
        'post': post,
        'content': content,
        'menu': menu,
        'title': content.title,
        'cat_selected': content.cat_id, }

    return render(request, 'BiBcar/single.html', context=context)  # }


class Gallery(DataMixin, ListView):
    model = Content
    template_name = 'BiBcar/gallery.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='BiBcar')
        return dict(list(context.items()) + list(c_def.items()))


class Contact(DataMixin, ListView):
    model = UserForm
    template_name = 'BiBcar/contact.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='BiBcar')
        return dict(list(context.items()) + list(c_def.items()))


class About(DataMixin, ListView):
    model = UserForm
    template_name = 'BiBcar/about.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='BiBcar')
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>404 Not Found</h1>')


def UserForm(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact request submitted successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)


    else:
        form = AddPostForm()
        return HttpResponse(f"Отображение странички регистрации пользователец")
