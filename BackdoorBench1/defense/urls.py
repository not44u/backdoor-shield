# BackdoorBench/defense/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.defense_home, name='defense_home'),  # Defense 模块主页
    path('abl/', include('BackdoorBench1.defense.abl.urls')),  # ABL 子模块的路由
]
