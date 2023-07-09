from django import template

from BiBcar.forms import AddPostForm
from BiBcar.models import *

register = template.Library()


@register.simple_tag()
def get_content():
    return Content.objects.all()


@register.inclusion_tag('BiBcar/single.html')
def show_info():
    content = Content.objects.all()
    return {"content": content}


@register.inclusion_tag('BiBcar/cont_form.html')
def show_form():
    content = Content.objects.all()
    form = AddPostForm()
    return {"content": content,
            'form': form}


#
# @register.inclusion_tag('BiBcar/messages.html')
# def messages():
#     content = Content.objects.all()
#     return {"content": content}