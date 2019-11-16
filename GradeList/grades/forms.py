from django import forms
from .models import Grades, Objections

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grades
        fields = ('user', 'english', 'math', 'japanese',)

class ObjectionForm(forms.ModelForm):
    class Meta:
        model = Objections
        fields = ('text',)
