from django.db import models
from django.contrib.auth.models import User




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




class ShippingState(models.Model):
    name = models.TextField()


state_choices = (('TX', 'TX'), ('TN', 'TN'))


class ShippingInformation(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    address_line1 = models.CharField(max_length=128)
    address_line2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128,choices=state_choices)
    zip = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)


class CardProvider(models.Model):
    name = models.CharField(max_length=128)
    art = models.URLField()

    def __str__(self):
        return self.name


month_choices = (('JAN', '01 January'), ('FEB', '02 February'))
year_choices = ((2017, 2017), (2018, 2018), (2019, 2019))


class BillingInformation(models.Model):
    cardholder_name = models.CharField(max_length=128)
    card_provider = models.ForeignKey(CardProvider, default=1)
    card_number = models.CharField(max_length=128)
    exp_month = models.CharField(max_length=128, choices=month_choices, default='JAN')
    exp_year = models.IntegerField(choices=year_choices, default=2017)
    sec_code = models.IntegerField(default=123)






