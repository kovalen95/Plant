from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("category", views.CategoryViewSet, basename="category")
router.register("room", views.RoomViewSet, basename="room")
router.register("plant", views.PlantViewSet, basename="plant")
router.register("user-plant", views.UserPlantViewSet, basename="user-plant")


urlpatterns = [
    path("", include(router.urls)),
    path("profile/", views.ProfileRetrieveView.as_view(), name="profile"),
]
