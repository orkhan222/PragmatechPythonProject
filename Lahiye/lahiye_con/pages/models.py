from django.db import models

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


    def __str__(self):
        return self.title

# Moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HomeBestSellers(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    image = models.ImageField('Shekili', upload_to='bestsellers_image')
    price= models.CharField('Qiymet hissesi', max_length=127)

    def __str__(self):
        return self.title

class MenViewProducts(models.Model):
    title= models.CharField('Title', max_length=127,null=True)
    image = models.ImageField('Shekili', upload_to='viewproducts_image')
    price= models.CharField('Qiymet hissesi', max_length=127)

    def __str__(self):
        return self.title

    