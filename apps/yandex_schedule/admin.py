from django.contrib import admin

from apps.yandex_schedule.models import City, TransportType, StationType, Station


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'yandex_city_code']


@admin.register(TransportType)
class TransportTypeAdmin(admin.ModelAdmin):
    list_display = ['transport_type']


@admin.register(StationType)
class StationTypeAdmin(admin.ModelAdmin):
    list_display = ['station_type']


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ['name', 'station_code', 'longitude', 'latitude',
                    'city', 'station_type', 'transport_type']
    list_filter = ['name', 'station_code', 'station_type', 'transport_type']
    search_fields = ['name', 'city', 'station_code', 'station_type', 'transport_type']
