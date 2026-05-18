
from django import template

register = template.Library()

@register.filter
def format_number(value):
    value = str(int(value))

    last_three = value[-3:]
    remaining = value[:-3]

    if remaining:
        remaining = ",".join(
            [remaining[max(i - 2, 0):i] for i in range(len(remaining), 0, -2)][::-1]
        )
        return remaining + "," + last_three

    return last_three