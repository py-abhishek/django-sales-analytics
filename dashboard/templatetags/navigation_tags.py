from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, *url_names):
    request = context['request']
    
    current_url = request.resolver_match.url_name

    if current_url in url_names:
        return 'active'
    return ''


@register.simple_tag(takes_context=True)
def show_menu(context, *url_names):
    request = context['request']

    current_url = request.resolver_match.url_name

    if current_url in url_names:
        return 'show'
    return ''