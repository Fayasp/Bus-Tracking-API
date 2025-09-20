from rest_framework import serializers
from . models import Station,Bus,Event

class StationCreateSerializer(serializers.ModelSerializer):

    name      = serializers.CharField(error_message={"blank" : "Please enter the station name"})
    lattitude = serializers.FloatField()
    longitude = serializers.FloatField()

    class Meta:
        model = Station
        fields = ('name','lattitude','longitude')


from rest_framework import serializers
from . models import Bus


class BusListCreateSerializer(serializers.ModelSerializer):

    name        = serializers.CharField(error_message = {"blank" : "Please enter  the bus name"})
    bus_number  = serializers.FloatField()
    route_name  = serializers.CharField(error_message = {"blank" : "Please enter  the route name"})

    class Meta:
        model = Bus
        fields = ('name','bus_number','route_name')
        

class busSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ('id','name','bus_number','route_name')

class StationSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ("id", "name", "lattitide", "longitude")

class EventListCreateSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Event
            fields = ('bus','station','time_stamp')


    

        bus      = serializers.PrimaryKeyRelatedField(queryset= Bus.objects.all())
        station  = serializers.PrimaryKeyRelatedField(query_set = Station.objects.all())

        
