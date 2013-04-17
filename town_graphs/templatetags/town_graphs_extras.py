from django import template

register = template.Library()

@register.filter
def normalize_icons(value):
    return value.replace(" ", "_").replace("/", "_")
    
@register.filter
def normalize_vars(value):
    return normalize_icons(value).replace("-", "_").replace("+", "_").replace(".", "_")

@register.filter
def get_partido_key(value, arg):
    voto = value[arg]
    return voto.partido.name

@register.filter
def get_key(value, arg):
    return value[arg]
