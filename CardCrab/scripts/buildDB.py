import re

from CardCrab.models import *
from mtgsdk import *



CardDetails.objects.all().delete()
CardSet.objects.all().delete()
PlayFormat.objects.all().delete()
CardRarity.objects.all().delete()
CardType.objects.all().delete()

sets = ['soi', 'emn', 'ogw', 'bfz', 'm10', 'm11', 'm12', 'm13', 'm14', 'm15', 'ori']

front = True
for set_name in sets:
    cards = Card.where(set=set_name).all()

    i = 0
    for card in cards:

        if front:

            card_details = CardDetails(name=card.name)

            if card.layout == "double-faced":
                # get back art from next card
                card_details.back_art = cards[i+1].image_url
                # let loop know next card is the backside
                front = False

            if CardDetails.objects.filter(name=card.name).exists():
                print("DUPLICATE FOUND: " + card.name)
                continue

            card_details.front_art = card.image_url
            card_details.name = card.name


            # create the set object if one does not exist for this set.
            if not CardSet.objects.filter(name=card.set_name).exists():
                cs = CardSet(name=card.set_name)
                cs.save()
            else:
                cs = CardSet.objects.get(name=card.set_name)

            card_details.set = cs

            if not CardRarity.objects.filter(name=card.rarity).exists():
                cr = CardRarity(name=card.rarity)
                cr.save()
            else:
                cr = CardRarity.objects.get(name=card.rarity)

            card_details.rarity = cr

            # get rid of extra stuff from type
            card_type = card.type
            card_type = re.sub(u"\u2014", "-", card_type)
            card_type = card_type.split(' -')[0]

            if not CardType.objects.filter(name=card_type).exists():
                ct = CardType(name=card_type)
                ct.save()
            else:
                ct = CardType.objects.get(name=card_type)

            card_details.type = ct

            # need to save before adding m2m relationships
            card_details.save()

            legalities = card.legalities
            for legal in legalities:
                if legal['legality'] == 'Legal':
                    format = legal['format']
                    if not PlayFormat.objects.filter(name=format).exists():
                        pf = PlayFormat(name=format)
                        pf.save()
                    else:
                        pf = PlayFormat.objects.get(name=format)
                    card_details.formats.add(pf)

            if card.colors == None:
                    color = "Colorless"
                    cc = CardColor.objects.get(name=color)
                    card_details.color.add(cc)
            else:
                for color in card.colors:
                    cc = CardColor.objects.get(name=color)
                    card_details.color.add(cc)

            # print(str(card.multiverse_id) + ": " + card.name)
            # print("------")
            # print("Name: " + card.name)
            # print("Mutliverse_id: " + str(card.multiverse_id))
            # print("Layout: " + card.layout)
            #
            # print("Rarity: " + card.rarity)
            # print("Image URL: " + card.image_url)
            # print("Legalities: " + str(card.legalities))
            # print("Source: " + str(card.source))
            # print("Rulings: " + str(card.rulings))
            # print("Type: " + card.type)
            # print("Supertypes: " + str(card.supertypes))
            # print("Subtypes: " + str(card.subtypes))
            #
            # print("Colors: " + str(card.colors))


        else:
            # deal with back of card above..
            front = True

        i+=1