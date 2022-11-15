from lot.parking_lot import ParkingLot
from helpers.enums import ParkingLotType
from tickets.tickets_receipts import ParkingReceipt
from parking_rates.parking_fee import MallParkingRates


class MallParkingLot(ParkingLot):  # {
    def __init__(
            self,
            name='mallParkingLot'
    ):  # {
        self.name = name
        super().__init__(ParkingLotType.MALL.value)
    # }

    def park(self, vehicle):  # {
        ticket = super(MallParkingLot, self).park(vehicle)
        if ticket:  # {
            return ticket
        # }
        else:  # {
            return "No Space available"
        # }
    # }

    def unpark(self, vehicle) -> ParkingReceipt:  # {
        receipt = super(MallParkingLot, self).unpark(vehicle).get_receipt()
        total_fee = MallParkingRates(receipt).get_fee(vehicle.get_type())
        receipt.set_fee(total_fee)
        return receipt
    # }
# }

