from rest_framework import serializers
from ..models import Score, Probability


# 取出分数
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'


# 取出概率
class ProbabilitySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Probability
        fields = '__all__'
