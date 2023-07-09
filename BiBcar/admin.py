from django.contrib import admin

# Register your models here.
from .models import *


# admin.site.register(Hero)


class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo_b', 'photo_l', 'photo_s', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


class CategoryContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class UserFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'car_number')
    list_display_links = ('name', 'phone_number')
    search_fields = ('car_number',)


admin.site.register(Content, ContentAdmin)
admin.site.register(CategoryContent, CategoryContentAdmin)
admin.site.register(UserForm, UserFormAdmin)
# admin.site.register(Jobs, JobsAdmin)
# admin.site.register(CategoryJobs, CategoryJobsAdmin)
