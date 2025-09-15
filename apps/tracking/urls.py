from django.urls import path
from . import views

urlpatterns = [

    path("station-list-create",views.StationListCreatApiview.as_view()),
    path("station-retrieve/<int:id>", views.StationRetrieveApiView.as_view())
]