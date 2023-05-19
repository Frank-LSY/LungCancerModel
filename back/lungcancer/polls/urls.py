from django.urls import path
from .view.users import SearchUser, CreateUser
from .view.questions import QuestionList, QuestionHandle, SpecificQuestion
from .view.results import CalcProbability
from .view.history import ListHistory, AddHistory, AddDetail

app_name = 'polls'

urlpatterns = [
    # 查询某用户是否存在
    path('user/checkUser/', view=SearchUser.as_view()),
    # 创建用户
    path('user/createUser/', view=CreateUser.as_view()),

    # 获取用户历史问卷
    path('history/listHistory/', view=ListHistory.as_view()),
    # 插入一条历史记录
    path('history/addHistory/', view=AddHistory.as_view()),
    # 插入历史记录对应的细节
    path('history/addDetail/', view=AddDetail.as_view()),

    # 获取全部问题
    path('question/getAllQuestions/', view=QuestionList.as_view()),
    # 获取所有问题id
    path('question/getQuestionHandle/', view=QuestionHandle.as_view()),
    # 获取某一个问题
    path('question/getOneQuestion/', view=SpecificQuestion.as_view()),

    # 计算分数
    path('result/calcProbability', view=CalcProbability.as_view())
]
