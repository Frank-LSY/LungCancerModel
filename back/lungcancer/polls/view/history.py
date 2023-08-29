# 历史记录视图
from rest_framework import generics, filters, status
from rest_framework.response import Response
from ..models import History, User, Detail, Question
from ..serializer.history import HistorySerializer, DetailSerializer


class ListHistory(generics.ListAPIView):
    """
    查询用户的问卷历史
    """
    serializer_class = HistorySerializer

    def list(self, request, *args, **kwargs):
        userid = request.query_params.get('userid', None)
        queryset = History.objects.filter(userid=userid).order_by('-time')
        serializer = HistorySerializer(queryset, many=True)
        # print(serializer.data)

        if (userid == None):
            return Response({
                'message': "请给用户id！",
                'code': status.HTTP_400_BAD_REQUEST})
        else:
            if (len(serializer.data) == 0):
                return Response({
                    'message': "无问卷记录！",
                    'code': status.HTTP_404_NOT_FOUND})
            else:
                return Response({
                    "count": len(serializer.data),
                    "data": serializer.data
                })


class AddHistory(generics.CreateAPIView):
    """
    插入一条问卷历史
    """
    serializer_class = HistorySerializer

    def create(self, request, *args, **kwargs):
        smoke = request.data['smoke']
        probability = request.data['probability']
        userid = request.data['userid']
        user = User.objects.get(userid=userid)
        serializer = HistorySerializer()
        history = serializer.create(validated_data={
            'smoke': smoke,
            'probability': probability,
            'userid': user,
        })
        history = HistorySerializer(history)

        return Response({
            'message': "插入历史记录！",
            'code': status.HTTP_200_OK,
            'data': history.data
        })


class AddDetail(generics.CreateAPIView):
    """
    插入历史对应的所有答案细节
    """
    serializer_class = DetailSerializer

    def create(self, request, *args, **kwargs):
        detail = request.data['detail']
        pollid = request.data['pollid']
        poll = History.objects.get(pollid=pollid)
        serializer = DetailSerializer()
        detail_list = []
        for k, v in detail.items():
            question = Question.objects.get(questionid=k)
            item = serializer.create(validated_data={
                'pollid': poll,
                'choice': v,
                'questionid': question
            })
            detail_list.append(DetailSerializer(item).data)

        return Response({
            'message': "插入历史细节！",
            'code': status.HTTP_200_OK,
            'data': detail_list
        })
