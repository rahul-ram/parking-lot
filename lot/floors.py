from helpers.enums import ParkingSpotType
from lot.spots import LargeSpot, CompactSpot, MotorBikeSpot
from helpers.enums import VehicleType
from lot.spots import ParkingSpot


class ParkingFloor:  # {
    def __init__(
            self,
            number,
            small_spots,
            compact_spots,
            large_spots,
            name=None):  # {
        self.__number = number
        self.__name = name
        self.__max_motorbike_spots: int = small_spots
        self.__max_compact_spots: int = compact_spots
        self.__max_large_spots: int = large_spots

        self.__compact_spots = {}
        self.__large_spots = {}
        self.__motorbike_spots = {}

        self.__occupied_motorbike_spots = 0
        self.__occupied_compact_spots = 0
        self.__occupied_large_spots = 0

        if self.__max_motorbike_spots > 0:  # {
            for slot_num in range(1, self.__max_motorbike_spots + 1):  # {
                self.add_parking_spot(MotorBikeSpot(slot_num))
            # }

        if self.__max_compact_spots > 0:  # {
            end_range = self.__max_motorbike_spots + self.__max_compact_spots
            for slot_num in range(self.__max_motorbike_spots + 1, end_range + 1):  # {
                self.add_parking_spot(CompactSpot(slot_num))
            # }

        if self.__max_large_spots > 0:  # {
            start_slot_num = self.__max_motorbike_spots + self.__max_compact_spots
            last_slot_num = self.__max_motorbike_spots + self.__max_compact_spots + self.__max_large_spots
            for slot_num in range(start_slot_num + 1, last_slot_num + 1):  # {
                self.add_parking_spot(LargeSpot(slot_num))
            # }
    # }

    def add_parking_spot(self, spot: ParkingSpot):  # {
        if spot.get_type() == ParkingSpotType.MOTORBIKE:  # {
            self.__motorbike_spots[spot.get_number()] = spot,
        # }
        elif spot.get_type() == ParkingSpotType.COMPACT:  # {
            self.__compact_spots[spot.get_number()] = spot,
        # }
        elif spot.get_type() == ParkingSpotType.LARGE:  # {
            self.__large_spots[spot.get_number()] = spot,
        # }
    # }

    def park_vehicle(self, vehicle):  # {
        """
        get next available spot and park vehicle based on type
        """
        if vehicle.get_type() == VehicleType.SCOOTER or vehicle.get_type() == VehicleType.MOTORCYCLE:  # {
            for key in self.__motorbike_spots.keys():  # {
                if self.__motorbike_spots.get(key)[0].is_free():  # {
                    spot = self.__motorbike_spots.get(key)[0]
                    spot.assign_vehicle(vehicle)
                    self.__occupied_motorbike_spots += 1
                    vehicle.assign_spot_number(spot)
                    return True
                # }
            # }
            return False
        # }
        if vehicle.get_type() == VehicleType.CAR or vehicle.get_type() == VehicleType.SUV:  # {
            for key in self.__compact_spots.keys():  # {
                if self.__compact_spots.get(key)[0].is_free():  # {
                    spot = self.__compact_spots.get(key)[0]
                    spot.assign_vehicle(vehicle)
                    self.__occupied_compact_spots += 1
                    vehicle.assign_spot_number(spot)
                    return True
                # }
            # }
            return False
        # }
        if vehicle.get_type() == VehicleType.BUS or vehicle.get_type() == VehicleType.TRUCK:  # {
            for key in self.__large_spots.keys():  # {
                if self.__large_spots.get(key)[0].is_free():  # {
                    spot = self.__large_spots.get(key)[0]
                    spot.assign_vehicle(vehicle)
                    self.__occupied_large_spots += 1
                    vehicle.assign_spot_number(spot)
                    return True
                # }
            # }
            return False
        # }
    # }

    def unpark_vehicle(self, vehicle):  # {
        """
        Remove vehicle from a parking spot
        """
        if vehicle.get_type() == VehicleType.SCOOTER or vehicle.get_type() == VehicleType.MOTORCYCLE:  # {
            spot = self.__motorbike_spots.get(vehicle.get_spot_number())[0]
            spot.remove_vehicle()
            self.__occupied_motorbike_spots -= 1
            return True
        # }
        elif vehicle.get_type() == VehicleType.CAR or vehicle.get_type() == VehicleType.SUV:  # {
            spot = self.__compact_spots.get(vehicle.get_spot_number())[0]
            spot.remove_vehicle()
            self.__occupied_compact_spots -= 1
            return True
        # }
        elif vehicle.get_type() == VehicleType.BUS or vehicle.get_type() == VehicleType.TRUCK:  # {
            spot = self.__large_spots.get(vehicle.get_spot_number())[0]
            spot.remove_vehicle()
            self.__occupied_large_spots -= 1
            return True
        # }
    # }

    def is_full(self, vehicle_type):  # {
        """
        Check if there is a spot for vehicle of some type
        :param vehicle_type:  One of SCOOTER/MOTORCYCLE/BUS/TRUCK/CAR/SUV
        :return: None
        """
        # MotorCycles and Scooters can only be parked at small/motorbike spots
        if vehicle_type == VehicleType.MOTORCYCLE or vehicle_type == VehicleType.SCOOTER:  # {
            return self.__occupied_motorbike_spots >= self.__max_motorbike_spots
        # }

        # Cars and SUVs can only be parked at compact spots
        if vehicle_type == VehicleType.CAR or vehicle_type == VehicleType.SUV:  # {
            return self.__occupied_compact_spots >= self.__max_compact_spots
        # }

        # Buses and Trucks can only be parked at large spots
        if vehicle_type == VehicleType.BUS or vehicle_type == VehicleType.TRUCK:  # {
            return self.__occupied_large_spots >= self.__max_large_spots
        # }
    # }
# }
