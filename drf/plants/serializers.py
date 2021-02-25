# from django.conf import settings
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import (
    Category,
    Plant,
    Room,
    UserPlant,
)


class UserMixin(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


class AdminCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "description",
            "slug",
            "user",
            "image_url",
            "url",
        ]
        extra_kwargs = {"url": {"lookup_field": "slug"}}


class CategorySerializer(UserMixin, AdminCategorySerializer):
    pass


class AdminRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "id",
            "name",
            "description",
            "user",
            "exposure",
            "humidity",
            "temperature",
            "drafty",
            "url",
        ]


class RoomSerializer(UserMixin, AdminRoomSerializer):
    pass


class AdminPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = [
            "id",
            "name",
            "description",
            "user",
            "category",
            "watering_interval",
            "fertilizing_interval",
            "required_exposure",
            "required_humidity",
            "required_temperature",
            "blooming",
            "difficulty",
        ]


class PlantSerializer(UserMixin, AdminPlantSerializer):
    pass


class AdminUserPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlant
        fields = [
            "id",
            "name",
            "description",
            "user",
            "room",
            "plant",
            "last_watered",
            "last_fertilized",
            "image_url",
        ]


class UserPlantSerializer(UserMixin, AdminUserPlantSerializer):
    pass


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        ]
