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
    type = models.ForeignKey(CardType)
    formats = models.ManyToManyField(PlayFormat)
    color = models.ManyToManyField(CardColor)


    def __str__(self):
        return self.name


class Card(models.Model):
    card_details = models.ForeignKey(CardDetails)
    seller = models.ForeignKey(Seller)
    wear = models.ForeignKey(CardWear)
    printing = models.ForeignKey(CardPrint)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    quantity = models.IntegerField(default=1)


class Cart(models.Model):
    card_list = models.ManyToManyField(Card, through='CardInCart')
    # billing_info = models.ForeignKey(BillingInfo)
    # shipping_info = models.ForeignKey(ShippingInfo)


class CardInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    quantity = models.IntegerField()


