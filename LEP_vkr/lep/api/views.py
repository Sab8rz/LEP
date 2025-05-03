from rest_framework.response import Response
from rest_framework.views import APIView

from lep.api.serializers import CityInfoSerializer, LepCalculateSerializer, WireInfoSerializer, \
    LepCalculateManualSerializer, SubjectInfoSerializer
from lep.models import CityInfo, WiresInfo, SubjectInfo
from lep.utils import LepCalculator, LepCalculatorManual


class CityAPI(APIView):
    def get(self, request):
        cities = CityInfo.objects.all()
        serializer = CityInfoSerializer(cities, many=True)
        return Response(serializer.data)


class SubjectAPI(APIView):
    def get(self, request):
        subjects = SubjectInfo.objects.all().order_by('id')
        serializer = SubjectInfoSerializer(subjects, many=True)
        return Response(serializer.data)


class WireAPI(APIView):
    def get(self, request):
        wires = WiresInfo.objects.all()
        serializer = WireInfoSerializer(wires, many=True)
        return Response(serializer.data)


class LepCalculateAPI(APIView):
    def post(self, request):
        serializer = LepCalculateSerializer(data=request.data)
        if serializer.is_valid():
            calc = LepCalculator(**serializer.validated_data)
            combination, descr, max_sag = calc.calculate_all()
            return Response({
                'combination': combination,
                'descr': descr,
                'max_sag': max_sag
            })
        return Response(serializer.errors, status=400)


class LepCalculateManualAPI(APIView):
    def post(self, request):
        serializer = LepCalculateManualSerializer(data=request.data)
        if serializer.is_valid():
            calc = LepCalculatorManual(**serializer.validated_data)
            combination, descr, max_sag = calc.calculate_all()
            return Response({
                'combination': combination,
                'descr': descr,
                'max_sag': max_sag
            })
        return Response(serializer.errors, status=400)