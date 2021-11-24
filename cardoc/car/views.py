from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.validators import ValidationError

from user.models import User
from car.models import Tire
from .serializers import TireListSerializer


class TireListViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Tire.objects.all()
    serializer_class = TireListSerializer
    permission_class = IsAuthenticated
    pagination_class = PageNumberPagination

    def create(self, request, *arg, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    def get_queryset(self):
        name = self.request.query_params.get('name')
        user_id = User.objects.get(name = name).id

        if name:
            searchedData = Tire.objects.filter(user_id = user_id)

            if not searchedData:
                raise ValidationError('no data')

            return searchedData
