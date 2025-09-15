from rest_framework import serializers
from . models import Station,Bus,Event

class StationCreateSerializer(serializers.ModelSerializer):

    name      = serializers.CharField(error_message={"blank" : "Please enter the station name"})
    lattitude = serializers.FloatField()
    longitude = serializers.FloatField()

    class Meta:
        model = Station
        fields = ('name','lattitude','longitude')

        