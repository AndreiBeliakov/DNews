from django import template


register = template.Library()

CENSOR_WORDS = [
    'редиска',
    'Редиска'
]

@register.filter()
def censor(value):
    """
    text: 'редиска'
    """
    for word in CENSOR_WORDS:
        value = value.replace(word, '*' * len(word))
    return value