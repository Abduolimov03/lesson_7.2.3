from rest_framework import serializers
from .models import AirPods

class AirPodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirPods
        fields = '__all__'