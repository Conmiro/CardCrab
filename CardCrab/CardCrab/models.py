from django.db import models


class Seller(models.Model):
    name = models.TextField()

class CardDetails(models.Model):
    front_art = models.FileField(default=None)
    back_art = models.FileField(default=None)
    name = models.TextField()
    set = models.TextField()
    rarity = models.TextField()
    format = models.TextField()
    color = models.TextField()
    type = models.TextField()


class Card(models.Model):
    card_details = models.ForeignKey(CardDetails)
    seller = models.ForeignKey(Seller)
    condition = models.TextField()
    print = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)


class Cart(models.Model):
    card_list = models.ManyToManyField(Card)
    # billing_info = models.ForeignKey(BillingInfo)
    # shipping_info = models.ForeignKey(ShippingInfo)


