from django.urls import path

from .views import CityViewSet, StationTypeViewSet, TransportTypeViewSet, StationViewSet

urlpatterns = [
    path('yandex_schedule_city', CityViewSet),
    path('yandex_schedule_transport_type', TransportTypeViewSet),
    path('yandex_schedule_station_type', StationTypeViewSet),
    path('yandex_schedule_station', StationViewSet)
]
