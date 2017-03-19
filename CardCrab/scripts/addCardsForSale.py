from CardCrab.models import *
from random import randint


CardPrint.objects.all().delete()
CardWear.objects.all().delete()
Seller.objects.all().delete()

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
        price = (randint(1, 500)) / 100
        quantity = randint(1,12)

        card = Card(card_details=card_details)
        card.seller = seller
        card.wear = wear
        card.printing = printing
        card.price = price
        card.quantity = quantity

        card.save()



