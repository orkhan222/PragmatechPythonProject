from django.shortcuts import render,redirect
from .models import About, Cart, Contact, Home, HomeBestSeller, MenViewProduct, Slider, TrustedPartner
# Create your views here.
from django.forms import forms
from .forms import  ContactForm
from django.contrib import messages

def index(request):
    slider= Slider.objects.all()
    best= HomeBestSeller.objects.all()
    home = Home.objects.all()
    
    form=ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            form = Contact(full_name=full_name,email=email, subject=subject, message=message)
            form.save()
            messages.success(request, 'Mesaj gonderildi...')

            return redirect ('index')

    context={
        'slider':slider,
        'best':best,
        'home':home,
        'form':form,
    }

   
    return render(request, 'index.html',context)

def about(request):
    about=About.objects.all()
    context={
        'about':about,
    }
    return render(request, 'about.html',context)

def contact(request):
    ctc= Contact.objects.all()
    context={
        'ctc':ctc,
    }
    return render(request, 'contact.html',context)
    

def cart(request):
    cart=Cart.objects.all()
    context={
        'cart':cart,
    }

    return render(request, 'cart.html',context)
    
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
    trust =TrustedPartner.objects.all()
    context={
        'trustedpartner':trust
    }
  
    return render(request, 'women.html',context)  


def wishlist(request):
    return render(request, 'wishlist.html')  

def checkout(request):
    return render(request, 'checkout.html')  