from CardCrab.models import *
from random import randint


CardPrint.objects.all().delete()
CardWear.objects.all().delete()
Seller.objects.all().delete()
Card.objects.all().delete()

sellers = ['Betancards', 'Miro Games', 'Armstrong Games', 'Cenci Cards']
wears = ['Mint', 'Lightly Played', 'Moderately Played', 'Heavily Played', 'Damaged']
printings = ['Foil', 'Normal']

for seller in sellers:
    s = Seller(name=seller)
    s.save()

for wear in wears:
    cw = CardWear(name=wear)
    cw.save()

for printing in printings:
    cp = CardPrint(name=printing)
    cp.save()

for card_details in CardDetails.objects.all():
    for i in range(randint(1,6)):
        # get a random seller
        seller = Seller.objects.all().order_by('?').first()
        wear = CardWear.objects.all().order_by('?').first()
        printing = CardPrint.objects.all().order_by('?').first()
        price = (randint(1, 5)) / 100
        quantity = randint(1, 30)

        if wear.name == 'Mint':
            quantity*=0.25
            price *= 10
        elif wear.name == "Lightly Played":
            quantity*=0.5
            price *= 5
        elif wear.name == "Moderately Played":
            quantity *= 3
        elif wear.name == "Heavily Played":
            price *= 0.5
        elif wear.name == "Damaged":
            price *= 0.1

        if card_details.rarity.name == 'Mythic Rare':
            quantity*=0.10
            price *= 100
        elif card_details.rarity.name == 'Rare':
            quantity*=0.25
            price *= 25
        elif card_details.rarity.name == 'Uncommon':
            quantity*=0.8
            price *= 10
        elif card_details.rarity.name == 'Basic Land':
            quantity*=25
            price *= 0.10

        if printing.name == 'Foil':
            quantity*=0.25
            price*=5

        if price < 0.01:
            price = 0.01

        if quantity < 1:
            quantity = 1



        card = Card(card_details=card_details)
        card.seller = seller
        card.wear = wear
        card.printing = printing
        card.price = price
        card.quantity = quantity

        card.save()



