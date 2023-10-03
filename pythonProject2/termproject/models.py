from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Question(models.Model):
    question_id = models.IntegerField(blank=True, null=True)
    question=models.CharField(max_length=200)
    op_1=models.CharField(max_length=200)
    op_2 = models.CharField(max_length=200)
    op_3 = models.CharField(max_length=200)
    op_4 = models.CharField(max_length=200)
    ans=models.CharField(max_length=200)

    def __str__(self):
        return self.question

class Quiz(models.Model):
    question_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=50, null=True)
    score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user_name