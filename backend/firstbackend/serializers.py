from rest_framework import serializers
from .models import Firstbackend


class FirstbackendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firstbackend
        fields = '__all__'