from rest_framework import serializers

from .models import City, TransportType, StationType, Station, Region, Country


class CitySerializer(serializers.ModelSerializer):

    region_name = serializers.StringRelatedField(source='region.name')
    region_code = serializers.StringRelatedField(source='region.yandex_region_code')
    country_name = serializers.StringRelatedField(source='country.name')
    country_code = serializers.StringRelatedField(source='region.yandex_country_code')

    class Meta:
        model = City
        fields = (
            'name',
            'yandex_city_code',
            'region_name',
            'country_name',
            'region_code',
            'country_code',
        )


class TransportTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransportType
        fields = '__all__'


class StationTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = StationType
        fields = '__all__'


class StationSerializer(serializers.ModelSerializer):

    city_name = serializers.StringRelatedField(source='city.name')
    city_code = serializers.StringRelatedField(source='city.yandex_city_code')
    region_name = serializers.StringRelatedField(source='city.region.name')
    country_name = serializers.StringRelatedField(source='city.country.name')
    station_type = serializers.StringRelatedField(source='station_type.station_type')
    transport_type = serializers.StringRelatedField(source='transport_type.transport_type')

    class Meta:
        model = Station
        fields = (
            'name',
            'station_code',
            'longitude',
            'latitude',
            'city_name',
            'city_code',
            'station_type',
            'transport_type',
            'region_name',
            'country_name',
        )


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'
