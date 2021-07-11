from typing import List
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class YandexScheduleInfoHandler:

    @staticmethod
    def get_all_info(regions_info: list):
        logger.info('Start get_all_info function')
        countries_info_list = []
        settlements_info = {}
        settlements_list = [s for s in regions_info]
        for settlements_by_region in settlements_list:
            settlements_in_region = [s for s in settlements_by_region.values()][0]
            all_settlements_info = YandexScheduleInfoHandler.get_all_settlements_info(settlements_in_region)
            settlements_info.update(all_settlements_info)
        countries_info_list.append(settlements_info)
        logger.info('Function get_all_info: done')
        return countries_info_list

    @staticmethod
    def get_all_settlements_info(settlements_by_region_list: List[dict]):
        logger.info('Start get_all_settlement_info function')
        country_base_info = {}
        for settlement_by_region in settlements_by_region_list:
            settlements_list = settlement_by_region.get('settlements')
            countries_info = YandexScheduleInfoHandler.get_settlement_info(settlements_list)
            country_base_info.update(countries_info)
        logger.info('Function get_all_settlement_info: done')
        return country_base_info

    @staticmethod
    def get_settlement_info(settlements_list: List[dict]):
        logger.info('Start get_settlement_info function')
        countries_dict = {}
        for settlement in settlements_list:
            yandex_code = settlement["codes"]["yandex_code"] \
                if settlement["codes"].get("yandex_code") else ''
            if settlement.get('title') is not None:
                settlement_name = settlement.get('title', '')
                countries_dict[settlement_name] = {}
                countries_dict[settlement_name]['city_code'] = {
                    'city_code': yandex_code if settlement["codes"] != {} else 'Нет информации'
                }
                stations = YandexScheduleInfoHandler.get_stations_info(settlement)
                countries_dict[settlement_name]['stations'] = stations
        logger.info('Function get_settlement_info: done')
        return countries_dict

    @staticmethod
    def get_stations_info(settlement: dict):
        logger.info('Start get_stations_info function')
        stations_list = []
        stations_by_settlement_list = settlement.get('stations')
        for s in stations_by_settlement_list:
            stations = {"station_code": s["codes"]["yandex_code"] if s else {},
                        "station_type": s["station_type"] if s["station_type"] else "",
                        "station_name": s["title"] if s["title"] else "", "transport_type": s["transport_type"],
                        "longitude": s["longitude"] if s["longitude"] else "",
                        "latitude": s["latitude"] if s["latitude"] else ""}
            stations_list.append(stations)
        logger.info('Function get_stations_info: done')
        return stations_list
