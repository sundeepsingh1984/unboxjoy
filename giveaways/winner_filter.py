from django import template
register = template.Library()


@register.filter(name="winner")
def in_winners(registrations ):
    return registrations.filter(winner="True")