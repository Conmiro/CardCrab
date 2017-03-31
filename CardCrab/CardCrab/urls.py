"""DjangoTut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^search_body/', views.search_body, name='search_body'),
    url(r'^add_seller/', views.add_seller, name='add_seller'),
    url(r'^card_details/', views.card_details, name='card_details'),
    url(r'^add_card_details/', views.add_card_details, name='add_card_details'),
    url(r'^add_card/', views.add_card, name='add_card'),
    url(r'^cart_body/', views.cart_body, name='cart_body'),
    url(r'^checkout/', views.checkout, name='checkout'),
    url(r'^shipping_billing_body/', views.shipping_billing_body, name='shipping_billing_body'),
    url(r'^shopping_cart/', views.shopping_cart, name='shopping_cart'),
    url(r'^submit_order/', views.submit_order, name='submit_order'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/$', auth_views.login, name='login', kwargs={'template_name': 'login.html','redirect_authenticated_user': True}),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^my_store/', views.my_store, name='my_store'),
    url(r'^my_store_body/', views.my_store_body, name='my_store_body')

]

