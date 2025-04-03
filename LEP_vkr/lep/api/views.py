from rest_framework.response import Response
from rest_framework.views import APIView

from lep.api.serializers import CityInfoSerializer, LepCalculateSerializer
from lep.models import CityInfo
from lep.utils import LepCalculator


class CityAPI(APIView):
    def get(self, request):
        cities = CityInfo.objects.all()
        serializer = CityInfoSerializer(cities, many=True)
        return Response(serializer.errors, status=400)


class LepCalculateAPI(APIView):
    def post(self, request):
        serializer = LepCalculateSerializer(data=request.data)
        if serializer.is_valid():
            calc = LepCalculator(**serializer.validated_data)
            res = calc.calculate_all()
            return Response({'result': res})
        return Response(serializer.errors, status=400)