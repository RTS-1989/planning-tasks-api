import time
import logging

from planning_tasks_api.settings import YANDEX_SCHEDULE_TOKEN, YANDEX_RASP_URL, LOGGER_LEVEL

from db_functions import DbFunctions
from insert_to_db import YandexScheduleInfoInsertToDatabase


def start_parse(token: str, url: str, db_functions: DbFunctions):
    logging.basicConfig(level=LOGGER_LEVEL, format='[%(asctime)s: %(name)s: %(levelname)s] %(message)s')
    logger = logging.getLogger('Main')
    logger.setLevel(logging.INFO)
    logging.basicConfig(level=logging.INFO)
    logger.info('Yandex schedule parse info app starts')
    yandex_schedule = YandexScheduleInfoInsertToDatabase(token, url,
                                                         db_functions)
    raw_info_to_parse = yandex_schedule.get_raw_info_to_parse()
    parsed_info_dict = YandexScheduleInfoInsertToDatabase.get_info_to_parse(raw_info_to_parse=raw_info_to_parse)
    station_types, transport_types = yandex_schedule.get_stations_types_and_transport_types(parsed_info_dict)
    countries, regions = yandex_schedule.get_country_and_region_info(raw_info_to_parse)
    yandex_schedule.insert_regions(regions=regions)
    yandex_schedule.insert_countries(countries=countries)
    yandex_schedule.insert_cities(parsed_info_dict)
    yandex_schedule.insert_transport_type(transport_types)
    yandex_schedule.insert_station_type(station_types)
    time.sleep(2)
    yandex_schedule.station_info_to_write(parsed_info_dict)
    logger.info('Yandex schedule parse info app done')


if __name__ == '__main__':
    start_parse(YANDEX_SCHEDULE_TOKEN, YANDEX_RASP_URL, DbFunctions())
