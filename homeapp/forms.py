from django import forms
from django_countries.fields import CountryField

class countryForm(forms.Form):
    fromCountry = CountryField(blank_label='(select country)').formfield(attts={
        'class':'custom-select d-block',
    })
    toCountry = CountryField(blank_label='(select country)').formfield(attts={
        'class':'custom-select d-block',
    })
    amount = forms.FloatField(widget = forms.NumberInput(attrs={
        'placeholder':'Amount',
        'class':'form-control'

    }))
    