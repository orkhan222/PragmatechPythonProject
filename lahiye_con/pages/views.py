from django.shortcuts import render
from .models import HomeBestSellers, Slider
# Create your views here.

def index(request):
    slider= Slider.objects.all()
    best= HomeBestSellers.objects.all()
    context={
        'slider':slider,
        'best':best
    }
  
   
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
    

def cart(request):
    return render(request, 'cart.html')
    
def order(request):
    return render(request, 'order.html')

def productDetail(request):
    return render(request, 'product-detail.html')


def men(request):
    return render(request, 'men.html')

def women(request):
    return render(request, 'women.html')  


def wishlist(request):
    return render(request, 'wishlist.html')  

def checkout(request):
    return render(request, 'checkout.html')  

