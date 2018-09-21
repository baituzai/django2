from django.contrib import admin

# Register your models here.
from .models import UserInfo
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'address', 'phone', 'datetime')
admin.site.register(UserInfo, UserInfoAdmin)