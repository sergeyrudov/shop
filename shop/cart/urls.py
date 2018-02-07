from django.conf.urls import url, include
from cart.views import *


urlpatterns = [
	url(r'^add/', add_product, name='addtocart' ),
	url(r'^$', show_cart, name='cart'),
	
]