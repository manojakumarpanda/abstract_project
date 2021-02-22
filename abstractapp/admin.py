from django.contrib import admin
from .models import student,school,teacher,attendant


class Adminstudent(admin.ModelAdmin):
    list_display = ['sname','srolno','smarks','saddress','email']


class Adminteacher(admin.ModelAdmin):
    list_display = ['tname', 'tsalary', 'tcity', 'saddress']


class Adminattendant(admin.ModelAdmin):
    list_display = ['aname', 'asalary', 'tcity', 'saddress']


admin.site.register(student,Adminstudent)

admin.site.register(teacher,Adminteacher)
admin.site.register(attendant,Adminattendant)
