from django.db import models
from tinymce import models  as tinymce_models
from datetime import datetime

# Create your models here.
class Courses(models.Model):
    title=models.CharField(max_length=200)
    date_published=models.DateTimeField(auto_now_add=True)
    #content=tinymce_models.HTMLField()
    content=models.TextField()

    def __str__(self):
        return self.title
    
