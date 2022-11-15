from lot.parking_lot import ParkingLot
from helpers.enums import ParkingLotType
from vehicle.vehicle import Motorcycle
from tickets.tickets_receipts import ParkingReceipt
from parking_rates.parking_fee import StadiumParkingRates


class Stadium(ParkingLot):  # {
    def __init__(
            self,
            name='StadiumParkingLot'
    ):  # {
        self.name = name
        super().__init__(ParkingLotType.STADIUM.value)
    # }

    def park(self, vehicle):  # {
        ticket = super(Stadium, self).park(vehicle)
        if ticket:  # {
            return ticket
        # }
        else:  # {
            return "No Space available"
        # }
    # }

    def unpark(self, vehicle) -> ParkingReceipt:  # {
        receipt = super(Stadium, self).unpark(vehicle).get_receipt()
        total_fee = StadiumParkingRates(receipt).get_fee(vehicle.get_type())
        receipt.set_fee(total_fee)
        return receipt
    # }
# }

