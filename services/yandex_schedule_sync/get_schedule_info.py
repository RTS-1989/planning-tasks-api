from typing import List
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class YandexScheduleInfoHandler:

    @staticmethod
    def get_all_info(regions_info: list) -> List:
        logger.info('Function get_all_info: start')
        countries_info_list = []
        settlements_info = {}
        settlements_list = [s for s in regions_info]
        for settlements_by_region in settlements_list:
            country_info = {}
            if settlements_by_region.get('codes'):
                country_info = YandexScheduleInfoHandler.get_country_info(settlements_by_region)
            settlements_in_region = [s for s in settlements_by_region.values()][0]
            settlements_in_region = YandexScheduleInfoHandler.update_settlements_in_region(
                settlements_in_region, country_info)
            all_settlements_info = YandexScheduleInfoHandler\
                .get_all_settlements_info(settlements_in_region, country_info)
            settlements_info.update(all_settlements_info)
        countries_info_list.append(settlements_info)
        logger.info('Function get_all_info: done')
        return countries_info_list

    @staticmethod
    def get_all_settlements_info(settlements_by_region_list: List[dict], country_info: dict) -> dict:
        logger.info('Function get_all_settlements_info: start')
        country_base_info = {}
        for settlement_by_region in settlements_by_region_list:
            countries_info = YandexScheduleInfoHandler.get_settlement_info(settlement_by_region, country_info)
            country_base_info.update(countries_info)
        logger.info('Function get_all_settlement_info: done')
        return country_base_info

    @staticmethod
    def get_settlement_info(settlement_by_region: dict, country_info: dict) -> dict:
        logger.info('Function get_settlement_info: start')
        settlements_list = settlement_by_region.get('settlements')
        region_info = YandexScheduleInfoHandler.get_regions_info(settlement_by_region)
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
                if region_info:
                    countries_dict[settlement_name].update(region_info)
                countries_dict[settlement_name].update(country_info)
        logger.info('Function get_settlement_info: done')
        return countries_dict

    @staticmethod
    def get_country_info(settlements_by_region: dict) -> dict:
        logger.info('Function get_country_info: start')
        if settlements_by_region.get('codes'):
            country_code_dict = settlements_by_region.get("codes")
            logger.info('Function get_country_info: done')
            return {
                'country_code': country_code_dict.get("yandex_code"),
                'country_name': settlements_by_region.get("title")
            }
        logger.info('Function get_country_info: done')
        return {}

    @staticmethod
    def get_stations_info(settlement: dict):
        logger.info('Function get_stations_info: start')
        stations_list = []
        stations_by_settlement_list = settlement.get('stations')
        for s in stations_by_settlement_list:
            stations = {}
            stations["station_code"] = s["codes"]["yandex_code"] if s else {}
            stations["station_type"] = s["station_type"] if s["station_type"] else ""
            stations["station_name"] = s["title"] if s["title"] else ""
            stations["transport_type"] = s["transport_type"]
            stations["longitude"] = s["longitude"] if s["longitude"] else ""
            stations["latitude"] = s["latitude"] if s["latitude"] else ""
            stations_list.append(stations)
        logger.info('Function get_stations_info: done')
        return stations_list

    @staticmethod
    def get_regions_info(settlements_by_region: dict) -> dict:
        logger.info('Function get_regions_info: start')
        if settlements_by_region.get('codes'):
            region_code_dict = settlements_by_region.get("codes")
            logger.info('Function get_regions_info: done')
            return {
                'region_code': region_code_dict.get("yandex_code"),
                'region_name': settlements_by_region.get("title")
            }

    @staticmethod
    def update_settlements_in_region(settlements: List[dict], update_info: dict) -> list:
        logger.info('Function update_settlements_in_region: start')
        new_settlements: list = []
        for s in settlements:
            s.update(update_info)
            new_settlements.append(s)
        logger.info('Function update_settlements_in_region: done')
        return new_settlements
