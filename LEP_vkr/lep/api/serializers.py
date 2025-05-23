from rest_framework import serializers
from lep.models import CityInfo, WiresInfo, SubjectInfo


class CityInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityInfo
        fields = ('id', 'city')


class SubjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectInfo
        fields = ('id', 'subject')


class WireInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WiresInfo
        fields = ('id', 'wire')


def positive_num_validator(self):
    if self <= 0:
        raise serializers.ValidationError("Значение должно быть положительным числом")


class LepCalculateSerializer(serializers.Serializer):
    # city = serializers.PrimaryKeyRelatedField(queryset=CityInfo.objects.all())
    subject = serializers.PrimaryKeyRelatedField(queryset=SubjectInfo.objects.all())
    wire = serializers.PrimaryKeyRelatedField(queryset=WiresInfo.objects.all())
    l = serializers.FloatField(min_value=30, max_value=500, validators=(positive_num_validator, ))


class LepCalculateManualSerializer(serializers.Serializer):
    t_min = serializers.FloatField()
    t_max = serializers.FloatField()
    t_avg = serializers.FloatField()
    e = serializers.IntegerField(validators=(positive_num_validator, ))
    q = serializers.IntegerField(validators=(positive_num_validator, ))
    l = serializers.FloatField(validators=(positive_num_validator,))
    F0 = serializers.FloatField(validators=(positive_num_validator, ))
    diameter = serializers.FloatField(validators=(positive_num_validator, ))
    weight = serializers.FloatField(validators=(positive_num_validator, ))
    a0 = serializers.FloatField(validators=(positive_num_validator, ))
    E0 = serializers.IntegerField(validators=(positive_num_validator, ))
    o_r = serializers.FloatField(validators=(positive_num_validator, ))
    o_c = serializers.FloatField(validators=(positive_num_validator, ))

    def validate(self, data):
        if data['t_min'] >= data['t_max']:
            raise serializers.ValidationError({
                "t_min": "Минимальная температура должна быть меньше максимальной",
                "t_max": "Максимальная температура должна быть больше минимальной"
            })
        if not(data['t_min'] < data['t_avg'] < data['t_max']):
            raise serializers.ValidationError({
                "t_min": "Минимальная температура должна быть меньше среднегодовой температуры",
                "t_max": "Максимальная температура должна быть больше среднегодовой температуры",
                "t_avg": "Среднегодовая температура должна быть меньше максимальной и больше минимальной температур"
            })
        return data