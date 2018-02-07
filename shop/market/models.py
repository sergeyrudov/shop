from django.db import models
from django.forms import ModelForm

# Create your models here.

class Category(models.Model):
	name = models.CharField('Article', max_length=250)

	def __str__(self):
		return '{0}'.format(self.name)

class Product(models.Model):
	name = models.CharField('Product name', max_length=250)
	description = models.CharField('Description', max_length=250)
	price = models.FloatField('Price')
	category_link = models.ForeignKey(Category)
	quantity = models.IntegerField()

	def __str__(self):
		return '{0} - {1} - {2}'.format(self.name, self.description, self.price)
