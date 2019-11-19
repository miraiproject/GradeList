from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'grades'
urlpatterns = [
    path('edit_profile/',views.edit_profile, name="edit_profile"),
    path('profile_done/', views.profile_done, name='profile_done'),
    path('profile/', views.profile, name='profile'),
    path('profile_detail/', views.profile_detail, name='profile_detail'),        
    path('user/', views.user, name='user'),
    path('reply/<int:objection_id>/', views.reply, name='reply'),
    path('submitted/', views.submitted, name='submitted'),
    path('', auth_views.LoginView.as_view(template_name='grades/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout_done/', views.done, name='logout_done'),
    path('signup/', views.signup, name='signup'),
]
