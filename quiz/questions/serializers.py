from rest_framework import serializers
from answers.serializers import AnswerSerializer


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question_text = serializers.CharField(max_length=200)
    answer = AnswerSerializer()

#
#     def get_lot_units(self, obj):
#         return []
#         # return list(obj.lot_units)
#
#     def create(self, validated_data, recipe_id):
#         results = []
#         for unit in validated_data:
#             results.append(RecipeUnit.objects.create(**unit, recipe_id=recipe_id))
#         return results
#
#     def update(self, instance, validated_data):
#         pass
