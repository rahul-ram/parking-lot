
from abc import ABC
from tickets.tickets_receipts import ParkingTicket, ParkingReceipt
from config import Config
from lot.floors import ParkingFloor


class ParkingLot(ABC):   # {
    #  __slots__ = 'lot_type'

    def __init__(
            self,
            lot_type
    ):  # {
        self.__lot_type = lot_type
        self.__conf = Config.config(key=self.__lot_type)

        self.__max_motorbike_count = int(self.__conf.get('small_spots'))
        self.__max_compact_count = int(self.__conf.get('compact_spots'))
        self.__max_large_count = int(self.__conf.get('large_spots'))
        self.__no_of_floors = int(self.__conf.get('floors'))

        self.__parking_floors = {}
        self.__active_tickets = {}

        for i in range(1, self.__no_of_floors + 1):  # {
            self.__parking_floors[i] = ParkingFloor(number=i,
                                                    small_spots=self.__max_motorbike_count,
                                                    compact_spots=self.__max_compact_count,
                                                    large_spots=self.__max_large_count
                                                    )
        # }
    # }

    def is_lot_full(self, vehicle_type):  # {
        for key in self.__parking_floors:  # {
            if not self.__parking_floors.get(key).is_full(vehicle_type):  # {
                return False
            # }
        # }
        return True
    # }

    def __park_vehicle_in_level(self, vehicle):  # {
        """
        park the vehicle in dedicated spot in a parking floor
        """
        for level in self.__parking_floors:  # {
            if self.__parking_floors.get(level).park_vehicle(vehicle):  # {
                return True
            # }
        return False
        # }
    # }

    def __remove_vehicle_from_level(self, vehicle):  # {
        """
        unpark the vehicle in dedicated spot in a parking floor
        """
        for level in self.__parking_floors:  # {
            if self.__parking_floors.get(level).unpark_vehicle(vehicle):  # {
                return True
            # }
        return False
        # }
    # }

    def park(self, vehicle):  # {
        if self.is_lot_full(vehicle.get_type()):  # {
            return False
        # }
        elif not self.__park_vehicle_in_level(vehicle):  # {
            return False
        # }

        ticket = ParkingTicket()
        ticket.generate_ticket(vehicle=vehicle)

        vehicle.assign_ticket(ticket)

        self.__active_tickets[ticket.get_ticket_number()] = ticket
        return ticket
    # }

    def unpark(self, vehicle):  # {
        if self.__remove_vehicle_from_level(vehicle):
            receipt = ParkingReceipt()
            if not vehicle.get_ticket().get_exit_time():
                vehicle.get_ticket().close_ticket()
            receipt.generate_receipt(vehicle.get_ticket())
            vehicle.assign_receipt(receipt)
            return vehicle
        else:
            return f"No vehicle found at spot {vehicle.get_spot_number()}"
    # }
# }
