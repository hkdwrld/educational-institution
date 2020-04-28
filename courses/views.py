from django.shortcuts import render

# Create your views here.
from .forms import CreateCoursesForm

from .models import *

def CreateCourse(request):
    form=CreateCoursesForm()
    context={'form':form}
    return render(request,'courses/dashboard.html',context)