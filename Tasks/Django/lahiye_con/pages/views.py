from django.shortcuts import render
from .models import Contact, Home, HomeBestSeller, MenViewProduct, Slider
# Create your views here.

def index(request):
    slider= Slider.objects.all()
    best= HomeBestSeller.objects.all()
    home = Home.objects.all()
    context={
        'slider':slider,
        'best':best,
        'home':home
    }
  
   
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    ctc= Contact.objects.all()
    context={
        'ctc':ctc,
    }
    return render(request, 'contact.html',context)
    

def cart(request):
    return render(request, 'cart.html')
    
def order(request):
    return render(request, 'order.html')

def productDetail(request):
    return render(request, 'product-detail.html')


def men(request):
    viewproducts= MenViewProduct.objects.all()
    context={
        'viweproducts':viewproducts
    }
  
    return render(request, 'men.html',context)

def women(request):
    return render(request, 'women.html')  


def wishlist(request):
    return render(request, 'wishlist.html')  

def checkout(request):
    return render(request, 'checkout.html')  