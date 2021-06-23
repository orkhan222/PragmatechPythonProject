from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

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

    