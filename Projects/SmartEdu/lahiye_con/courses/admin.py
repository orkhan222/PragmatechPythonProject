from django.contrib import admin
from .models import Courses
# Register your models here.

admin.register(Courses)

class CourseAdmin(admin.ModelAdmin):
    list_display=('name','avilable')
    list_filter= ('avilable',)
    search_fields=('name','description')
