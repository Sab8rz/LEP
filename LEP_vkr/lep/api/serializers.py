from rest_framework.serializers import ValidationError, PrimaryKeyRelatedField, FloatField, IntegerField
from adrf.serializers import ModelSerializer, Serializer
from lep.models import WiresInfo, SubjectInfo


class SubjectInfoSerializer(ModelSerializer):
    class Meta:
        model = SubjectInfo
        fields = ('id', 'subject')


class WireInfoSerializer(ModelSerializer):
    class Meta:
        model = WiresInfo
        fields = ('id', 'wire')


def positive_num_validator(self):
    if self <= 0:
        raise ValidationError("Значение должно быть положительным числом")


class LepCalculateSerializer(Serializer):
    subject = PrimaryKeyRelatedField(queryset=SubjectInfo.objects.all())
    wire = PrimaryKeyRelatedField(queryset=WiresInfo.objects.all())
    l = FloatField(min_value=30, max_value=700, validators=(positive_num_validator, ))


class LepCalculateManualSerializer(Serializer):
    t_min = FloatField()
    t_max = FloatField()
    t_avg = FloatField()
    e = IntegerField(validators=(positive_num_validator, ))
    q = IntegerField(validators=(positive_num_validator, ))
    l = FloatField(min_value=30, max_value=700, validators=(positive_num_validator, ))
    F0 = FloatField(validators=(positive_num_validator, ))
    diameter = FloatField(validators=(positive_num_validator, ))
    weight = FloatField(validators=(positive_num_validator, ))
    a0 = FloatField(validators=(positive_num_validator, ))
    E0 = IntegerField(validators=(positive_num_validator, ))
    o_r = FloatField(validators=(positive_num_validator, ))
    o_c = FloatField(validators=(positive_num_validator, ))

    def validate(self, data):
        if data['t_min'] >= data['t_max']:
            raise ValidationError({
                "t_min": "Минимальная температура должна быть меньше максимальной",
                "t_max": "Максимальная температура должна быть больше минимальной"
            })
        if not(data['t_min'] < data['t_avg'] < data['t_max']):
            raise ValidationError({
                "t_min": "Минимальная температура должна быть меньше среднегодовой температуры",
                "t_max": "Максимальная температура должна быть больше среднегодовой температуры",
                "t_avg": "Среднегодовая температура должна быть меньше максимальной и больше минимальной температур"
            })
        return data