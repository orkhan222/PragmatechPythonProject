from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.fields import TextField
User = get_user_model()

# from . models import 
# Register your models here.



class Home(models.Model):
    title= models.CharField('Title', max_length=127,null=True)  
    image = models.ImageField('Shekili', upload_to='home_image')
    text2 = models.CharField('Text2',max_length=127,null=True)


    
# Moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name='Home'
        verbose_name_plural='Homes'
        ordering=('-created_at',)


    def __str__(self):
        return self.title

class Write(models.Model):
    title= models.CharField('Title', max_length=127,null=True)  
    


    
# Moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name='Write'
        verbose_name_plural='Writes'
        ordering=('-created_at',)


    def __str__(self):
        return self.title


class Skills(models.Model):
    title= models.CharField('Title', max_length=127,null=True)  
    text01= models.CharField('Text01', max_length=127,null=True)  
    text02= models.CharField('Text02', max_length=127,null=True)   
    text03= models.CharField('Text03', max_length=127,null=True)  
    text04= models.CharField('Text04', max_length=127,null=True)  
    text05= models.CharField('Text05', max_length=127,null=True)  
    text06= models.CharField('Text06', max_length=127,null=True)  

# Moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name='Skill'
        verbose_name_plural='Skills'
        ordering=('-created_at',)


    def __str__(self):
        return self.title