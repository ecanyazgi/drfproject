from .serializers import NewUserCreateSerializer
from rest_framework import mixins,permissions,viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import BasePermission
from .models import NewUser

class IsNotAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)


class NewUserRegistrationViewSet(mixins.CreateModelMixin,GenericViewSet):
    # permission_classes = (IsNotAuthenticated)
    queryset = NewUser.objects.all()
    serializer_class = NewUserCreateSerializer



