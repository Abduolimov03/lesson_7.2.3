from django.shortcuts import render

from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AirPods
from .serializers import AirPodsSerializer
from rest_framework import status

@api_view(['GET',])
def air_list(request):
    airs = AirPods.objects.all()
    serializers = AirPodsSerializer(airs, many=True)
    res = {
        'dara':serializers.data,
        'count':len(airs),
        'status':status.HTTP_200_OK
    }
    return Response(serializers.data)

@api_view(['GET',])
def air_detail(request, pk):
    try:
        air = AirPods.objects.get(id=pk)
    except AirPods.DoesNotExist:
        return Response({'status':status.HTTP_400_BAD_REQUEST})
    serializer = AirPodsSerializer(air)
    return Response({
        'air':serializer.data,
        'status':status.HTTP_200_OK
    })

@api_view(['POST',])
def air_create(request):
    serializer = AirPodsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status':status.HTTP_201_CREATED})
    return Response({'status':status.HTTP_400_BAD_REQUEST})

@api_view(['POST',])
def air_update(request, pk):
    air = AirPods.objects.get(id=pk)
    serializers = AirPodsSerializer(air, data = request.data)
    if serializers.is_valid():
        serializers.save()
        return Response({'status':status.HTTP_200_OK})
    return Response({'status':status.HTTP_400_BAD_REQUEST})

@api_view(['DELETE',])
def air_delete(request, pk):
    try:
        air = AirPods.objects.get(id=pk)
    except AirPods.DoesNotExist:
        return Response({'status':status.HTTP_404_NOT_FOUND})
    air.delete()
    return Response({'status':status.HTTP_200_OK})

