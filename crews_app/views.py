from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from crews_app.serializers import LotSerializer, ZalogaSerializer
from django.shortcuts import render
from django.shortcuts import redirect
from airplanes_app.models import Lot, Zaloga
import datetime

@login_required
@csrf_protect
def zalogi(request):
    return render(request, 'crews_app/zalogi.html')

@login_required
@csrf_protect
@api_view(['GET'])
def rest_zalogi(request):
    zalogi = Zaloga.objects.all()
    serializer = ZalogaSerializer(zalogi, many=True)
    return JsonResponse(serializer.data, safe=False)

@login_required
@csrf_protect
@api_view(['GET'])
def rest_loty(request, data):
    if request.method == 'GET':
        try:
            loty = Lot.objects.all().filter(czas_startu__date=data).order_by('czas_startu')
            serializer = LotSerializer(loty, many=True)
            return JsonResponse(serializer.data, safe=False)
        except ValidationError:
            return HttpResponse("");

@login_required
@csrf_protect
@api_view(['PATCH'])
def rest_zmiana_zalogi(request):
    if request.method == 'PATCH':
        lot = Lot.objects.get(id=request.data["id"])
        if request.data["zaloga"] == 'None':
            lot.zaloga = None
        else:
            zaloga = Zaloga.objects.get(id=request.data["zaloga"])
            obecne_loty = Lot.objects.all().filter(czas_startu__lte=lot.czas_ladowania).filter(czas_ladowania__gte=lot.czas_startu)
            obecne_loty_zalogi = obecne_loty.filter(zaloga=zaloga.id)
            if obecne_loty_zalogi.count() > 0:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            lot.zaloga = zaloga
        serializer = LotSerializer(lot, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
