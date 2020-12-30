import doctest
from model.BankService import BankService
from model.ServiceTerm import ServiceTerm
from model.PlanName import PlanName
from model.SortType import SortType


class BankServiceManagerUtils:

    def __init__(self, bank_service_list=None):
        if bank_service_list is None:
            self.bank_service_list = []
        else:
            self.bank_service_list = bank_service_list

    def __del__(self):
        return

    def sort_bank_services_by_discount_rate(self, type_of_sort: str):
        """
        >>> service1 = BankService('Monobank', 12, PlanName.SILVER, ServiceTerm.LONG_TERM, 1, 2, 0.5, 'expedited', 100)
        >>> service2 = BankService('BoA', 6, PlanName.GOLD, ServiceTerm.SHORT_TERM, 2, 1, 3, 'full', 450)
        >>> service3 = BankService('NBC', 9, PlanName.SILVER, ServiceTerm.HOME_EQUITY, 0.8, 0.7, 1.5, 'premium', 600)
        >>> service4 = BankService('JPMorgan', 5, PlanName.SILVER, ServiceTerm.LONG_TERM, 0.4, 0.2, 0.6, 'full', 200)
        >>> service5 = BankService('Privatbank', 7, PlanName.GOLD, ServiceTerm.SHORT_TERM, 0.5, 0.5, 1, 'vip', 520)
        >>> services = [service1, service2, service3, service4, service5]
        >>> manager_utils = BankServiceManagerUtils(services)
        >>> sorted_services = manager_utils.sort_bank_services_by_discount_rate(SortType.ASCENDING.value)
        >>> for service in sorted_services: print(service.bank_name)
        Monobank
        JPMorgan
        Privatbank
        NBC
        BoA
        >>> sorted_services = manager_utils.sort_bank_services_by_discount_rate(SortType.DESCENDING.value)
        >>> for service_1 in sorted_services: print(service_1.bank_name)
        BoA
        NBC
        Privatbank
        JPMorgan
        Monobank
        """
        sorted_services = sorted(self.bank_service_list, key=lambda service: service.discount_rate_in_percents)
        if type_of_sort == SortType.ASCENDING.value:
            return sorted_services
        elif type_of_sort == SortType.DESCENDING.value:
            return sorted_services[::-1]
        else:
            return sorted_services

    def sort_bank_services_by_interest_rate_in_percents(self, type_of_sort: str):
        """
        >>> service1 = BankService('Monobank', 12, PlanName.SILVER, ServiceTerm.LONG_TERM, 1, 2, 0.5, 'expedited', 100)
        >>> service2 = BankService('BoA', 6, PlanName.GOLD, ServiceTerm.SHORT_TERM, 2, 1, 3, 'full', 450)
        >>> service3 = BankService('NBC', 9, PlanName.SILVER, ServiceTerm.HOME_EQUITY, 0.8, 0.7, 1.5, 'premium', 600)
        >>> service4 = BankService('JPMorgan', 5, PlanName.SILVER, ServiceTerm.LONG_TERM, 0.4, 0.2, 0.6, 'full', 200)
        >>> service5 = BankService('Privatbank', 7, PlanName.GOLD, ServiceTerm.SHORT_TERM, 0.5, 0.5, 1, 'vip', 520)
        >>> services = [service1, service2, service3, service4, service5]
        >>> manager_utils = BankServiceManagerUtils(services)
        >>> sorted_services = manager_utils.sort_bank_services_by_interest_rate_in_percents(SortType.ASCENDING.value)
        >>> for service in sorted_services: print(service.bank_name)
        JPMorgan
        Privatbank
        NBC
        Monobank
        BoA
        >>> sorted_services = manager_utils.sort_bank_services_by_interest_rate_in_percents(SortType.DESCENDING.value)
        >>> for service_1 in sorted_services: print(service_1.bank_name)
        BoA
        Monobank
        NBC
        Privatbank
        JPMorgan
        """
        sorted_services = sorted(self.bank_service_list, key=lambda service: service.interest_rate_in_percents)
        if type_of_sort == SortType.ASCENDING.value:
            return sorted_services
        elif type_of_sort == SortType.DESCENDING.value:
            return sorted_services[::-1]


if __name__ == "__main__":
    doctest.testmod(verbose=True)
