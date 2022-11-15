from abc import ABC
from helpers.enums import ParkingSpotType


class ParkingSpot(ABC):  # {
    __slots__ = ["__number"]

    def __init__(
            self,
            number,
            parking_spot_type
    ):  # {
        self.__number = number
        self.__spot_type = parking_spot_type
        self.__free = True
        self.__vehicle = None

    # }

    def is_free(self):  # {
        return self.__free
    # }

    def assign_vehicle(self, vehicle):  # {
        self.__vehicle = vehicle
        self.__free = False
    # }

    def remove_vehicle(self):  # {
        self.__vehicle = None
        self.__free = True
    # }

    def get_number(self):  # {
        return self.__number
    # }

    def get_type(self):  # {
        return self.__spot_type
    # }


class MotorBikeSpot(ParkingSpot):  # {
    def __init__(
            self,
            number
    ):  # {
        super().__init__(number, ParkingSpotType.MOTORBIKE)
    # }
# }


class CompactSpot(ParkingSpot):  # {
    def __init__(
            self,
            number
    ):  # {
        super().__init__(number, ParkingSpotType.COMPACT)
    # }
# }


class LargeSpot(ParkingSpot):  # {
    def __init__(
            self,
            number
    ):  # {
        super().__init__(number, ParkingSpotType.LARGE)
    # }
# }



