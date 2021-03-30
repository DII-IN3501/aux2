from django.urls import path
from . import views

urlpatterns = [
    path('<str:nombre>', views.index, name="index"),
    path('', views.index, name="index"),
]
