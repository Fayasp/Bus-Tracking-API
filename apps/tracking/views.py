from django.shortcuts import render
from django.http import Http404
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.tracking.schema import BusDetailSchema, EventDetailSchema, StationReadonlySchema

from . models import Bus,Station,Event
from . serializers import BusListCreateSerializer, EventListCreateSerializer, StationCreateSerializer
from core.helpers.response import ResponseInfo


class StationListCreatApiview(generics.ListCreateAPIView):

    def __init__(self, **kwargs):
        self.response = ResponseInfo().response
        super().__init__(**kwargs)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
            serializer = StationCreateSerializer( data = request.data)

            if not serializer.is_valid():
                self.response["message"] = "Validation Failed"
                self.response["error"] = serializer.errors

                return Response(self.response,status.HTTP_400_BAD_REQUEST)
            serializer.save()
            self.response["message"] = "Success"
            self.response["data"] = serializer.data
            return Response(self.response,status.HTTP_200_OK)
    

class StationRetrieveApiView(generics.RetrieveAPIView):
     
     serializer_class = StationReadonlySchema
     lookup_field     = "id"
     lookup_url_kwarg = "id"
     
     def __init__(self, **kwargs):
          self.response = ResponseInfo().response
          super().__init__(**kwargs)

     def get_queryset(self):
          return super().get_queryset()

     def retrieve(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
            serializer = self.get_serializer(obj)
            self.response["message"] = "success"
            self.response["data"] = serializer.data
            return Response(self.response, status.HTTP_200_OK)
        except Http404 as e:
            self.response["message"] = "Team not found"
            return Response(self.response, status.HTTP_404_NOT_FOUND)


class BusListCreateApivew(generics.ListCreateAPIView):

    def __init__(self, **kwargs):
        self.response = ResponseInfo().response
        super().__init__(**kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        serializer = BusListCreateSerializer( data = request.body)
        if not serializer.is_valid():
            if not serializer.is_valid():
                self.response["message"] = "Validation Failed"
                self.response["error"] = serializer.errors

                return Response(self.response,status.HTTP_400_BAD_REQUEST)
            serializer.save()
            self.response["message"] = "Success"
            self.response["data"] = serializer.data
            return Response(self.response,status.HTTP_200_OK)
        

class BusDetailApiview(generics.RetrieveAPIView):

    def __init__(self, **kwargs):
        self.response = ResponseInfo().response
        super().__init__(**kwargs)

    serializer_class = BusDetailSchema
    lookup_field = "id"
    lookup_url_kwarg = "id"

    def get_queryset(self):
        return super().get_queryset()


    def retrieve(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
            serializer = self.get_serializer(obj)
            self.response["message"] = "Succes"
            self.response["data"]    = serializer.data
            return Response(self.response,status.HTTP_200_OK)
        except Http404 as e:
            self.response["Message"]  = "Bus Not Found"
            return Response(self.response,status.HTTP_404_NOT_FOUND)
        


class EventListCreateApiView(generics.ListCreateAPIView):

    queryset = Event.objects.all()
    serializer_class = EventListCreateSerializer

    def __init__(self, **kwargs):
        response = ResponseInfo().response
        super().__init__(**kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            self.response["message"] = "Validation Failed"
            self.response["error"] = serializer.errors
            return Response(self.response, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        self.response["message"] = "Success"
        self.response["data"] = serializer.data
        return Response(self.response, status=status.HTTP_201_CREATED)
    

class EventRetreveApiview(generics.RetrieveAPIView):

    def __init__(self, **kwargs):
        response = ResponseInfo().response
        super().__init__(**kwargs)


    serializer_class = EventDetailSchema
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


    def get_queryset(self):
        return super().get_queryset()
    
    def retrieve(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
            serializer = self.get_serializer(obj)
            self.response["message"] = "Succes"
            self.response["data"]    = serializer.data
            return Response(self.response,status.HTTP_200_OK)
        except Http404 as e:
            self.response["Message"]  = "Bus Not Found"
            return Response(self.response,status.HTTP_404_NOT_FOUND)


    