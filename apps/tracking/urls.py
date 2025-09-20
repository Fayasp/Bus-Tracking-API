from django.urls import path
from . import views

urlpatterns = [

  path('bus-list-create',views.BusListCreateApivew.as_view()),
    path("bus-detail/<int:id>",views.BusDetailApiview.as_view()),

    path("station-list-create",views.StationListCreatApiview.as_view()),
    path("station-retrieve/<int:id>", views.StationRetrieveApiView.as_view()),

    path('event-list-create', views.EventListCreateApiView.as_view()),
    path('event-retrieve/<int:id>',views.EventRetreveApiview.as_view)
]