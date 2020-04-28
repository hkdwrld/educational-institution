from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Student, Account, Teacher, Admin
from django.dispatch import receiver


@receiver(post_save, sender=Account)
def student_profile(sender, instance, created, **kwargs):
    if created:
        print("created")
        # group = Group.objects.get(name='student')
        # instance.groups.add(group
        access = instance.access
        if access == "student":
            Student.objects.create(
                user=instance,
                name=instance.username,
                email=instance.email
            )
        elif access == "teacher":
            Teacher.objects.create(
                user=instance,
                name=instance.username,
                email=instance.email
            )
        else:
            Admin.objects.create(
                user=instance,
                name=instance.username,
                email=instance.email
            )
