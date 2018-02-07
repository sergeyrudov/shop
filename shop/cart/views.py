from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.urlresolvers import reverse
from .cart import Cart
from market.views import main_page, category_page
from market.models import Product, Category

# Create your views here.

def show_cart(request):
	cart = Cart(request.session)
	products = []
	for i in cart.cart:
		products.append(Product.objects.get(id=i[0]))
	context = {'products':products}
	return render(request, 'cart/cart.html', context)

def add_product(request):
	cart = Cart(request.session)
	quantity = request.POST.get('quantity')
	product_id = request.POST.get('product_id')
	category = request.POST.get('category_id')
	cart.add_product(product_id, quantity)
	return redirect(reverse('category', args=[category]))
