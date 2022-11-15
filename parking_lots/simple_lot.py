from lot.parking_lot import ParkingLot
from helpers.enums import ParkingLotType
from parking_rates.parking_fee import MallParkingRates


class SimpleLot(ParkingLot):  # {
    def __init__(
            self,
            name='SimpleParkingLot'
    ):  # {
        self.name = name
        super().__init__(ParkingLotType.SIMPLE.value)
    # }

    def park(self, vehicle):  # {
        ticket = super(SimpleLot, self).park(vehicle=vehicle)
        if ticket:  # {
            return ticket
        # }
        else:  # {
            return "No Space available"
        # }
    # }

    def unpark(self, vehicle):  # {
        receipt = super(SimpleLot, self).unpark(vehicle).get_receipt()
        total_fee = MallParkingRates(receipt).get_fee(vehicle.get_type())
        receipt.set_fee(total_fee)
        return receipt
    # }
# }
