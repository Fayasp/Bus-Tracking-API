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


class BusSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ("id", "bus_number", "route_name")


class StationSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ("id", "name", "location")
class EventDetailSchema(serializers.ModelSerializer):
    bus = BusSimpleSerializer(read_only=True)
    station = StationSimpleSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ("id", "bus", "station", "timestamp")
