from django import forms
from .models import Teams

class TeamForm(forms.ModelForm):
    
    class Meta:
        model = Teams
        fields = ['team_name']

    team_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'textInput', 'placeholder': 'Enter Team Name'}))