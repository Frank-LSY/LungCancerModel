import json
import uuid
from django.db import models
import django_mysql.models

# Create your models here.


# 用户表
class User(models.Model):
    # 用户名
    username = models.CharField(max_length=40)
    # 电话
    phone = models.CharField(max_length=40)
    # 用户id
    userid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)


# 问题表
class Question(models.Model):
    # 问题名
    title = models.CharField(max_length=40)
    # 问题id
    questionid = models.CharField(max_length=40, unique=True, primary_key=True)

    # def set_choices(self, x):
    #     self.choices = json.dumps(x)

    # def get_choices(self):
    #     return json.loads(self.choices)


# 选项表
class Choice(models.Model):
    # 问题id
    questionid = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='choice', to_field='questionid')
    # 选项
    choice = models.CharField(max_length=200)


# 选项打分表
class Score(models.Model):
    # 吸烟状况
    SMOKE_LIST = ('NEVER', "LIGHT", "HEAVY")
    smoke = django_mysql.models.EnumField(choices=SMOKE_LIST)
    # 问题id
    questionid = models.ForeignKey(
        Question, on_delete=models.CASCADE, to_field='questionid')
    # 问题选项
    choice = models.IntegerField()
    # 问题分值
    score = models.IntegerField()


# 概率表
class Probability(models.Model):
    # 5年还是10年期
    year = models.CharField(max_length=20)
    # 吸烟状况
    SMOKE_LIST = ('NEVER', "LIGHT", "HEAVY")
    smoke = django_mysql.models.EnumField(choices=SMOKE_LIST)
    # 分数
    point = models.IntegerField()
    # 概率
    probability = models.CharField(max_length=80)


# 历史记录表
class History(models.Model):
    # 用户id
    userid = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field='userid')
    # 问卷id
    pollid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    # 做题时间
    time = models.DateTimeField()
    # 吸烟状况
    SMOKE_LIST = ('NEVER', "LIGHT", "HEAVY")
    smoke = django_mysql.models.EnumField(choices=SMOKE_LIST)
    # 最终结果
    probability = models.CharField(max_length=80)


# 详细记录表
class Detail(models.Model):
    # 问卷id
    pollid = models.ForeignKey(
        History, on_delete=models.CASCADE, to_field='pollid')
    # 问题id
    questionid = models.ForeignKey(
        Question, on_delete=models.CASCADE, to_field='questionid')

    # 问题选项
    choice = models.IntegerField()
