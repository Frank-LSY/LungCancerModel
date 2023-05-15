# 问题视图
from rest_framework import generics, filters, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Question
from ..serializer.questions import AllQuestionSerializer, QuestionHandleSerializer


# Create your views here.
class QuestionList(generics.ListAPIView):
    """
    获取全部问题列表
    """
    queryset = Question.objects.all().order_by('id')
    serializer_class = AllQuestionSerializer


class QuestionHandle(generics.ListAPIView):
    """
    获取全部问题id
    """
    serializer_class = QuestionHandleSerializer
    ordering_fields=('questionid','id')


    def list(self, request):
        queryset = Question.objects.all().order_by('id')
        serializer = QuestionHandleSerializer(queryset, many=True)

        qid = []
        for item in serializer.data:
            qid.append(item['questionid'])

        return Response(qid)


class SpecificQuestion(generics.ListAPIView):
    """
    获取某个问题
    """
    serializer_class = QuestionHandleSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        qid = self.request.query_params.get('qid', None)
        if qid is not None:
            queryset = queryset.get(questionid=qid)
        else:
            queryset = None
        return queryset
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        if (queryset):
            serializer = AllQuestionSerializer(queryset)
            return Response(serializer.data)
        else:
            return Response({
                'message': "请输入查询条件",
                'code': status.HTTP_400_BAD_REQUEST
            })
