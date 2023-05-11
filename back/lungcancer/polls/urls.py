from django.urls import path
from .view.users import SearchUser, CreateUser
from .view.questions import QuestionList, QuestionHandle, SpecificQuestion

app_name = 'polls'

urlpatterns = [
    # 查询某用户是否存在
    path('checkUser/', view=SearchUser.as_view()),
    # 创建用户
    path('createUser/', view=CreateUser.as_view()),
    # 获取全部问题
    path('getAllQuestions/', view=QuestionList.as_view()),
    # 获取所有问题id
    path('getQuestionHandle/', view=QuestionHandle.as_view()),
    # 获取某一个问题
    path('getOneQuestion/', view=SpecificQuestion.as_view()),
    # path('choice/', view = views.ChoiceList.as_view())
    # # 获取问题全部
    # path('getAllQuestions/', view=views.get_all_question, name='getAllQuestions'),
    # # 获取某一个问题及选项
    # # 获取问题的id
    # path('getQuestionId/', view=views.get_question_id, name='getQuestionId')
]
