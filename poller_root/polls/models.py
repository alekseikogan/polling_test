from django.db import models
from django.urls import reverse


class Survey(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    # def get_absolute_url(self):
    #     return reverse("polls:survey", kwargs={"id": self.id})

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.CharField(max_length=250, verbose_name='Вопрос')
    pub_date = models.DateTimeField(verbose_name='Дата публикации')
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        related_name='questions')
    previous_question = models.ForeignKey(
        'self',
        verbose_name='Прошлый вопрос',
        related_name='children',
        on_delete=models.SET_NULL,
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100, verbose_name='Ответ')
    votes = models.PositiveIntegerField(default=0, verbose_name='Количество голосов')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.choice_text
