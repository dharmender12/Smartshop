from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.shortcuts import redirect
# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
 def get(self,request):
    mobiles = Product.objects.filter(category='M')
    laptops = Product.objects.filter(category='L')
 
    topwears = Product.objects.filter(category='TW')
    bottomwears = Product.objects.filter(category='BW')
    kids = Product.objects.filter(category='K')
    shoes = Product.objects.filter(category='S')
    return render(request, 'app/home.html',
                  {'topwears':topwears, 'bottomwears':bottomwears, 'kids':kids,'shoes':shoes,
                   'mobiles': mobiles,'laptops':laptops})


# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class ProductDetailView(View):
 def get(self,request, pk):
   product = Product.objects.get(pk=pk)
   item_already_in_cart = False
   if request.user.is_authenticated:
     item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
   return render(request,'app/productdetail.html',
                 {'product': product, 'item_already_in_cart': item_already_in_cart})

# class ProductDetailView(View):
#  def get(self,request, pk):
#    product = Product.objects.get(pk=pk)
#    item_already_in_cart = False
#    if request.user.is_authenticated:
#      item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
#    return render(request,'app/productdetail.html',
#                  {'product': product})

@login_required
def add_to_cart(request):
  user = request.user
  product_id = request.GET.get('prod_id')
  product = Product.objects.get(id=product_id)
  Cart(user=user, product=product).save()
  return redirect('/cart')

def show_cart(request):
  if request.user.is_authenticated:
    user = request.user
    cart = Cart.objects.filter(user=user)
    
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    if cart_product:
      for p in cart_product:
          tempamount = (p.quantity * p.product.discounted_price)
          amount += tempamount
      total_amount = amount + shipping_amount
      return render(request, 'app/addtocart.html',
                    {'carts': cart, 'totalamount': total_amount, 'amount': amount})
    else:
      return render(request, 'app/emptycart.html')
    

def plus_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    print(prod_id)
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity+= 1
    c.save()
    amount = 0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount
    data = {
      'quantity': c.quantity,
      'amount': amount,
      'totalamount': amount + shipping_amount
    }
    return JsonResponse(data)

def minus_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity -= 1
    if c.quantity == 0:
      c.delete()
    else:
      c.save()
    amount = 0.0
    shipping_amount = 70.0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount
    data = {
      'quantity': c.quantity,
      'amount': amount,
      'totalamount': amount + shipping_amount
    }
    return JsonResponse(data)

def remove_cart(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.delete()
    amount = 0.0
    shipping_amount = 70.0
    cart_product = Cart.objects.filter(user=request.user)
    if not cart_product.exists():
      return JsonResponse({'empty_cart': True})
    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount
    data = {
      'amount': amount,
      'totalamount': amount + shipping_amount
    }
    return JsonResponse(data)


@method_decorator(login_required, name='dispatch')
def payment_done(request):
   user = request.user
   custid = request.GET.get('custid')
   customer = Customer.objects.get(id=custid)
   cart = Cart.objects.filter(user=user)
   for c in cart:
      OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
      c.delete()  
   return redirect("orders")

# def buy_now(request):
def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')

def address(request):
  add = Customer.objects.filter(user=request.user)
  return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

@login_required
def orders(request):
  op = OrderPlaced.objects.filter(user=request.user)
  return render(request, 'app/orders.html', {'order_placed':op})

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
 if data == None: 
   mobiles = Product.objects.filter(category='M')
 elif data == 'Redmi' or data == 'Samsung':
  mobiles = Product.objects.filter(category='M').filter(brand=data)
 elif data == 'below':
    mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
 elif data == 'above':
    mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)
 return render(request, 'app/mobile.html',{'mobiles':mobiles})

