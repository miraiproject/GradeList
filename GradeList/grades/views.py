from django.shortcuts import render
from .forms import GradeForm
from .models import Grades

# Create your views here.
def user(request):
    """ユーザーページ"""
    grades = Grades.objects.all()
    totals = []
    for i in range(len(grades)):
        totals.append(grades[i].total)
    average = totals / len(grades)
    ranks = Grades.objects.all().order_by('-total')
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commmit=False)
            form = GradeForm()
    else:
        form = GradeForm()
    return render(request, 'grades/user.html', {'form': form, 'average': average, 'ranks': ranks})
