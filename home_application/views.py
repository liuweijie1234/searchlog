# -*- coding: utf-8 -*-
from django.shortcuts import render
from blueking.component.shortcuts import get_client_by_request

# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def home(request):
    client = get_client_by_request(request)
    res = client.cc.search_business()


    return render(request, 'home_application/index_home.html')


def config(request):
    """
    配置
    """
    return render(request, 'home_application/config.html')



