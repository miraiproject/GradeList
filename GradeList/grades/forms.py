from django import forms
from .models import Grades

class GradeForm(forms.ModelForm):
#    math = forms.IntegerField(
#        label='数学',
#        min_value=0,
#        max_value=100,
#    )
#    japanese = forms.IntegerField(
#        label='国語',
#        min_value=0,
#        max_value=100,
#    )
    class Meta:
        model = Grades
        fields = ('user', 'english', 'math', 'japanese',)
