# BackdoorBench1/defense/abl/views.py
from django.http import HttpResponse
from .abl_logic import run_abl_logic

def abl_home(request):
    result = run_abl_logic()
    return HttpResponse(f"ABL 模块运行结果：{result}")
