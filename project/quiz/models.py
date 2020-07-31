from django.db import models

# Create your models here.

class Quiz(models.Model):
    player = models.OneToOneField(Player)
    correct_count = models.IntegerField(default=0)
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=300)
    answer_index = models.IntegerField(default=0)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=300)
    choose = models.BooleanField(default=False)



