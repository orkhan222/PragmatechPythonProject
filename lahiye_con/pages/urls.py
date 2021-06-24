
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path('cart/', views.cart,name="cart"),
    path('order/', views.order,name="order"),
    path('product-detail/', views.productDetail,name="productDetail"),
    path('men/', views.men,name="men"),
    path('women/', views.women,name="women"),
    path('wishlist/', views.wishlist,name="wishlist"),
    path('checkout/', views.checkout,name="checkout"),
    
]
