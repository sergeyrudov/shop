from django.conf.urls import url, include
from market.views import main_page, category_page

urlpatterns = [
	url(r'^([0-9]+)', category_page, name='category' ),
	
	]