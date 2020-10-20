from django import forms
from .models import Reservation


class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'Date', 'time', 'number_of_persons', 'message')

    