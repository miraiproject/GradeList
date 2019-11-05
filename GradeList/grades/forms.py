from django import forms

class GradeForm(forms.Form):
    user = forms.CharField(max_length=50)
    subject = forms.CharField(max_length=50)
    score = forms.IntegerField(min_value=0, max_value=100)
