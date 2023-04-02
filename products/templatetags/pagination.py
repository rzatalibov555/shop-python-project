from django import template

register = template.Library()

#TODO: bu tamplatetagsdaki pagination tam deyil. (numune kimidir)
@register.filter()
def create_range(paginator, products):
    if products.number + 2 > paginator.num_pages:
        return range(products.number - 2, paginator.num_pages)
    if products.number - 2 < 1:
        return range(1, products.number + 2)
    return range(products.number - 2, products.number + 3)