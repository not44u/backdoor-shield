# BackdoorBench1/defense/abl/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.abl_home, name='abl_home'),  # ABL 模块主页
]
