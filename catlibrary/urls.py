from django.urls import path
from catlibrary.views import index

app_name = "catlibrary"

urlpatterns = [
    path('', index, name="index"),
]
