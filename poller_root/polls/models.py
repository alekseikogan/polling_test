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


# https://habr.com/ru/articles/5959/
class Question(models.Model):
    question_text = models.CharField(max_length=250, verbose_name='Вопрос')
    pub_date = models.DateTimeField(verbose_name='Дата публикации')
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        related_name='questions')
    code = models.CharField(max_length=15, unique=True, null=False, blank=False)
    previous_question = models.ForeignKey(
        'self',
        verbose_name='Прошлый вопрос',
        related_name='children',
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    path = models.CharField(max_length=255, null=False, editable=False)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    # https://pyformat.info/
    def __str__(self):
        return "%s%s" % ('------'[:self.path.count('/', 2)-1], self.question_text)

    def save(self):
        if self.previous_question:
            self.path = f'{self.previous_question.path}{self.code}/'
        else:
            self.path = f'/{self.code}/'
            super(type(self), self).save()
        for a in Question.objects.filter(previous_question=self.id):
            a.save()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100, verbose_name='Ответ')
    votes = models.PositiveIntegerField(default=0, verbose_name='Количество голосов')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.choice_text
