from django import template

register = template.Library()

@register.filter
def count(value):
	return len(value)

@register.filter
def space_to_dash(value):
	return value.replace(" ","_")