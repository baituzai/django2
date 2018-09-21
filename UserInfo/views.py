from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
# 在 Info/views.py 中新导入两个文件
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache

from .models import UserInfo
import json 

#def UserInfo(requets): 这里小写 userinfo
def userinfo(request):
    # userinfor_list = UserInfo.object.all()
    userinfo_list = UserInfo.objects.all()
    items = []
    for i in range(len(userinfo_list)):
        data = userinfo_list[i]
        data.index = len(userinfo_list)-i
        data.datetime = data.datetime.strftime('%Y-%m-%dT %h:%M:%S')
        item = {
            'pk': data.index,
            'name':data.name,
            'address': data.address,
            'phone': data.phone,
            'datetime': data.datetime
        }
        items.append(item)
    return JsonResponse({'items':items}, safe=False)


# 注意缩进


@csrf_exempt
@never_cache
def userinfoPost(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        userinfo = UserInfo(
            name = name,
            address = address,
            phone = phone
        )
        userinfo.save()
        return JsonResponse({'result':'ok'}, safe=False)
    elif request.method == 'GET':
        return JsonResponse({'result':'failed'}, safe=False)