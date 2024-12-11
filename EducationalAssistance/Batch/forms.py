from django import forms

from EducationalAssistance.models import Batch


class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['batch_name', 'start_date', 'end_date', 'status', 'budget', 'limit', 'current_count']

    batch_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'textInput', 'placeholder': 'Enter Batch Name'}), 
        max_length=255)
    start_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'dateInput', 'id': "datepicker-range-start", "name": 'start', 'placeholder': 'Enter Start Date'}))
    end_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'dateInput', 'id': "datepicker-range-end", "name": 'end', 'placeholder': 'Enter End Date'}))
    status = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'textInput', 'placeholder': 'Enter Status'}))
    budget = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'textInput', 'id': "number-input", 'placeholder': 'Enter Budget'}))
    limit = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'textInput', 'id': "number-input", 'placeholder': 'Enter Limit'}))
    current_count = forms.IntegerField(
        required=False, 
        widget=forms.NumberInput(attrs={'class': 'textInput', 'id': "number-input", 'placeholder': 'Enter Current Count'})
    )