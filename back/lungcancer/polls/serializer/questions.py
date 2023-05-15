from rest_framework import serializers
from ..models import Question


class AllQuestionSerializer(serializers.ModelSerializer):
    choice = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='choice')

    class Meta:
        model = Question
        fields = '__all__'


class QuestionHandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['questionid']
