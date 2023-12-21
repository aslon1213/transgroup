from django.contrib.auth.models import Group, User
from rest_framework import serializers
from constructions.models import Construction, ConstructionThreeDImage, Order, SubwayStation
from web_contents.models import Comment, ContentItem
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SubwayStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubwayStation
        fields = "__all__"




class ConstructionThreeDImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionThreeDImage
        fields = "__all__"


class ConstructionSerializer(serializers.ModelSerializer):
    subway_station_location = SubwayStationSerializer()
    threedimage = ConstructionThreeDImageSerializer()
    class Meta:
        model = Construction
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


