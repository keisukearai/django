from django import template
register = template.Library()

@register.filter
def get_search_query_param(value):
    result = ''
    for k, v in value:
        if k != 'page':
            result += f'&{k}={v}'
    return result

@register.filter
def num_to_str(value):
    return str(value)