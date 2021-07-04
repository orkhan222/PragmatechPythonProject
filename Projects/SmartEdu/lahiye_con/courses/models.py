from typing import DefaultDict
from django.db import models
from django.db.models import base
from django.db.models.fields import TextField

# Create your models here.

class Courses(models.Model):
    name= models.CharField(max_length=127,unique=True,verbose_name='Kurs adi',help_text='Kurs adini yaz:')
    description= models.TextField(blank=True,null=True)
    image=models.ImageField(default='courses/default_course_image.jpg')
    date=models.DateField(auto_now=True)
    avaibable= models.BooleanField(default=True)


    def __str__(self):
        return self.name


    