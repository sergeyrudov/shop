from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.


def main_page(request):
	categories = Category.objects.all()
	if categories:
		object = categories[0]
		context = {'category':object, 'categories': categories}
		return render(request, 'market/index.html', context)
	else:
		context = {}
		return render(request, 'market/index.html', context)
		
		
def category_page(request, id):
	categories = Category.objects.all()
	category = Category.objects.get(id=id)
	context = {'category':category, 'categories': categories}
	return render(request, 'market/categorypage.html', context)