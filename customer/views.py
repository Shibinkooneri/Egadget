from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DetailView
from account.models  import Product,Cart,Order
from django.contrib import messages
from account.views import Signin_required,decs
from django.utils.decorators import method_decorator

# Create your views here.
# class CustView(View):
#     def get(self,request):
#         return render(request,"cust_home.html")
@method_decorator([Signin_required],name='dispatch')
class CustView(ListView):
    template_name="cust_home.html"
    queryset=Product.objects.all()
    context_object_name="pro"

@method_decorator(decs,name='dispatch')
class ProductDetailView(DetailView):
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("pid")
    #     pro=Product.objects.get(id=id)
    #     return render(request,"prodetails.html",{"data":pro})
    template_name="prodetails.html"
    queryset=Product.objects.all()
    pk_url_kwarg="pid"
    context_object_name="data"

decs
def AddtoCart(request,*args,**kwargs):
    pid=kwargs.get("id")
    pro=Product.objects.get(id=pid)
    user=request.user
    qty=request.POST.get('qty')
    Cart.objects.create(product=pro,user=user,quantity=qty)
    messages.success(request,"Product added to cart")
    return redirect('custhome')

@method_decorator([Signin_required],name='dispatch')
class CartView(ListView):
    template_name="cart.html"
    queryset=Cart.objects.all()
    context_object_name="cart"

    def get_queryset(self):
        
        return Cart.objects.filter(user=self.request.user, status='cart')

@Signin_required
def removecart(request,*args,**kwargs):
    id=kwargs.get("id")
    cart=Cart.objects.get(id=id)
    cart.delete()
    messages.success(request,"Product removed successfully")
    return redirect('cart')

@method_decorator([Signin_required],name='dispatch')
class CheckoutView(TemplateView):
    template_name="checkout.html"
    def post(self,request,*args,**kwargs):
        address=request.POST.get("address")
        ph=request.POST.get("phone")
        user=request.user
        cid=kwargs.get("pid")
        cart=Cart.objects.get(id=cid)
        prod=cart.product
        qty=cart.quantity
        Order.objects.create(user=user,address=address,phone=ph,product=prod,quantity=qty)
        cart.status='Order Placed'
        cart.save()
        messages.success(request,"Order Placed")
        return redirect('cart')
    
@method_decorator([Signin_required],name='dispatch') 
class OrderView(ListView):
    template_name="orders.html"
    queryset=Order.objects.all()
    context_object_name='order'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

@Signin_required
def cancelorder(request,**kwargs):
    oid=kwargs.get('id')
    order=Order.objects.get(id=oid)
    order.status='Cancelled'
    order.save()
    messages.success(request,"Order Cancelled")
    return redirect('order')


