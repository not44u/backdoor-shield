from django.contrib import admin
from django.urls import path, include
from . import views  # 导入你的视图

urlpatterns = [
    path('admin/', admin.site.urls),
    path('defense/', include('BackdoorBench.defense.urls')),
    path('', views.index, name='index'),  # 添加这一行来处理根路径请求
    path('charts1/', views.charts1_view, name='charts1'),
]
