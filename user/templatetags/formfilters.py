from django import template

register = template.Library()


@register.filter(name="inputField")
def input_field(value):
    return value.as_widget(attrs={"class": "form-control"})
