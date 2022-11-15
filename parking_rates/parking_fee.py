from abc import ABC
from datetime import datetime
import math

from tickets.tickets_receipts import ParkingReceipt
from helpers.enums import VehicleType


class ParkingRate(ABC):  # {
    def __init__(
            self,
            receipt: ParkingReceipt
    ):  # {
        self.__receipt = receipt
    # }

    def get_total_time(self):  # {
        start = datetime.strptime(self.__receipt.get_entry_time(), "%d-%b-%Y %H:%M:%S")
        end = datetime.strptime(self.__receipt.get_exit_time(), "%d-%b-%Y %H:%M:%S")
        delta = end - start
        if delta.total_seconds() < 60 * 60:  # {
            return 1
        # }
        else:  # {
            return int(math.ceil(float(delta.total_seconds()) / float(60 * 60)))
        # }
    # }

    @staticmethod
    def total_fee(hours, rate_per_hour):  # {
        return hours * rate_per_hour
    # }

# }


class MallParkingRates(ParkingRate):  # {
    """
    Get Parking fee for Simple parking lots or Mall parking lot
    """

    def __init__(self, receipt: ParkingReceipt):  # {
        self.__receipt = receipt
        self.__motorcycle_hourly_fee = 10
        self.__car_hourly_fee = 20
        self.__bus_hourly_fee = 50
        super().__init__(receipt)
    # }

    def get_fee(self, vehicle_type):  # {
        if vehicle_type == VehicleType.MOTORCYCLE or vehicle_type == VehicleType.SCOOTER:  # {
            return self.total_fee(self.get_total_time(), self.__motorcycle_hourly_fee)
        # }
        if vehicle_type == VehicleType.CAR or vehicle_type == VehicleType.SUV:  # {
            return self.total_fee(self.get_total_time(), self.__car_hourly_fee)
        # }
        if vehicle_type == VehicleType.BUS or vehicle_type == VehicleType.TRUCK:  # {
            return self.total_fee(self.get_total_time(), self.__bus_hourly_fee)
        # }
    # }
# }


class StadiumParkingRates(ParkingRate):  # {
    """
    Get Parking fee for Stadium parking lot
    """

    def __init__(self, receipt: ParkingReceipt):  # {
        self.__receipt = receipt
        self.__motorcycle_hourly_fee = 100
        self.__car_hourly_fee = 200
        self.__motorcycle_flat_4 = 30
        self.__motorcycle_flat_4_12 = 60
        self.__car_flat_4 = 60
        self.__car_flat_4_12 = 120
        super().__init__(receipt)
    # }

    def get_fee(self, vehicle_type):  # {
        total_time = self.get_total_time()
        fee = 0
        if vehicle_type == VehicleType.MOTORCYCLE or vehicle_type == VehicleType.SCOOTER:  # {
            if total_time <= 4:
                fee += self.__motorcycle_flat_4
            elif 4 < total_time <= 12:
                fee += (self.__motorcycle_flat_4 + self.__motorcycle_flat_4_12)
            elif total_time > 12:
                hourly_rate = self.total_fee(total_time - 12, self.__motorcycle_hourly_fee)
                fee += (self.__motorcycle_flat_4 + self.__motorcycle_flat_4_12 + hourly_rate)
        # }
        if vehicle_type == VehicleType.CAR or vehicle_type == VehicleType.SUV:  # {
            if total_time <= 4:
                fee += self.__car_flat_4
            elif 4 < total_time <= 12:
                fee += (self.__car_flat_4 + self.__car_flat_4_12)
            elif total_time > 12:
                hourly_rate = self.total_fee(total_time - 12, self.__car_hourly_fee)
                fee += (self.__car_flat_4 + self.__car_flat_4_12 + hourly_rate)
        # }
        return fee
    # }
# }


class AirPortParkingRates(ParkingRate):  # {
    """
    Get Parking fee for AirPort parking lot
    """

    def __init__(self, receipt: ParkingReceipt):  # {
        self.__receipt = receipt

        self.__motorcycle_daily_fee = 80
        self.__car_daily_fee = 100

        self.__motorcycle_flat_1 = 0
        self.__motorcycle_flat_1_8 = 40
        self.__motorcycle_flat_8_24 = 60

        self.__car_flat_0_12 = 60
        self.__car_flat_12_24 = 80

        super().__init__(receipt)
    # }

    def get_fee(self, vehicle_type):  # {
        total_time = self.get_total_time()
        fee = 0
        if vehicle_type == VehicleType.MOTORCYCLE or vehicle_type == VehicleType.SCOOTER:  # {
            if total_time <= 1:
                fee = self.__motorcycle_flat_1
            elif 1 < total_time <= 8:
                fee += self.__motorcycle_flat_1_8
            elif 8 < total_time <= 24:
                fee += self.__motorcycle_flat_8_24
            elif total_time > 24:
                no_of_days = math.ceil(float(total_time - 24) / 24)
                if no_of_days < 1:
                    no_of_days = 1
                daily_flat_rate = self.total_fee(no_of_days, self.__motorcycle_daily_fee)
                fee += (self.__motorcycle_flat_8_24 + daily_flat_rate)
        # }
        if vehicle_type == VehicleType.CAR or vehicle_type == VehicleType.SUV:  # {
            if total_time <= 12:
                fee += self.__car_flat_0_12
            elif 12 < total_time <= 24:
                fee += (self.__car_flat_0_12 + self.__car_flat_12_24)
            elif total_time > 24:
                no_of_days = int(math.ceil(float(total_time - 24) / 24))
                daily_flat_rate = self.total_fee(no_of_days, self.__car_daily_fee)
                fee += (self.__car_flat_0_12 + self.__car_flat_12_24 + daily_flat_rate)
        # }
        return fee
    # }
# }
