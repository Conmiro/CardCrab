from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):

    return render(request, 'index.html')

def search(request):

    return render(request, 'search.html')

def add_seller(request):

    return render(request, 'admin/add_seller.html')