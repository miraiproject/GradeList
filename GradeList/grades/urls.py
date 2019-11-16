from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'grades'
urlpatterns = [
    path('user/', views.user, name='user'),
    path('submitted/', views.submitted, name='submitted'),
    path('', auth_views.LoginView.as_view(template_name='grades/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout_done/', views.done, name='logout_done'),
    path('signup/', views.signup, name='signup'),
]
