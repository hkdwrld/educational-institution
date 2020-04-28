from django.contrib import admin
from .models import Courses
from tinymce.widgets import TinyMCE
from django.db import models

class CoursesAdmin(admin.ModelAdmin):
    fields=['title','content','date_published']
    readonly_fields=['date_published']

# Register your models here.
admin.site.register(Courses,CoursesAdmin)