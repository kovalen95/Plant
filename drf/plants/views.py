from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from .models import (
    Category,
    Plant,
    Room,
    UserPlant,
)

from .serializers import (
    AdminCategorySerializer,
    CategorySerializer,
    AdminRoomSerializer,
    RoomSerializer,
    AdminPlantSerializer,
    PlantSerializer,
    AdminUserPlantSerializer,
    UserPlantSerializer,
    UserSerializer,
)


class AdminViewSetMixin:
    model = None
    admin_serializer_class = None
    user_serializer_class = None

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.model.objects.all()
        return self.model.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return self.admin_serializer_class
        return self.user_serializer_class


class CategoryViewSet(AdminViewSetMixin, viewsets.ModelViewSet):
    lookup_field = "slug"
    model = Category
    admin_serializer_class = AdminCategorySerializer
    user_serializer_class = CategorySerializer


class RoomViewSet(AdminViewSetMixin, viewsets.ModelViewSet):
    model = Room
    admin_serializer_class = AdminRoomSerializer
    user_serializer_class = RoomSerializer


class PlantViewSet(AdminViewSetMixin, viewsets.ModelViewSet):
    model = Plant
    admin_serializer_class = AdminPlantSerializer
    user_serializer_class = PlantSerializer


class UserPlantViewSet(AdminViewSetMixin, viewsets.ModelViewSet):
    model = UserPlant
    admin_serializer_class = AdminUserPlantSerializer
    user_serializer_class = UserPlantSerializer


class ProfileRetrieveView(RetrieveAPIView):
    # retrieve == GET /object/<pk>
    def retrieve(self, request, pk=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
