from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'

    category_name = models.CharField(max_length=50)

    def get_question(self):
        return self


class AnswerModel(models.Model):
    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        db_table = 'answer'

    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)


    def get_answer(self):
        return self

class QuestionModel(models.Model):
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        db_table = 'question'

    question_text = models.CharField(max_length=200)
    category = models.ManyToManyField(CategoryModel, related_name='category')
    answers =  models.ManyToManyField(AnswerModel, related_name='answer')

    def get_question(self):
        return self


class ResponseModel(models.Model):
    class Meta:
        verbose_name = 'Response'
        verbose_name_plural = 'Responses'
        db_table = 'response'

    questions = models.ManyToManyField(QuestionModel, related_name='question')
    difficulty_level = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    timer = models.IntegerField(default=0)

    def get_response(self):
        return self
