import requests
from typing import List
import logging

from db_functions import DbFunctions
from get_schedule_info import YandexScheduleInfoHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class YandexScheduleInfoInsertToDatabase:

    def __init__(self, yandex_schedule_token: str, yandex_schedule_url: str,
                 db_functions: DbFunctions):
        self.token = yandex_schedule_token
        self.url = yandex_schedule_url
        self.db_functions = db_functions

    @staticmethod
    def get_yandex_schedule_codes_json(token, url):
        logger.info('Start get_yandex_schedule_codes_json function')
        full_url = f'{url}/v3.0/stations_list/?apikey={token}&lang=ru_RU&format=json'
        response = requests.get(full_url)
        logger.info('Function get_yandex_schedule_codes_json: done')
        return response.json()

    def get_info_to_parse(self) -> dict:
        """
        Получаем аттрибуты токен и url яндекс расписаний для запроса кодов сервиса.
        На выходе имеем словарь со всеми кодами и информацией о наседеных путнках и
        станций, которые к ним относятся.
        """
        logger.info('Start get_info_to_parse function')
        settlements_info = self.get_yandex_schedule_codes_json(self.token, self.url)
        countries_list = [item for item in settlements_info.get('countries')]
        info = YandexScheduleInfoHandler.get_all_info(countries_list)
        info_dict = {k: v for item in info for k, v in item.items()}
        logger.info('Function get_info_to_parse: done')
        return info_dict

    def station_info_to_write(self, info_to_parse: dict):
        logger.info('Start station_info_to_write function')
        for key, value in info_to_parse.items():
            city_and_station_info = YandexScheduleInfoInsertToDatabase.get_city_and_station_info(key, value)
            stations_info = self.get_stations_to_insert_info(city_and_station_info)
            stations_to_insert = YandexScheduleInfoInsertToDatabase.get_unique(stations_info)
            self.insert_stations(stations_to_insert)
        logger.info('Function station_info_to_write: done')

    def get_stations_to_insert_info(self, city_and_station_info: List[dict]) -> List[tuple]:
        logger.info('Start get_stations_to_insert_info function')
        stations_info_to_insert: List = []
        cities_info_from_db = self.db_functions.select_all_cities()
        transport_type_info_from_db = self.db_functions.select_all_transport_types()
        station_type_info_from_db = self.db_functions.select_all_station_types()
        for item in city_and_station_info:
            city_code = item.get('city_code') if item.get('city_code') else ' Нет данных'
            transport_type = item.get('transport_type')
            station_type = item.get('station_type')
            city_id = [i[0] for i in cities_info_from_db if i[2] == city_code]
            city_id = city_id[0] if city_id != [] else None
            transport_type_id = [i[0] for i in transport_type_info_from_db if i[1] == transport_type][0]
            station_type_id = [i[0] for i in station_type_info_from_db if i[1] == station_type][0]
            station_code = item.get('station_code')
            name = item.get('station_name')
            item_longitude = item.get('longitude')
            item_latitude = item.get('latitude')
            longitude = None if item_longitude == '' else float(item_longitude)
            latitude = None if item_latitude == '' else float(item_latitude)
            insert_info: tuple = (name, station_code, longitude, latitude,
                                  city_id, station_type_id, transport_type_id,)
            stations_info_to_insert.append(insert_info)
        logger.info('Function get_stations_to_insert_info: done')
        return stations_info_to_insert

    def insert_stations(self, stations_info: List[tuple]):
        logger.info('Start insert_stations function')
        for station_info_to_insert in stations_info:
            name = station_info_to_insert[0]
            station_code = station_info_to_insert[1]
            longitude = station_info_to_insert[2]
            latitude = station_info_to_insert[3]
            city_id = station_info_to_insert[4]
            station_type_id = station_info_to_insert[5]
            transport_type_id = station_info_to_insert[6]
            self.db_functions.insert_station_info(name, station_code, longitude, latitude,
                                                  city_id, station_type_id, transport_type_id)
        logger.info('Function insert_stations: done')

    @staticmethod
    def get_city_and_station_info(city, value_dict: dict) -> List[dict]:
        logger.info('Start get_city_and_station_info function')
        full_info = []
        city_code = {k: v['city_code'] for k, v in value_dict.items() if k == 'city_code'}
        stations_info = [i for key, value in value_dict.items() for i in value if key != 'city_code'
                         and key != '']
        for item in stations_info:
            full_info_for_city_and_station = {'city': city}
            full_info_for_city_and_station.update(city_code)
            full_info_for_city_and_station.update(item)
            full_info.append(full_info_for_city_and_station)
        logger.info('Function get_city_and_station_info: done')
        return full_info

    @staticmethod
    def get_stations_types_and_transport_types(info_to_parse):
        logger.info('Start get_stations_types_and_transport_types function')
        station_types = []
        transport_types = []
        for item in info_to_parse.values():
            for s in item.get('stations'):
                if s['station_type'] is not None and s['station_type'] not in station_types:
                    station_types.append(s['station_type'])
                if s['transport_type'] is not None and s['transport_type'] not in transport_types:
                    transport_types.append(s['transport_type'])
        logger.info('Function get_stations_types_and_transport_types: done')
        return station_types, transport_types

    def insert_cities(self, info_to_parse: dict):
        logger.info('Start insert_cities function')
        for key, value in info_to_parse.items():
            city_name = None
            city_code = None
            if key is not None and key != '':
                city_name = key
                city_code = value['city_code']['city_code']
            if city_name:
                self.db_functions.insert_city_info(city_name, city_code)
        logger.info('Function insert_cities: done')

    def insert_transport_type(self, stations_and_transport: tuple):
        logger.info('Start insert_transport_type function')
        transport = stations_and_transport[1]

        for transport_type in transport:
            self.db_functions.insert_transport_type(transport_type)
        logger.info('Function insert_transport_type: done')

    def insert_station_type(self, stations_and_transport: tuple):
        logger.info('Start insert_station_type function')
        stations = stations_and_transport[0]

        for station_type in stations:
            self.db_functions.insert_station_type(station_type)
        logger.info('Function insert_station_type: done')

    @staticmethod
    def get_unique(info_to_insert: List[tuple]) -> List[tuple]:
        logger.info('Start get_unique function')
        unique_set = set(info_to_insert)
        unique_list = list(unique_set)
        logger.info('Function get_unique: done')
        return unique_list
