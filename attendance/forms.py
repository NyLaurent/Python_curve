from django import forms
from .models import Student, Attendence 


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'classroom', 'gender', 'residence']

        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter student name'
            }),
            'classroom': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Enter classroom name'
            }),
            'gender': forms.RadioSelect(attrs={
                'class': 'form-check-input'
            }),
            'residence': forms.Select(attrs={
                'class': 'form-control'
            }),
        }