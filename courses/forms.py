from django.forms import ModelForm
from django import forms
from django.db import models
from .models import Courses


class CreateCoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields=('title','content')
