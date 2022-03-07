import datetime
from django import forms
from .models import Inproduct


class addproduct(forms.Form):
    name = forms.CharField(max_length=512)
    inload_number = forms.CharField(max_length=512)
    count = forms.CharField(max_length=200)
    unit = forms.ChoiceField(choices=Inproduct.ROLES)
    in_date = forms.DateTimeField(initial=datetime.datetime.now())