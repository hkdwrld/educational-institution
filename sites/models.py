from django.db import models
from account.models import Student

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=200)
    STATUS = (
        ('Pending', 'Pending'),
        ('Submitted', 'Submitted'),
    )
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS)