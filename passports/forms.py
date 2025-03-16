from django import forms
from .models import BorderCrossingApplication

class BorderCrossingForm(forms.ModelForm):
    class Meta:
        model = BorderCrossingApplication
        fields = ['crossing_date', 'flight_number', 'crossing_point', 'destination_country', 'purpose']
