from django.contrib.auth import views
from django.urls import path
from .views import register, signout


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', signout, name='logout'),
    path('register/', register, name='register')
]