from django.urls import path
from .views import *

urlpatterns=[
    path('home',CustView.as_view(),name='custhome'),
    path('prodet/<int:pid>',ProductDetailView.as_view(),name='prodet'),
    path('acart/<int:id>',AddtoCart,name='acart'),
    path('cart',CartView.as_view(),name='cart'),
    path('rcart/<int:id>',removecart,name='rcart'),
    path('cout/<int:pid>',CheckoutView.as_view(),name="cout"),
    path('orders',OrderView.as_view(),name='order'),
    path('corder/<int:id>',cancelorder,name='corder')
]