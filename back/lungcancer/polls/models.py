import json

from django.db import models

# Create your models here.

# 用户表，用户名和电话
class User(models.Model):
    username = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)

# 问题表
class Question(models.Model):
    # 问题名
    title = models.CharField(max_length=40)
    # 问题id
    id = models.CharField(max_length=40)
    # 选项
    choices = models.CharField(max_length=200)

    def set_choices(self,x):
        self.choices = json.dumps(x)
    
    def get_choices(self):
        return json.loads(self.choices)