def laptop(request, data=None):
  if data == None:
    laptops = Product.objects.filter(category='L')
  elif data == 'Dell' or data == 'HP':
    laptops = Product.objects.filter(category='L').filter(brand=data)
  elif data == 'below':
    laptops = Product.objects.filter(category='L').filter(discounted_price__lt=50000)
  elif data == 'above':
    laptops = Product.objects.filter(category='L').filter(discounted_price__gt=50000)
  return render(request, 'app/laptop.html', {'laptops': laptops})

#### Top Wear
class TopWearView(View):
  def get(self, request, data=None):
    if data is None:
      topwears = Product.objects.filter(category='TW')
    elif data in ['Nike', 'Adidas']:
      topwears = Product.objects.filter(category='TW', brand=data)
    elif data == 'below':
      topwears = Product.objects.filter(category='TW', discounted_price__lt=1000)
    elif data == 'above':
      topwears = Product.objects.filter(category='TW', discounted_price__gt=1000)
    return render(request, 'app/topwear.html', {'topwears': topwears})


### Bottom Wear
def bottomwear(request, data=None):
  if data == None:
    bottomwears = Product.objects.filter(category='BW')
  elif data == "Levis" or data == 'Wrangler':
    bottomwears = Product.objects.filter(category='BW').filter(brand=data)
  elif data == 'below':
    bottomwears = Product.objects.filter(category='BW').filter(discounted_price__lt=1500)
  elif data == 'above':
    bottomwears = Product.objects.filter(category='BW').filter(discounted_price__gt=1500)
  return render(request, 'app/bottomwear.html', {'bottomwears': bottomwears})

def shoes(request, data=None):
  if data == None:
    shoes = Product.objects.filter(category='S')
  elif data == 'Nike' or data == 'Adidas':
    shoes = Product.objects.filter(category='S').filter(brand=data)
  elif data == 'below':
    shoes = Product.objects.filter(category='S').filter(discounted_price__lt=2000)
  elif data == 'above':
    shoes = Product.objects.filter(category='S').filter(discounted_price__gt=2000)
  return render(request, 'app/shoes.html', {'shoes': shoes})
      
# def laptop(request):
#  return render(request, 'app/laptop.html')

# def topwear(request):
#  return render(request, 'app/topwear.html')

# def bottomwear(request):
#  return render(request, 'app/bottomwear.html')

# def shoes(request):
#  return render(request, 'app/shoes.html')

# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
  def get(self,request):
    form = CustomerRegistrationForm()
    return render(request, 'app/customerregistration.html', {'form':form})
  def post(self,request):
    form = CustomerRegistrationForm(request.POST)
    if form.is_valid():
      messages.success(request, 'Congratulations!! Registered Successfully')
      form.save()
    return render(request, 'app/customerregistration.html', {'form':form}) 
  
# Checkout Page
# @login_required
def checkout(request):
  user = request.user
  add = Customer.objects.filter(user=request.user)
  cart_items = Cart.objects.filter(user=user)
  amount = 0.0
  shipping_amount = 70.0
  total_amount = 0.0
  cart_product = [p for p in Cart.objects.all() if p.user == request.user]
  if cart_product:
    for p in cart_product:
      tempamount = (p.quantity * p.product.discounted_price)
      amount += tempamount
    total_amount = amount + shipping_amount
  return render(request, 'app/checkout.html',{'add':add,
  'totalamount':total_amount,'cart_items':cart_items})

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
  def get(self,request):
    form = CustomerProfileForm()
    return render(request, 'app/profile.html', {'form':form,
    'active':'btn-primary'})
  def post(self,request):
    form = CustomerProfileForm(request.POST)
    if form.is_valid():
      usr = request.user
      name = form.cleaned_data['name']
      locality = form.cleaned_data['locality']
      city = form.cleaned_data['city']
      state = form.cleaned_data['state']
      zipcode = form.cleaned_data['zipcode']
      reg = Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
      reg.save()
      messages.success(request, 'Congratulations!! Profile Updated Successfully')
    return render(request, 'app/profile.html', {'form':form,'active':'btn-primary'})

def logout_view(request):
  logout(request)
  return redirect('login')