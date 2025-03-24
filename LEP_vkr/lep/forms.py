from django import forms


class LepCalculateForm(forms.Form):
    span_length = forms.FloatField(min_value=30, max_value=700, label='Длина пролета')
    t_min = forms.IntegerField(label='Минимальная температура')
    t_max = forms.IntegerField(label='Максимальная температура')
    t_avg = forms.IntegerField(label='Среднегодовая температура')
    F0 = forms.FloatField(label='Общее сечение провода')
    d = forms.FloatField(label='Диаметр провода')
    p = forms.FloatField(label='Вес провода км/кг')
    e = forms.FloatField(label='Толщина гололёда')
    q = forms.FloatField(label='Скоростной напор ветра')
    a0 = forms.FloatField(label='Коэффициент линейного расширения')
    E0 = forms.IntegerField(label='Модуль упругости материала')
    o_r = forms.FloatField(label='Допускаемое напряжение при наибольшей нагрузке')
    o_h = forms.FloatField(label='Допускаемое напряжение при низшей температуре')
    o_c = forms.FloatField(label='Допускаемое напряжение при среднегодовой температуре')