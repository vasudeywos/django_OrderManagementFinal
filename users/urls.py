from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register , name='register'),
    path('accounts/profile/', views.profile , name='profile')
]
