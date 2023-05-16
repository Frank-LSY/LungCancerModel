# 用户视图
from rest_framework import generics, filters, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from django_filters.rest_framework import DjangoFilterBackend
from ..models import User
from ..serializer.users import UserSerializer

# Create your views here.


class CreateUser(generics.ListAPIView):
    """
    新增用户，并返回用户id
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        # print(self.request.query_params.dict())
        username = self.request.query_params.get('username', None)
        phone = self.request.query_params.get('phone', None)
        if username is not None and phone is not None:
            queryset = queryset.filter(username=username, phone=phone)
        else:
            queryset = None
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # print('qset:', queryset)
        if (queryset):
            return Response({
                'message': "用户已存在！",
                'code': status.HTTP_403_FORBIDDEN})
        elif (queryset == None):
            return Response({
                'message': "请输入姓名及电话！",
                'code': status.HTTP_400_BAD_REQUEST})
        else:
            user = request.query_params.dict()
            serializer = UserSerializer()
            usr = serializer.create(validated_data=user)
            usr = UserSerializer(usr)
            # print(usr.data['userid'])
            return Response({
                'message': "创建成功！",
                'code': status.HTTP_200_OK,
                'data':usr.data['userid']
            })


class SearchUser(generics.ListAPIView):
    """
    查询是否有某个用户，是返回用户uuid，否提示新用户
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        # print(self.request.query_params.dict())
        username = self.request.query_params.get('username', None)
        phone = self.request.query_params.get('phone', None)
        if username is not None and phone is not None:
            queryset = User.objects.filter(username=username, phone=phone)
        else:
            queryset = None
        return queryset

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        # print('qset:', queryset)
        if (queryset):
            serializer = UserSerializer(queryset, many=True)
            # print(serializer.data[0]['userid'])
            # 返回userid，用于后面查找和录入
            return Response(serializer.data[0]['userid'])
        elif (queryset == None):
            return Response({
                'message': "请输入姓名及电话！",
                'code': status.HTTP_400_BAD_REQUEST})
        else:
            return Response({
                'message': "新用户！",
                'code': status.HTTP_404_NOT_FOUND})