from rest_framework import serializers
from lep.models import CityInfo


class CityInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityInfo
        fields = ('id', 'city')


class LepCalculateSerializer(serializers.Serializer):
    city = serializers.PrimaryKeyRelatedField(queryset=CityInfo.objects.all())
    span_length = serializers.FloatField()
    F0 = serializers.FloatField()
    d = serializers.FloatField()
    p = serializers.FloatField()
    a0 = serializers.FloatField()
    E0 = serializers.IntegerField()
    o_r = serializers.FloatField()
    o_h = serializers.FloatField()
    o_c = serializers.FloatField()