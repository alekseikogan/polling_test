from django.contrib import admin

from .models import Choice, Question

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
            {'fields': ['pub_date'], 'classes': ['wide']} # можно wide
        ),
    ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
