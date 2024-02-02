from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=250, verbose_name='Вопрос')
    pub_date = models.DateTimeField(verbose_name='Дата публикации')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250, verbose_name='Ответ')
    votes = models.PositiveIntegerField(default=0, verbose_name='Количество голосов')

    def __str__(self):
        return self.choice_text
