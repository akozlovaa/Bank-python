import doctest
from model.BankService import BankService
from model.ServiceTerm import ServiceTerm
from model.PlanName import PlanName


class BankServiceManager:

    def __init__(self, bank_service_list=None):
        if bank_service_list is None:
            self.bank_service_list = []
        else:
            self.bank_service_list = bank_service_list

    def __del__(self):
        return

    def find_bank_services_by_service_class(self, service_class_to_find: ServiceTerm):
        """
        >>> service1 = BankService('Monobank', 12, PlanName.SILVER, ServiceTerm.LONG_TERM, 1, 2, 0.5, 'expedited', 100)
        >>> service2 = BankService('BoA', 6, PlanName.GOLD, ServiceTerm.SHORT_TERM, 2, 1, 3, 'full', 450)
        >>> service3 = BankService('NBC', 9, PlanName.SILVER, ServiceTerm.HOME_EQUITY, 0.8, 0.7, 1.5, 'premium', 600)
        >>> services = [service1, service2, service3]
        >>> manager = BankServiceManager(services)
        >>> print(manager.find_bank_services_by_service_class(ServiceTerm.LONG_TERM))
        ['Monobank']
        >>> print(manager.find_bank_services_by_service_class(ServiceTerm.SHORT_TERM))
        ['BoA']
        >>> print(manager.find_bank_services_by_service_class(ServiceTerm.HOME_EQUITY))
        ['NBC']
        """
        result_services = []
        for service in self.bank_service_list:
            if service.service_term == service_class_to_find:
                result_services.append(service.bank_name)
            else:
                pass
        return result_services


if __name__ == "__main__":
    doctest.testmod(verbose=True)
