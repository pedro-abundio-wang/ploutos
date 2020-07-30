from django.urls import path
from shares import views

urlpatterns = [
    path("", views.home, name="home"),
]