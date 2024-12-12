from EducationalAssistance.models import Student, RequirementStatusCoices, Batch
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'school', 'grade', 'email', 'address', 'requirementsStatus']

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'textInput', 'placeholder': 'Enter Name'}))
    school = forms.CharField(widget=forms.TextInput(attrs={'class': 'textInput', 'placeholder': 'Enter School'}))
    grade = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'textInput', 'placeholder': 'Enter Grade'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'textInput w-[300px]', 'placeholder': 'Enter Email'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'textInput', 'placeholder': 'Enter Address'}))
    requirementsStatus = forms.ChoiceField(
        choices=RequirementStatusCoices.choices, initial=RequirementStatusCoices.Completed,
        widget=forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}))
    