from django.contrib import admin

from .models import Choice, Question, Survey

admin.site.site_header = "Админ-панель сайта опросов"
admin.site.site_title = "Опросы"
admin.site.index_title = "Администрация сайта"


# class ChoiceInLine(admin.StackedInline):
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None, {'fields': ['question_text']}
        ),
        (
            'Дата публикации',
            {'fields': ['pub_date'], 'classes': ['wide']} # можно collapse
        ),
    ]
    inlines = [ChoiceInLine]


class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 2


class SurveyAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None, {'fields': ['name']}
        ),
    ]
    inlines = [QuestionInLine]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Survey, SurveyAdmin)
