from rest_framework import serializers
from . models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model = Menu