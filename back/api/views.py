from django.shortcuts import render
from rest_framework import permissions, viewsets
from django.contrib.auth.models import Group, User
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .serializers import GroupSerializer, UserSerializer, ConstructionSerializer
from constructions.models import Location_Attirbutes, Construction
# import .serializers import ConstructionSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


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
    return Response(Location_Attirbutes)


@api_view(["GET"])
def GetAllConstructionsOnStation(request, station_name):
    objects = Construction.objects.filter(Location=station_name).all()
    
    serialized_objects = ConstructionSerializer(objects, many=True)
    return Response(serialized_objects.data)



    