from django.db import models


class CityInfo(models.Model):
    city = models.CharField('Город', max_length=100)
    ice_zone = models.IntegerField('Район по гололеду')
    wind_zone = models.IntegerField('Район по ветровому давлению')
    avg_year_temp = models.FloatField('Среднегодовая температура')
    min_temp = models.FloatField('Минимальная температура')
    max_temp = models.FloatField('Максимальная температура')

    class Meta:
        ordering = ['city']

    def __str__(self):
        return self.city