from lot.parking_lot import ParkingLot
from helpers.enums import ParkingLotType
from tickets.tickets_receipts import ParkingReceipt
from parking_rates.parking_fee import AirPortParkingRates


class AirportLot(ParkingLot):  # {
    def __init__(
            self,
            name='AirportParkingLot'
    ):  # {
        self.name = name
        super().__init__(ParkingLotType.AIRPORT.value)
    # }

    def park(self, vehicle):  # {
        ticket = super(AirportLot, self).park(vehicle)
        if ticket:  # {
            return ticket
        # }
        else:  # {
            return "No Space available"
        # }
    # }

    def unpark(self, vehicle) -> ParkingReceipt:  # {
        receipt = super(AirportLot, self).unpark(vehicle).get_receipt()
        total_fee = AirPortParkingRates(receipt).get_fee(vehicle.get_type())
        receipt.set_fee(total_fee)
        return receipt
    # }
# }
