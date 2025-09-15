from django.db import models

class Station(models.Model):

    name      = models.CharField(max_length=100,null=False,blank=True)
    lattitide = models.FloatField()
    longitude = models.FloatField()


    def __str__(self):
        return self.name

class Bus(models.Model):

    bus_number = models.CharField(max_length=50, unique=True)
    route_name = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.bus_number} = {self.route_name}"
    

class Event(models.Model):

    bus        = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name="event")
    station    = models.ForeignKey(Station, on_delete=models.CASCADE)
    timestamp  = models.DateTimeField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.bus.bus_number} at {self.station.name} on {self.timestamp}"