from django.urls import path
from . import views

app_name = 'grades'
urlpatterns = [
    path('user/', views.user, name='user'),
]
