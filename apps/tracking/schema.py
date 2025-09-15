from rest_framework import serializers
from . models import Bus,Event,Station


class StationReadonlySchema(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ('name','lattitude','longitude')


class BusDetailSchema(serializers.ModelSerializer):

    class Meta:
        model = Bus
        fields = ('name','bus_number','route_name')