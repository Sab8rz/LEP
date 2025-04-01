from django import forms
from .models import CityInfo


class LepCalculateForm(forms.Form):
    city = forms.ModelChoiceField(
        label='Город',
        queryset=CityInfo.objects.all().order_by('city'),
        empty_label='Выберите город'
    )
    span_length = forms.FloatField(min_value=30, max_value=700, label='Длина пролета')
    F0 = forms.FloatField(label='Общее сечение провода')
    d = forms.FloatField(label='Диаметр провода')
    p = forms.FloatField(label='Вес провода км/кг')
    a0 = forms.FloatField(label='Коэффициент линейного расширения')
    E0 = forms.IntegerField(label='Модуль упругости материала')
    o_r = forms.FloatField(label='Допускаемое напряжение при наибольшей нагрузке')
    o_h = forms.FloatField(label='Допускаемое напряжение при низшей температуре')
    o_c = forms.FloatField(label='Допускаемое напряжение при среднегодовой температуре')