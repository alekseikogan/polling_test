from django import template

register = template.Library()


@register.filter
def ru_plural(value):
    '''Определяет склонение слова ГОЛОС в зависимости от количества'''
    value = int(value)

    if value % 10 == 1 and value % 100 != 11:
        variant = 'голос'
    elif value % 10 >= 2 and value % 10 <= 4 and \
            (value % 100 < 10 or value % 100 >= 20):
        variant = 'голоса'
    else:
        variant = 'голосов'

    return variant
