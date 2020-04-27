from django.shortcuts import render
from typing import Union, Type, List
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from core.serializers import AppSerializer, UpdateAppSerializer, AppAPISerializer
from core.models import App
from rest_framework import status, mixins, viewsets, permissions
from fabrika.base import MarkAsDeletedMixin
from fabrika.stubs import QueryType
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

class AppViewSet(mixins.CreateModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.ListModelMixin,
                              MarkAsDeletedMixin,
                              viewsets.GenericViewSet):
    queryset: QueryType[App] = App.objects.non_deleted()
    permission_classes = [IsAdminUser, AllowAny]

    def get_permissions(self) -> Union[List[AllowAny],
                                       List[IsAdminUser]]:

        if self.action == "list" or self.action == "test":
            return [AllowAny(), ]
        return [IsAdminUser(), ]

    def get_serializer_class(self) -> Union[Type[AppSerializer],
                                            Type[UpdateAppSerializer]]:

        if self.action == 'update' or self.action == "partial_update":
            return UpdateAppSerializer
        elif self.action == 'test':
            return AppAPISerializer
        return AppSerializer

    def get_queryset(self) -> QueryType[App]:
        if self.request.user.is_staff:
           return App.objects.all()
        return App.objects.non_deleted()

    @action(detail=False, methods=['POST'], permission_classes=[AllowAny])
    def test(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer_class()
        serializer = serializer(data=self.request.data, many=False)
        if serializer.is_valid():
            api = serializer.data['api']
            apps = App.objects.non_deleted().filter(api=api)
            serializer = AppSerializer(apps, many=True)
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

