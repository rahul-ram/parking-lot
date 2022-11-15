from abc import ABC
from enum import Enum
from helpers.enums import VehicleType


class Vehicle(ABC):
    def __init__(
            self,
            vehicle_type: Enum,
            identifier,
            ticket=None,
            receipt=None,
    ):  # {
        self.__type = vehicle_type
        self.__identifier = identifier
        self.__ticket = ticket
        self.__receipt = receipt
        self.__spot_number = None
    # }

    def assign_ticket(self, ticket):  # {
        self.__ticket = ticket
    # }

    def get_ticket(self):  # {
        return self.__ticket
    # }

    def assign_receipt(self, receipt):  # {
        self.__receipt = receipt
    # }

    def get_receipt(self):  # {
        return self.__receipt
    # }

    def get_type(self):  # {
        return self.__type
    # }

    def assign_spot_number(self, spot):  # {
        self.__spot_number = spot.get_number()
    # }

    def get_spot_number(self):  # {
        return self.__spot_number
    # }


class Scooter(Vehicle):  # {
    def __init__(
            self,
            identifier
    ):  # {
        super().__init__(VehicleType.SCOOTER, identifier)
    # }
# }


class Motorcycle(Vehicle):  # {
    def __init__(
            self,
            identifier
    ):  # {
        super().__init__(VehicleType.MOTORCYCLE, identifier)
    # }
# }


class Car(Vehicle):  # {
    def __init__(
            self,
            identifier
    ):  # {
        super().__init__(VehicleType.CAR, identifier)
    # }
# }


class Suv(Vehicle):  # {
    def __init__(
            self,
            identifier
    ):  # {
        super().__init__(VehicleType.SUV, identifier)
    # }
# }


class Bus(Vehicle):  # {
    def __init__(
            self,
            identifier
    ):  # {
        super().__init__(VehicleType.BUS, identifier)
    # }
# }


class Truck(Vehicle):  # {
    def __init__(
            self,
            identifier
    ):  # {
        super().__init__(VehicleType.TRUCK, identifier)
    # }
# }
