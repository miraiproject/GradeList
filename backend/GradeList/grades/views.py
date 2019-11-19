from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from .forms import GradeForm, ObjectionForm, ReplyForm, ProfileForm
from .models import Grades, Objections, Replies, Profile
from .serializers import UserSerializer, GradesSerializer, ObjectionsSerializer, RepliesSerializer, ProfileSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from statistics import mean


# Create your views here.
@api_view(['GET','POST'])
@login_required
def user(request):
    """ユーザーページ"""
    """成績表示"""
    try:
        grade = Grades.objects.get(user=request.user)
    except Grades.DoesNotExist:
        grade = Grades(user=request.user)
        grade.save()

    """成績入力フォーム"""
#    import pdb; pdb.set_trace()
    if request.method == 'POST':
        g_form = GradeForm(request.POST)
        if g_form.is_valid():
            new_grade = g_form.save(commit=False)
            delete_grade = Grades.objects.get(user=new_grade.user)
            delete_grade.delete()
            new_grade.save()
            g_form = GradeForm()
    else:
        g_form = GradeForm()

    grades = Grades.objects.all()
    totals = []
    for i in range(len(grades)):
        grades[i].total = grades[i].english + grades[i].math + grades[i].japanese
        grades[i].gpa = 0.0
        grades[i].save()
        totals.append(grades[i].total)
    average = sum(totals) /  len(grades)
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

    """異議申立入力フォーム"""
    objections = Objections.objects.all()
    
    if request.method == 'POST':
        o_form = ObjectionForm(request.POST)
        if o_form.is_valid():
            objection = o_form.save(commit=False)
            objection.author = request.user
            objection.save()
            o_form = ObjectionForm() 
        return redirect('grades:submitted')
    else:
        o_form = ObjectionForm()

    user_objections = Objections.objects.filter(author=request.user)
    
    """異議申立回答表示"""
    replies = Replies.objects.all()

    user = User.objects.get(username=request.user.username)
    user = UserSerializer(user)
    grades = GradesSerializer(grades, many=True)
    objection = ObjectionsSerializer(user_objections, many=True)

    return Response(user.data)
#    return render(request, 'grades/user.html', {'g_form': g_form, 'o_form': o_form, 'average': average, 'ranks': ranks, 'grade': grade, 'objections': objections, 'user_objections': user_objections, 'replies': replies})

@login_required
def submitted(request):
    return render(request, 'grades/submitted.html')

@api_view(['GET','POST'])
@login_required
def reply(request, objection_id):
    """異議申立返信フォーム"""
    if request.method == 'GET':
        objection = Objections.objects.get(id=objection_id)
        replies = Replies.objects.filter(target=objection)
        serializer = ObjectionsSerializer(objection, many=True)
        replies = RepliesSerializer(replies, many=True)
        return Response(replies.data)

    elif request.method == 'POST':
        serializer = RepliesSerializer(request.POST, many=True)
        if serializer.is_valid():
            serializer.author = request.user
            serializer.target = Objections.objects.get(id=Objection_id)
            serializer.save()
            return Response(serializer.data)
        return redirect('grades:submitted')
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return render(request, 'grades/reply.html', {'form': form, 'objection': objection})

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
                return redirect('grades:user')
    else:
        form = UserCreationForm()
    return render(request, 'grades/signup.html', {'form': form})


@login_required
def profile(request):
    profile_1 =  Profile.objects.filter(user__username__exact=request.user).first()
    if profile_1 == None:
        if request.method == "POST":
            form = ProfileForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
            return redirect('grades:profile_detail')
        else:
            form = ProfileForm
        return render(request, 'grades/profile.html',{
            'form':form,
            })
    else:
        return redirect('grades:profile_done')

@login_required
def profile_detail(request):
    user = request.user
    # profiles = user.profile_set.all().first()
    profiles = Profile.objects.filter(user__username__exact=request.user)
    username = user.username
    return render(request, 'grades/profile_detail.html', {'user':user,'profiles':profiles})

@login_required
def edit_profile(request):
    user = request.user
    profiles = Profile.objects.filter(user__username__exact=request.user).first()
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profiles)
        if form.is_valid():
            form.save()
            return redirect('grades:profile_detail')
    else:
        form = ProfileForm(instance=profiles)
    return render(request, 'grades/edit_profile.html', {'form': form, 'user':user })

def profile_done(request):
    return render(request, 'grades/profile_done.html')