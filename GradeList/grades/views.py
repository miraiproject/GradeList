from django.shortcuts import render,redirect,get_object_or_404
from .forms import GradeForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login 

# Create your views here.
# def user(request):
#     """ユーザーページ"""
#     if request.method == 'POST':
#         form = GradeForm(request.POST)
#         if form.is_valid():
#             score = form.save(commmit=False)
#             form = forms.GradeForm()
#     else:
#         form = forms.GradeForm()
#     return render(request, 'grades/user.html', {'grade': grade, 'form': form, 'score': score,})




def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'grades/users_detail.html', {'user': user})


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
                return redirect('grades:users_detail', pk=new_user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'grades/signup.html', {'form': form})