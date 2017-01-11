from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):

    # if submit button was pressed
    if request.method == 'POST':
        make = request.POST.get('make')
        model = request.POST.get('model')
        year = request.POST.get('year')
        car = Car(make=make, model=model, year=year)
        car.save()
    else:
        remove = request.GET.get('remove')
        if remove:
            Car.objects.get(pk=remove).delete()

    context = {'cars': Car.objects.all()}

    return render(request, 'index.html', context)

