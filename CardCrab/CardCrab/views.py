from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from .forms import AddSellerForm, AddCardDetailsForm, AddCardForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *


def index(request):

    return render(request, 'index.html')


def shopping_cart(request):
    try:
        cart = Cart.objects.get(pk=1)
    except ObjectDoesNotExist:
        cart = Cart()
        cart.save()

    if request.method == 'POST':
        action = request.POST.get('action')
        card_id = request.POST.get('card_id')
        card = Card.objects.get(pk=card_id)

        if action == 'remove':
            card_in_cart = CardInCart.objects.get(cart=cart, card=card)
            card_in_cart.delete()
            return HttpResponse("Removed!")

        add_quantity = int(request.POST.get('quantity'))
        available_quantity = card.quantity
        try:
            card_in_cart = CardInCart.objects.get(cart=cart, card=card)
            curr_quantity = card_in_cart.quantity

            new_quantity = add_quantity + curr_quantity
            print(new_quantity)
            if new_quantity > available_quantity:
                return HttpResponse("Not Enough")
            else:
                card_in_cart.quantity = new_quantity
                card_in_cart.save()

        except ObjectDoesNotExist:
            if add_quantity > available_quantity:
                return HttpResponse("Not Enough")
            else:
                CardInCart.objects.create(cart=cart, card=card, quantity=add_quantity)

        return HttpResponse("Added!")

    total = 0
    for cardincart in cart.cardincart_set.all():
        total += cardincart.card.price * cardincart.quantity

    cardlist = cart.card_list.all()

    for card in cardlist:
        cardincart = CardInCart.objects.get(cart=cart,card=card)
        card.price = cardincart.quantity * card.price

    print(cardlist)

    context = {'cardlist': cardlist, 'total': total}

    return render(request, 'shopping_cart.html', context)

def card_details(request):

    if request.method == 'POST':
        card_id = request.POST.get('card_id')
        chosen_id = request.POST.get('chosen_id')
        chosen = Card.objects.get(pk=chosen_id)
        details = CardDetails.objects.get(pk=card_id)

        other_cards = Card.objects.filter(card_details=details).exclude(pk=chosen_id)

        context = {'details': details, 'chosen': chosen, 'other_cards': other_cards}
        return render(request, 'card_details.html', context)

    return render(request, 'card_details.html')

def search_body(request):

    cards = CardDetails.objects.all()

    if request.method == 'POST':

        page = request.POST.get('page')
        search_text = request.POST.get('search_text')
        wears = request.POST.getlist('wear')
        printings = request.POST.getlist('printing')
        card_types = request.POST.getlist('type')
        card_colors = request.POST.getlist('color')
        card_rarities = request.POST.getlist('rarity')
        card_sets = request.POST.getlist('set')

        if search_text:
            cards = cards.filter(name__icontains=search_text)
        if card_types:
            cards = cards.filter(type__in=card_types)
        if card_colors:
            cards = cards.filter(color__in=card_colors)
        if card_rarities:
            cards = cards.filter(rarity__in=card_rarities)
        if card_sets:
            cards = cards.filter(set__in=card_sets)

    else:
        page = 2


    paginator = Paginator(cards, 4)

    try:
        cards = paginator.page(page)
    except PageNotAnInteger:
        cards = paginator.page(1)
    except EmptyPage:
        cards = paginator.page(paginator.num_pages)


    for card in cards:
        individuals = Card.objects.filter(card_details=card)
        if wears:
            individuals = individuals.filter(wear__in=wears)
        if printings:
            individuals = individuals.filter(printing__in=printings)
        if individuals:
            cheapest = individuals.order_by('price').first()
            card.cheapest_card = cheapest



    context = {'cards': cards }

    return render(request, 'search_body.html', context)


def search(request):

    filters = {'wear': CardWear.objects.all(), 'print': CardPrint.objects.all(), 'color': CardColor.objects.all(),
               'rarity': CardRarity.objects.all(), 'set': CardSet.objects.all(), 'type': CardType.objects.all()}

    search_text = None
    if request.method == 'POST':
        search_text = request.POST.get('search_text')

    print(search_text)
    context = {'filters': filters, 'search_text': search_text}
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