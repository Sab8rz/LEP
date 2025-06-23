from adrf.views import APIView
from asgiref.sync import sync_to_async
from rest_framework.response import Response

from lep.api.serializers import LepCalculateSerializer, WireInfoSerializer, \
    LepCalculateManualSerializer, SubjectInfoSerializer
from lep.models import WiresInfo, SubjectInfo
from lep.utils import LepCalculator, LepCalculatorManual


class SubjectAPI(APIView):
    async def get(self, request):
        subjects = await sync_to_async(list)(SubjectInfo.objects.all().order_by('subject'))
        serializer = SubjectInfoSerializer(subjects, many=True)
        return Response(serializer.data)


class WireAPI(APIView):
    async def get(self, request):
        wires = await sync_to_async(list)(WiresInfo.objects.all())
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