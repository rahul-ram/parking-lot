from enum import Enum


#  Vehicle Types
class VehicleType(Enum):
    MOTORCYCLE = 1
    SCOOTER = 2
    CAR = 3
    SUV = 4
    BUS = 5
    TRUCK = 6


class ParkingSpotType(Enum):
    MOTORBIKE = 1
    COMPACT = 2
    LARGE = 3


class ParkingTicketStatus(Enum):
    ACTIVE = 1
    PAID = 2


class ParkingLotType(Enum):
    SIMPLE = "SIMPLE"
    STADIUM = "STADIUM"
    MALL = "MALL"
    AIRPORT = "AIRPORT"
