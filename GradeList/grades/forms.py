from django import forms

class GradeForm(forms.Form):
    user = forms.ModelChoiceField(
        label='名前',
        max_length=50,
        queryset=Grades.objects.all(),
    )
    
    english = forms.IntegerField(
        label='英語',
        min_value=0,
        max_value=100,
    )
    math = forms.IntegerField(
        label='数学',
        min_value=0,
        max_value=100,
    )
    japanese = forms.IntegerField(
        label='国語',
        min_value=0,
        max_value=100,
    )
