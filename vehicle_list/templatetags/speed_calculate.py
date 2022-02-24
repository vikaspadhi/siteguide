from django import template

register = template.Library()

@register.filter(name='speed_calculate')
def speed_calculate(value):
    return (int(value)/500)*180


    