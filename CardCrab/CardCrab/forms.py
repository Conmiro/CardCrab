from django import forms
from .models import *


class ShippingInformationForm(forms.ModelForm):
    class Meta:
        model = ShippingInformation
        fields = '__all__'

class AddSellerForm(forms.Form):
    name = forms.CharField(label="Seller Name")


class AddCardDetailsForm(forms.Form):

    front_art = forms.URLField(label='Front art URL')
    back_art = forms.URLField(label='Back art URL', required=False)
    name = forms.CharField()
    set = forms.ModelChoiceField(queryset=CardSet.objects.all())
    formats = forms.ModelMultipleChoiceField(queryset=PlayFormat.objects.all())
    color = forms.ModelMultipleChoiceField(queryset=CardColor.objects.all())
    rarity = forms.ModelChoiceField(queryset=CardRarity.objects.all())
    type = forms.ModelChoiceField(queryset=CardType.objects.all())


class AddCardForm(forms.Form):
    card_details = forms.ModelChoiceField(queryset=CardDetails.objects.all(), label='Card')
    seller = forms.ModelChoiceField(queryset=Seller.objects.all())
    wear = forms.ModelChoiceField(queryset=CardWear.objects.all())
    printing = forms.ModelChoiceField(queryset=CardPrint.objects.all())
    price = forms.DecimalField(decimal_places=2, max_digits=6)

