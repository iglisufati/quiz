from rest_framework import serializers
from answers.serializers import AnswerSerializer


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question_text = serializers.CharField(max_length=200)
    answers = AnswerSerializer(many=True)