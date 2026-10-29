# BackdoorBench/defense/views.py
from django.http import HttpResponse

def defense_home(request):
    return HttpResponse("欢迎来到 Defense 模块主页！")
