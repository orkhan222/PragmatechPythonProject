from django.contrib import admin
from django.db.models.deletion import CASCADE
from . models import Home,Write,Skills

# Register your models here.
admin.site.register(Home)
admin.site.register(Write)
admin.site.register(Skills)