from django.contrib import admin
from .models import Teacher, Student, Account, Admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
# Register your models here.

admin.site.site_header = 'Admin Page'

def make_active(MyAdmin, request, queryset):
    queryset.update(is_active=True)
make_active.short_description = "Activate Users"

class MyAdmin(UserAdmin):
    actions = [make_active]
    list_filter = ('is_active', 'email_verified')
    list_display=('username','email','is_active','email_verified','is_staff')
    #list_editable=('is_active',)
    fieldsets = [("Personal Info", {"fields": ['username', 'email', 'first_name', 'last_name']}),
    (("Permissions", {"fields": ['is_active', 'is_staff', 'is_superuser', 'email_verified']})),
    (("Dates", {"fields": ['date_joined', 'last_login']}))]


admin.site.register(Account, MyAdmin)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Admin)

admin.site.unregister(Group)
