from django.http import HttpResponse
from django.shortcuts import render
from .forms import AddSellerForm, AddCardDetailsForm, AddCardForm

from .models import *


def index(request):

    return render(request, 'index.html')


def search(request):

    cards = CardDetails.objects.all()
    filters = {}
    filters['wear'] = CardWear.objects.all()
    filters['print'] = CardPrint.objects.all()
    filters['color'] = CardColor.objects.all()
    filters['rarity'] = CardRarity.objects.all()
    filters['set'] = CardSet.objects.all()

    for card in cards:
        individuals = Card.objects.filter(card_details=card)
        if individuals:
            cheapest = individuals.order_by('price').first()
            card.cheapest_card = cheapest

    context = {'cards': cards, 'filters': filters}
    return render(request, 'search.html', context)


def add_seller(request):

    if request.method == 'POST':
        form = AddSellerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            seller = Seller(name=data["name"])
            seller.save()

    form = AddSellerForm()
    sellers = Seller.objects.all()
    context = {'form': form, 'sellers': sellers}

    return render(request, 'admin/add_seller.html', context)



def add_card_details(request):
    if request.method == 'POST':
        mode = request.POST.get('submit')
        form = AddCardDetailsForm(request.POST)
        if mode == 'Preview':
            # want to keep the form populated, send it back to template
            context = {'form': form}
            return render(request, 'admin/add_card_details.html', context)
        elif mode == 'Submit':
            if form.is_valid():
                data = form.cleaned_data
                card_details = CardDetails(front_art=data['front_art'],
                                           back_art=data['back_art'],
                                           name=data['name'],
                                           set=data['set'],
                                           rarity=data['rarity'],
                                           type=data['type'])
                card_details.save()
                # '*' converts to list
                card_details.formats.add(*data['formats'].all())
                card_details.color.add(*data['color'].all())


    form = AddCardDetailsForm()
    context = {'form': form}
    return render(request, 'admin/add_card_details.html', context)


def add_card(request):

    if request.method == 'POST':
        form = AddCardForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            card = Card(card_details=data['card_details'],
                        seller=data['seller'],
                        wear=data['wear'],
                        printing=data['printing'],
                        price=data['price'])
            card.save()

    form = AddCardForm()

    context = {'form': form}
    return render(request, 'admin/add_card.html', context)