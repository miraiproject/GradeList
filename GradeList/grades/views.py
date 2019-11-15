from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login 

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


@login_required
def users_detail(request):
    userid = str(request.user.id)
    username = request.user.username
    return render(request, 'grades/user.html', {'username':username, 'userid':userid,})


def done(request):
    return render(request, 'grades/logout.html')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # ユーザーインスタンスを作成
        if form.is_valid():
            new_user = form.save() # ユーザーインスタンスを保存
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']
            # フォームの入力値で認証できればユーザーオブジェクト、できなければNoneを返す
            new_user = authenticate(username=input_username, password=input_password)
            # 認証成功時のみ、ユーザーをログインさせる
            if new_user is not None:
                # loginメソッドは、認証ができてなくてもログインさせることができる。→上のauthenticateで認証を実行する
                login(request, new_user)
                return redirect('grades:users_detail')
    else:
        form = UserCreationForm()
    return render(request, 'grades/signup.html', {'form': form})
