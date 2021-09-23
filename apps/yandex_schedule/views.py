from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, generics

from .models import City, TransportType, StationType, Station, Region, Country
from .serializers import CitySerializer, TransportTypeSerializer, \
    StationTypeSerializer, StationSerializer, RegionSerializer, CountrySerializer
from services.tools.custom_permissions import CanRead


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [CanRead]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']


class TransportTypeViewSet(ModelViewSet):
    queryset = TransportType.objects.all()
    serializer_class = TransportTypeSerializer
    permission_classes = [CanRead]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['transport_type']


class StationTypeViewSet(ModelViewSet):
    queryset = StationType.objects.all()
    serializer_class = StationTypeSerializer
    permission_classes = [CanRead]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['station_type']


class StationViewSet(ModelViewSet):
    queryset = Station.objects.select_related('city', 'transport_type', 'station_type')
    serializer_class = StationSerializer
    permission_classes = [CanRead]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['city__name', 'station_type__station_type', 'transport_type__transport_type',
                     'city__country__name', 'city__region__name', 'name']


class RegionViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [CanRead]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'yandex_region_code']


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [CanRead]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'yandex_country_code']
