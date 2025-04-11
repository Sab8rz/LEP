from rest_framework import serializers
from lep.models import CityInfo, WiresInfo


class CityInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityInfo
        fields = ('id', 'city')


class WireInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WiresInfo
        fields = ('id', 'wire')


class LepCalculateSerializer(serializers.Serializer):
    city = serializers.PrimaryKeyRelatedField(queryset=CityInfo.objects.all())
    wire = serializers.PrimaryKeyRelatedField(queryset=WiresInfo.objects.all())
    span_length = serializers.FloatField()