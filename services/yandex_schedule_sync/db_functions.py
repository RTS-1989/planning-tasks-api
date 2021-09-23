from typing import List

import psycopg2 as pg
from envparse import env

env.read_envfile()


class DbFunctions:

    def __init__(self):
        self.conn = pg.connect(
            database=env('POSTGRES_DB_NAME', ''),
            user=env('POSTGRES_DB_USER', ''),
            password=env('POSTGRES_DB_PASSWORD', ''),
            host=env('POSTGRES_DB_HOST', ''),
            port=env('POSTGRES_DB_PORT', ''),
        )

    def _execute(self, query, values: tuple):
        cursor = self.conn.cursor()
        cursor.execute(query, values)

    def select_one_record(self, query, values: tuple = None) -> tuple:
        cursor = self.conn.cursor()
        cursor.execute(query, values)
        return cursor.fetchone()

    def select_all_records(self, query, values: tuple = None) -> List[tuple]:
        cursor = self.conn.cursor()
        cursor.execute(query, values)
        return cursor.fetchall()

    def select_all_cities(self) -> List[tuple]:
        cities_query = """
                SELECT * FROM yandex_schedule_city;
                """
        return self.select_all_records(cities_query)

    def select_all_transport_types(self) -> List[tuple]:
        transport_types_query = """
                        SELECT * FROM yandex_schedule_transporttype;
                        """
        return self.select_all_records(transport_types_query)

    def select_all_station_types(self) -> List[tuple]:
        station_types_query = """
                    SELECT * FROM yandex_schedule_stationtype;
                    """
        return self.select_all_records(station_types_query)

    def select_all_countries(self) -> List[tuple]:
        countries_query = """
                    SELECT * FROM yandex_schedule_country;
        """
        return self.select_all_records(countries_query)

    def select_all_regions(self) -> List[tuple]:
        regions_query = """
                    SELECT * FROM yandex_schedule_region;
        """
        return self.select_all_records(regions_query)

    def insert_city_info(self, city_name, city_code, country_id, region_id):
        with self.conn:
            query = """
                INSERT INTO yandex_schedule_city(name, yandex_city_code, country_id, region_id)
                VALUES(%s, %s, %s, %s);"""
            self._execute(query, (city_name, city_code, country_id, region_id,))

    def insert_transport_type(self, transport_type):
        with self.conn:
            query = """
                INSERT INTO yandex_schedule_transporttype(transport_type)
                VALUES(%s);"""
            self._execute(query, (transport_type,))

    def insert_station_type(self, station_type):
        with self.conn:
            query = """
                INSERT INTO yandex_schedule_stationtype(station_type)
                VALUES(%s);"""
            self._execute(query, (station_type,))

    def insert_station_info(self, name, station_code, longitude, latitude, city_id,
                            station_type_id, transport_type_id):
        with self.conn:
            insert_query = """
                INSERT INTO yandex_schedule_station(name, station_code, longitude,
                latitude, city_id, station_type_id, transport_type_id)
                VALUES(%s, %s, %s, %s, %s, %s, %s);"""
            self._execute(insert_query, (name, station_code, longitude, latitude,
                                         city_id, station_type_id, transport_type_id))

    def insert_regions_info(self, name: str, yandex_region_code: str):
        with self.conn:
            insert_query = """
                INSERT INTO yandex_schedule_region(name, yandex_region_code) 
                VALUES(%s, %s);
            """
            self._execute(insert_query, (name, yandex_region_code))

    def insert_countries_info(self, name: str, yandex_country_code: str):
        with self.conn:
            insert_query = """
            INSERT INTO yandex_schedule_country(name, yandex_country_code)
            VALUES(%s, %s);
            """
            self._execute(insert_query, (name, yandex_country_code))
