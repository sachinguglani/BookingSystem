from django.urls import path
from . import views
from rms.views import create_post

urlpatterns = [
    path('rms/', views.roomData, name='rms'),
    path('rmsform/', create_post, name='create_post'),
    path('Registration/', views.RegistrationPage, name='RegistrationPage'),
]