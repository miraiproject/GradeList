from django import forms
from .models import Grades, Objections, Profile

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grades
        fields = ('user', 'english', 'math', 'japanese',)

class ObjectionForm(forms.ModelForm):
    class Meta:
        model = Objections
        fields = ('text',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['name','student_number','major','grade']
        labels={'name':'名前', 'student_number':'学籍番号', 'major':'学部・専攻', 'grade':'学年'}
