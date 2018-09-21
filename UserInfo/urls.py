from django.conf.urls import url

from . import views

# 小写报错 原因是 UserInfo 下的 urls 写错了 应该小写 不然后面连接地址会不对
urlpatterns = [
    # url(r'^userinfo/$', views.userInfo, name='userinfo')
    url(r'^userinfo/$', views.userinfo, name='userinfo'),
    url(r'^userinfo/add/$', views.userinfoPost, name='userinfoPost')

]