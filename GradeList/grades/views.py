from django.shortcuts import render
from .forms import GradeForm
from .models import Grades

from statistics import mean

# Create your views here.
def user(request):
    """ユーザーページ"""
    try:
        grade = Grades.objects.get(user=request.user)
    except Grades.DoesNotExist:
        grade = Grades(user=request.user)
        grade.save()

#    import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            new_grade = form.save(commit=False)
            delete_grade = Grades.objects.get(user=new_grade.user)
            delete_grade.delete()
            new_grade.save()
            form = GradeForm()
    else:
        form = GradeForm()

    grades = Grades.objects.all()
    totals = []
    for i in range(len(grades)):
        grades[i].total = grades[i].english + grades[i].math + grades[i].japanese
        grades[i].save()
        totals.append(grades[i].total)
    average = [total / len(grades) for total in totals]
    ranks = Grades.objects.all().order_by('-total')
    for i in range(len(ranks)):
        ranks[i].id = i + 1

    grade = Grades.objects.get(user=request.user)
    score = [grade.english, grade.math, grade.japanese]
    gp = []
    for i in range(3):
        if score[i] >= 96:
            gp.append(4.3)
        elif score[i] >= 85:
            gp.append(4.0)
        elif score[i] >= 75:
            gp.append(3.0)
        elif score[i] >= 65:
            gp.append(2.0)
        elif score[i] >= 60:
            gp.append(1.0)
        else:
            gp.append(0.0)
    grade.gpa = round(mean(gp), 2)
    grade.save()


    return render(request, 'grades/user.html', {'form': form, 'average': average, 'ranks': ranks, 'grade': grade})

