import json

from django.http import HttpResponse

from polls.models import Question
from polls.models import Choice
from polls.models import Score
from polls.models import Probability

# 数据库操作


# 插入问题和选项
def insert(request):
    with open('./json/questions14.json', 'r', encoding="utf-8") as f:
        data = f.read()
        json_questions = json.loads(data)
        i = -1
        for question in json_questions['question']:
            question_handle = Question(id=i,
                                       title=question['title'], questionid=question['id'])
            question_handle.save()
            i += 1
            for choice in question['choices']:
                choice_handle = Choice(choice=choice)
                choice_handle.questionid = question_handle
                choice_handle.save()
        return HttpResponse("问题及选项插入成功！")


# 插入选项到分数
def choice2score(request):
    # return HttpResponse(Question.objects.get(questionid="BMI"))
    # return HttpResponse(Question(
    #             title='1', questionid='2'))
    with open('./json/choice2score.json', 'r', encoding='utf-8') as f:
        data = f.read()
        json_data = json.loads(data)
        for k, v in json_data.items():
            for key, value in v.items():
                # print(key)
                question_handle = Question.objects.get(questionid=key)
                for c, s in value.items():
                    score_handle = Score(smoke=k, choice=c, score=s)
                    score_handle.questionid = question_handle
                    score_handle.save()
        return HttpResponse("选项分数插入成功！")


# 插入分数到概率
def score2prob(request):
    with open('./json/score2Prob10.json', 'r', encoding="utf-8") as f:
        data = f.read()
        json_data = json.loads(data)
        for k, v in json_data.items():
            for key, value in v.items():
                prob_handle = Probability(
                    year='five', smoke=k, point=key, probability=value)
                prob_handle.save()
        return HttpResponse("分数概率插入成功！")
