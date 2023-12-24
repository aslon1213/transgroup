from django.shortcuts import render
from rest_framework import permissions, viewsets
from django.contrib.auth.models import Group, User
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .serializers import GroupSerializer, UserSerializer, ConstructionSerializer, SubwayStationSerializer, ConstructionThreeDImageSerializer, CommentSerializer
from constructions.models import Location_Attirbutes, Construction, SubwayStation, ConstructionThreeDImage
from web_contents.models import Comment, ContentItem, EmailToBeContacted
# import .serializers import ConstructionSerializer
import json
@api_view(["GET"])
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(["GET"])
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(["GET"])
def GetIndex(request):
    return Response({"message": "Hello, world!"})

@api_view(["GET"])
def GetAllStationsOnMap(request):
    all_stations = SubwayStationSerializer(SubwayStation.objects.all(), many=True).data

    return Response(all_stations)


@api_view(["GET"])
def GetAllConstructionsOnStation(request, station_name):


    station = SubwayStation.objects.filter(name=station_name).first()

    objects = Construction.objects.filter(subway_station_location = station).all()
    
    serialized_objects = ConstructionSerializer(objects, many=True)
    data = serialized_objects.data
    # for d in data:
    #     d["subway_station_location"] = station.__dict__
    print(data)
    return Response(data)


@api_view(["GET"])
def GetConstructionThreeDImageByID(request, id):
    image = ConstructionThreeDImage.objects.filter(id=id).first()
    data = ConstructionThreeDImageSerializer(image).data
    return Response(data)
@api_view(["GET"])
def GetConstructionByID(request, id):
    construction = Construction.objects.filter(id=id).first()
    data = ConstructionSerializer(construction).data
    return Response(data)


@api_view(["GET"])
def GetThreeDImageByID(request, id):
    image = ConstructionThreeDImage.objects.filter(id=id).first()
    data = ConstructionThreeDImageSerializer(image).data
    return Response(data)




@api_view(["GET"])
def GetAllComments(request, id):
    try:
        comments = Comment.objects.filter(user_id=id).all()
        data = CommentSerializer(comments, many=True).data
    except Exception as e:
        return Response({"error": e.__str__()})
    return Response(data)



@api_view(["POST"])
def saveEmailToBeContacted(request):
    email = request.data["email"]
    
    try:
        email = EmailToBeContacted.objects.create(email=email)
        email.save()
    except Exception as e:
        return Response({"error": e.__str__()})
    return Response({"message": "success"})