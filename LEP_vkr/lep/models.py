from django.db import models


class SubjectInfo(models.Model):
    subject = models.CharField('Субъект', max_length=100)
    ice_zone = models.IntegerField('Район по гололеду')
    wind_zone = models.IntegerField('Район по ветровому давлению')
    avg_year_temp = models.FloatField('Среднегодовая температура')
    min_temp = models.FloatField('Абсолютная минимальная температура')
    max_temp = models.FloatField('Абсолютная максимальная температура')

    class Meta:
        ordering = ['subject']

    def __str__(self):
        return self.subject


class WiresInfo(models.Model):
    wire = models.CharField('Марка провода', max_length=15)
    gen_cross_sec = models.FloatField('Общее сечение')
    diametr = models.FloatField('Диаметр')
    weight = models.FloatField('Вес')
    coef_lin_exp = models.FloatField('Коэффициент линейного расширения')
    mod_elast_mat = models.IntegerField('Модуль упругости материала')
    max_vol = models.FloatField('Допускаемое напряжение (наибольшие нагрузки)')
    avg_vol = models.FloatField('Допускаемое напряжение (среднегодовая температура)')

    def __str(self):
        return self.wire