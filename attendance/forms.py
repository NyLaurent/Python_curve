from django import forms
from .models import Student, Attendence 


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','classroom']

        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter student name'
            }),
            'classroom': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Enter classroom name'
            }),
        }