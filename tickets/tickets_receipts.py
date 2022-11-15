import itertools
from abc import ABC
from datetime import datetime

from vehicle.vehicle import Vehicle


class Ticket(ABC):  # {
    ...
# }


class ParkingTicket(Ticket):  # {
    number_iter = itertools.count(start=1)

    def __init__(
            self
    ):  # {
        self.__number = "00" + str(next(self.number_iter))
        self.__spot_number = None
        self.__parkingLot = None
        self.__entry_time = None
        self.__exit_time = None
    # }

    def get_entry_time(self):  # {
        return self.__entry_time
    # }

    def get_exit_time(self):  # {
        return self.__exit_time
    # }

    def get_ticket_number(self):  # {
        return self.__number
    # }

    def generate_ticket(self, vehicle: Vehicle) -> Ticket:  # {
        self.__spot_number = vehicle.get_spot_number()
        self.__entry_time = datetime.utcnow().strftime("%d-%b-%Y %H:%M:%S")
        return self
    # }

    def close_ticket(self) -> None:  # {
        self.__exit_time = datetime.utcnow().strftime("%d-%b-%Y %H:%M:%S")
    # }

    def __str__(self) -> str:  # {
        return f"Parking Ticket: \n" \
               f"  Ticket Number: {self.__number}\n" \
               f"  Spot Number: {self.__spot_number} \n" \
               f"  Entry Date-time: {self.__entry_time}"
    # }

    def set_exit_time(self, time):  # {
        """
        For testing only
        """
        self.__exit_time = time
    # }
# }


class Receipt(ABC):  # {
    ...
# }


class ParkingReceipt(Receipt):  # {
    number_iter = itertools.count(start=1)

    def __init__(
            self
    ):  # {
        self.__number = "R-00" + str(next(self.number_iter))
        self.__entry_time = None
        self.__exit_time = None
        self.__fee = 0
    # }

    def get_entry_time(self):  # {
        return self.__entry_time
    # }

    def get_exit_time(self):  # {
        return self.__exit_time
    # }

    def get_receipt_number(self):  # {
        return self.__number
    # }

    def set_fee(self, fee):  # {
        self.__fee = fee
    # }

    def generate_receipt(self, ticket: ParkingTicket) -> Receipt:  # {
        self.__entry_time = ticket.get_entry_time()
        self.__exit_time = ticket.get_exit_time()
        return self
    # }

    def __str__(self) -> str:  # {
        return f"Parking Receipt: \n" \
               f"  Receipt Number: {self.__number}\n" \
               f"  Entry Date-time: {self.__entry_time}\n" \
               f"  Exit Date-time: {self.__exit_time}\n" \
               f"  Fees: {self.__fee}"
    # }
