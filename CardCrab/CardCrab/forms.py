from django import forms
from .models import *


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    username = forms.CharField(label='Username', max_length=30)
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm Password', max_length=100, widget=forms.PasswordInput())




class BillingInformationForm(forms.ModelForm):
    class Meta:
        model = BillingInformation
        fields = '__all__'

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


class AddCardForm(forms.ModelForm):
    class Meta:
        model = Card
        exclude = ['store']
        labels = {
            'card_details': 'Card'
        }

    def __init__(self, *args, **kwargs):
        super(AddCardForm, self).__init__(*args, **kwargs)
        self.fields['card_details'].queryset = CardDetails.objects.order_by('name')

# class AddCardForm(forms.Form):
#     card_details = forms.ModelChoiceField(queryset=CardDetails.objects.all(), label='Card')
#     wear = forms.ModelChoiceField(queryset=CardWear.objects.all())
#     printing = forms.ModelChoiceField(queryset=CardPrint.objects.all())
#     quantity = forms.IntegerField()
#     price = forms.DecimalField(decimal_places=2, max_digits=6)

