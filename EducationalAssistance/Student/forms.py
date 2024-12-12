from EducationalAssistance.models import Student, RequirementStatusCoices, Batch
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['batch', 'name', 'school', 'grade', 'email', 'address', 'requirementsStatus']

    batch = forms.ModelChoiceField(queryset=Batch.objects.all())
    name = forms.CharField(max_length=100)
    school = forms.CharField(max_length=255)
    grade = forms.IntegerField()
    email = forms.EmailField(max_length=255)
    address = forms.CharField(max_length=255)
    requirementsStatus = forms.ChoiceField(choices=Student.requirementsStatus.choices)
    