from django.contrib.auth.models import Group, User
from rest_framework import serializers
from constructions.models import Construction, ConstructionThreeDImage, Order
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class ConstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Construction
        fields = "__all__"



class ConstructionThreeDImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionThreeDImage
        fields = ["image", "construction", "neighbours"]

