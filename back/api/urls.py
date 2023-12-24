from django.urls import path

import api.views as views


# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title='Pastebin API')
# from django.conf.urls import url



urlpatterns = [
    path("", views.GetIndex, name="index"),
    path("all_stations", views.GetAllStationsOnMap, name="all_stations"),
    path("station/<str:station_name>/all_constructions", views.GetAllConstructionsOnStation, name="all_constructions_on_station"),
    path("construction/image/<int:id>", views.GetConstructionThreeDImageByID, name="construction_three_d_image_by_id"),
    path("construction/<int:id>", views.GetConstructionByID, name="construction_by_id"),
    path("tdimage/<int:id>", views.GetThreeDImageByID, name="three_d_image_by_id"),
    path("comment/all", views.GetAllComments, name="all_comments"),
    path("contact/email/save", views.saveEmailToBeContacted, name="save_email_to_be_contacted"),
]
