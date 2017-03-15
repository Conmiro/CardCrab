from django.db import models


class Seller(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class CardWear(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class CardPrint(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class PlayFormat(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class CardSet(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class CardColor(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class CardRarity(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class CardType(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


# display card details, then retrieve card if available.
class CardDetails(models.Model):
    front_art = models.URLField()
    back_art = models.URLField()
    name = models.TextField()
    set = models.ForeignKey(CardSet)
    rarity = models.ForeignKey(CardRarity)
    formats = models.ManyToManyField(PlayFormat)
    color = models.ManyToManyField(CardColor)
    type = models.ForeignKey(CardType)

    def __str__(self):
        return self.name


class Card(models.Model):
    card_details = models.ForeignKey(CardDetails)
    seller = models.ForeignKey(Seller)
    wear = models.ForeignKey(CardWear)
    print = models.ForeignKey(CardPrint)
    price = models.DecimalField(decimal_places=2, max_digits=6)



class Cart(models.Model):
    card_list = models.ManyToManyField(Card)
    # billing_info = models.ForeignKey(BillingInfo)
    # shipping_info = models.ForeignKey(ShippingInfo)


