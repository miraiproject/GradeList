from django.shortcuts import render
from .forms import GradeForm

# Create your views here.
def user(request):
    """ユーザーページ"""
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            score = form.save(commmit=False)
            form = forms.GradeForm()
    else:
        form = forms.GradeForm()
    return render(request, 'grades/user.html', {'grade': grade, 'form': form, 'score': score})
