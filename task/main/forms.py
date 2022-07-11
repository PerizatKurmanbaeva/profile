import datetime

from .models import People
from django.forms import ModelForm, TextInput, DateInput


class PeopleForm(ModelForm):
    class Meta:
        model= People
        fields= ["name", "surname", "date_of_birth"]
        widgets = {
            "name": TextInput(attrs={
                "class": 'form-control',
                "placeholder": 'Name'
            }),
            "surname": TextInput (attrs={
                "class": 'form-control',
                "placeholder": 'Surname'
            }),
            "date_of_birth": DateInput(format='%d/%m/%Y', attrs= {
                "class": 'form-control date-picker-input',
                "placeholder": 'mm/dd/yyyy',
                "max": datetime.date.today()
            }, )
        }