from rest_framework import serializers
from ..models import History, Detail


class DetailListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "questionid": value.questionid_id,
            "choice": value.choice
        }


class HistorySerializer(serializers.ModelSerializer):
    detail = DetailListingField(
        many=True, read_only=True)

    class Meta:
        model = History
        fields = '__all__'


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)
