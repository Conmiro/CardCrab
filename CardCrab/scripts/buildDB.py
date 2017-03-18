from CardCrab.models import *
from mtgsdk import *



# shadows over inistrad

set = CardSet.objects.filter(name='Shadows over Innistrad').first()

print(set.name)

cards = Card.where(set='soi').all()
