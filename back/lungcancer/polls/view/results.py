# 分数/概率视图
from rest_framework import generics, filters, status
from rest_framework.response import Response
from ..models import Score, Probability
from ..serializer.results import ScoreSerializer, ProbabilitySerialzer


class CalcProbability(generics.CreateAPIView):
    """
    计算5/10年期癌症概率
    """
    serializer_class = ScoreSerializer

    def smoking_status(self):
        answers = self.request.data['answers']
        print(answers)
        if (answers['smoking'] == 1):
            smoking = 'NEVER'
        else:
            if (answers['packYear'] == 3):
                smoking = 'HEAVY'
            else:
                smoking = 'LIGHT'
        return smoking

    def get_queryset(self):
        query_set = Score.objects.filter(smoke=self.smoking_status())
        return query_set

    def create(self, request, *args, **kwargs):
        answers = request.data['answers']
        queryset = self.filter_queryset(self.get_queryset())
        score = 0
        for query in queryset.iterator():
            serializer = ScoreSerializer(query)
            for k, v in answers.items():
                if (serializer.data['questionid'] == k and serializer.data['choice'] == v):
                    score += serializer.data['score']
                    print(serializer.data)

        year = request.data['year']
        prob_queryset = Probability.objects.filter(
            year=year, smoke=self.smoking_status(), point=score)
        prob_serializer = ProbabilitySerialzer(prob_queryset, many=True)

        return Response({
            "smoking": self.smoking_status(),
            "probability": prob_serializer.data[0]['probability']
        })
