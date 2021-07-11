from django.db import models


class City(models.Model):
    name = models.CharField(verbose_name='Название города', max_length=100)
    yandex_city_code = models.CharField(verbose_name='Код города Яндекса', max_length=100,
                                        unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название города'
        verbose_name_plural = 'Названия городов'


class TransportType(models.Model):
    transport_type = models.CharField(verbose_name='Тип транспорта', max_length=100, unique=True)

    def __str__(self):
        return self.transport_type

    class Meta:
        verbose_name = 'Тип транспорта'
        verbose_name_plural = 'Типы транспорта'


class StationType(models.Model):
    station_type = models.CharField(verbose_name='Тип станции', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Тип станции'
        verbose_name_plural = 'Типы станций'


class Station(models.Model):
    name = models.CharField(verbose_name='Название станции', max_length=100)
    station_code = models.CharField(verbose_name='Яндекс код станции', max_length=100, unique=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=27, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=27, blank=True, null=True)
    city = models.ForeignKey(City, verbose_name='Город станции', on_delete=models.RESTRICT,
                             null=True, blank=True)
    station_type = models.ForeignKey(StationType, verbose_name='Тип станции', on_delete=models.RESTRICT)
    transport_type = models.ForeignKey(TransportType, verbose_name='Тип транспорта', on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'
