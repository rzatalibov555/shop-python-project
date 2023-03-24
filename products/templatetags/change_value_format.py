from django import template

register = template.Library()


@register.filter()
def formatize(val):
    try:
        if val is not None:
            val = float(val)
            return f'{val:,.2f}'

        return val
    except Exception:
        return val