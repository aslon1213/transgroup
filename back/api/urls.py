from django.urls import path

import api.views as views

urlpatterns = [
    path("", views.GetIndex, name="index"),
    path("all_stations", views.GetAllStationsOnMap, name="all_stations"),
    path("station/<str:station_name>/all_constructions", views.GetAllConstructionsOnStation, name="all_constructions_on_station"),
]