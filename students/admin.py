from django.contrib import admin

from students.models import Student

# Register your models here.


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',  'group_id')
