from django import template

register = template.Library()

@register.filter()
def age(self):
    import datetime
    age = datetime.date.today() - self.date_of_birth
    return int(age.days / 365)