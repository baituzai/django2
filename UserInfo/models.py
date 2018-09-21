from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    index = models.IntegerField(default = 0)
    name = models.CharField(max_length = 4)
    address = models.TextField()
    phone   =models.CharField(max_length = 20)
    datetime = models.DateTimeField(auto_now_add= True)
    class Meta:
        ordering = ['-datetime']
