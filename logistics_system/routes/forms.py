from django import forms
from .models import Route

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['start_place', 'end_place', 'start_lat', 'start_lng', 'end_lat', 'end_lng', 'distance', 'duration']
        widgets = {
            'start_place': forms.TextInput(attrs={'class': 'form-control', 'id': 'start_place'}),
            'end_place': forms.TextInput(attrs={'class': 'form-control', 'id': 'end_place'}),
            'start_lat': forms.HiddenInput(attrs={'id': 'start_lat'}),
            'start_lng': forms.HiddenInput(attrs={'id': 'start_lng'}),
            'end_lat': forms.HiddenInput(attrs={'id': 'end_lat'}),
            'end_lng': forms.HiddenInput(attrs={'id': 'end_lng'}),
            'distance': forms.HiddenInput(attrs={'id': 'distance'}),
            'duration': forms.HiddenInput(attrs={'id': 'duration'})
        }
        