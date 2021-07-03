from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.fields import TextField
User = get_user_model()


# Homenu Slider 
class Slider(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    yazili = models.CharField('Yazili',max_length=127,null=True)
    image = models.ImageField('Shekili', upload_to='slider_image')
    abc= models.CharField('Qiymet hissesi', max_length=127)
    text2 = models.CharField('Text2',max_length=127,null=True)


    
# Moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name='Slider'
        verbose_name_plural='Sliders'
        ordering=('-created_at',)


    def __str__(self):
        return self.title

class Home(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    image = models.ImageField('Shekili', upload_to='bestsellers_image')


    # Moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name='Home'
        verbose_name_plural='Homes'
        ordering=('-created_at',)


    def __str__(self):
        return self.title


class HomeBestSeller(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    image = models.ImageField('Shekili', upload_to='bestsellers_image')
    price= models.CharField('Qiymet hissesi', max_length=127)



    # Moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name='HomeBestSeller'
        verbose_name_plural='HomeBestSellers'
        ordering=('-created_at',)


    def __str__(self):
        return self.title

class MenViewProduct(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    image = models.ImageField('Shekili', upload_to='viewproducts_image')
    price= models.CharField('Qiymet hissesi', max_length=127)


     # Moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name='MenViewProduct'
        verbose_name_plural='MenViewProducts'
        ordering=('-created_at',)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name= models.CharField('Name', max_length=127,null=True)
    surname = models.CharField('Surname',max_length=127,null=True)
    number= models.CharField('Number', max_length=127)
    email = models.EmailField('E-mail',null=True)
    message= models.TextField('Message',null=True)



     # Moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name='Contact'
        verbose_name_plural='Contacts'
        ordering=('-created_at',)

    def __str__(self):
        return self.name



class About(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    image = models.ImageField('Shekili', upload_to='about_image')
    text= models.TextField('Text', null=True)


     # Moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name='About'
        verbose_name_plural='Abouts'
        ordering=('-created_at',)

    def __str__(self):
        return self.title