from django import forms

from EducationalAssistance.models import Batch, StatusChoices


class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['batch_name', 'start_date', 'end_date', 'status', 'budget', 'limit', 'current_count']

    batch_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'textInput', 'placeholder': 'Enter Batch Name'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'dateInput', 'placeholder': 'Enter Start Date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'dateInput', 'placeholder': 'Enter End Date'}))
    status = forms.ChoiceField(
        required=False, 
        choices=StatusChoices.choices, initial=StatusChoices.Open,
        widget=forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Enter Status'}))
    budget = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'textInput', 'id': "number-input", 'placeholder': 'Enter Budget'}))
    limit = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'textInput', 'id': "number-input", 'placeholder': 'Enter Limit'}))
    current_count = forms.IntegerField(
        disabled=True,
        required=False, 
        widget=forms.NumberInput(attrs={'class': 'textInput', 'id': "number-input", 'placeholder': 'Enter Current Count'})
    )