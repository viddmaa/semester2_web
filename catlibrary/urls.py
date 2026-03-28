from django.urls import path
from . import views

app_name = "catlibrary"

urlpatterns = [
    path('', views.index, name='home'),
    path('care/', views.care, name='care'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),

]
