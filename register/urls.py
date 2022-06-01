from django.urls import path
from register.views import Register
from . import views

app_name = 'register'

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
]
