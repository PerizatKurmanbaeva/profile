from datetime import date, datetime

from django.db import models


# Create your models here.

class People(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    date_of_birth = models.DateField('Дата рождения')
    # date_now = datetime.now().date()
    # diff = relativedelta(date_now, date_of_birth)

    def age(self):
        import datetime
        return datetime.date.today() - self.date_of_birth

