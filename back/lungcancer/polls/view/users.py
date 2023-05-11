# 用户视图
from rest_framework import generics, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from ..models import User
from ..serializer.users import UserSerializer

# Create your views here.


class CreateUser(generics.ListAPIView):
    """
    插入用户
    """
    def list(self, request, *args, **kwargs):
        print(self.request.query_params.dict())
        # user = User(username='LSY',phone='12345678909')
        user = {
            'username':'LSY',
            'phone': '12345678909'
        }
        serializer_class = UserSerializer()
        serializer_class.create(validated_data = user)

        return Response({
                'message': "success",
                'code': status.HTTP_200_OK,
                'data': []
            })


class SearchUser(generics.ListAPIView):
    """
    查询是否有某个用户，是返回True，否返回False
    """

    def get_queryset(self):
        queryset = User.objects.all()
        print(self.request.query_params.dict())
        username = self.request.query_params.get('username', None)
        phone = self.request.query_params.get('phone', None)
        if username is not None and phone is not None:
            queryset = queryset.get(username=username, phone=phone)
        else:
            queryset = None
        return queryset

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        if (queryset):
            serializer_class = UserSerializer(queryset)
            return Response(True)
        else:
            return Response(False)
