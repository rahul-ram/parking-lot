import unittest
from datetime import datetime, timedelta

from parking_lots.simple_lot import SimpleLot
from parking_lots.airport_lot import AirportLot
from parking_lots.stadium import Stadium
from parking_lots.mall import MallParkingLot

from vehicle.vehicle import Vehicle, Car, Truck, Bus, Suv, Motorcycle, Scooter


class TestParkingLot(unittest.TestCase):

    def test_simple_lot(self):  # {
        p_lot = SimpleLot()

        vehicle1 = Motorcycle('12-ACA-122')
        vehicle2 = Scooter('17-ACA-122')
        vehicle3 = Scooter('14-ACA-122')

        print(f"{'_' * 50}")
        park_vehicle1 = p_lot.park(vehicle=vehicle1)
        print(park_vehicle1)

        print(f"{'_'*50}")

        park_vehicle2 = p_lot.park(vehicle=vehicle2)
        print(park_vehicle2)

        print(f"{'_' * 50}")

        park_vehicle3 = p_lot.park(vehicle=vehicle3)
        print(park_vehicle3)

        print(f"{'_' * 50}")

        unpark_vehicle2 = p_lot.unpark(vehicle=vehicle2)
        print(unpark_vehicle2)

        print(f"{'_' * 50}")

        park_vehicle3 = p_lot.park(vehicle=vehicle3)
        print(park_vehicle3)

        print(f"{'_' * 50}")

        park_vehicle1.set_exit_time((datetime.utcnow() + timedelta(minutes=40, hours=3)).strftime("%d-%b-%Y %H:%M:%S"))

        unpark_vehicle1 = p_lot.unpark(vehicle=vehicle1)
        print(unpark_vehicle1)

        print(f"{'_' * 50}")
    # }

    def test_mall_lot(self):  # {
        p_lot = MallParkingLot()

        vehicle1 = Motorcycle('12-ACA-122')
        vehicle2 = Car('17-ACA-122')
        vehicle3 = Truck('14-ACA-122')

        print(f"{'_' * 50}")
        park_vehicle1 = p_lot.park(vehicle=vehicle1)
        print(park_vehicle1)

        print(f"{'_'*50}")

        park_vehicle2 = p_lot.park(vehicle=vehicle2)
        print(park_vehicle2)

        print(f"{'_' * 50}")

        park_vehicle3 = p_lot.park(vehicle=vehicle3)
        print(park_vehicle3)

        print(f"{'_' * 50}")

        park_vehicle1.set_exit_time((datetime.utcnow() + timedelta(minutes=29, hours=3)).strftime("%d-%b-%Y %H:%M:%S"))

        unpark_vehicle1 = p_lot.unpark(vehicle=vehicle1)
        print(unpark_vehicle1)

        print(f"{'_' * 50}")

        park_vehicle2.set_exit_time((datetime.utcnow() + timedelta(minutes=1, hours=6)).strftime("%d-%b-%Y %H:%M:%S"))
        unpark_vehicle2 = p_lot.unpark(vehicle=vehicle2)
        print(unpark_vehicle2)

        print(f"{'_' * 50}")

        park_vehicle3.set_exit_time((datetime.utcnow() + timedelta(minutes=59, hours=1)).strftime("%d-%b-%Y %H:%M:%S"))
        unpark_vehicle3 = p_lot.unpark(vehicle=vehicle3)
        print(unpark_vehicle3)

        print(f"{'_' * 50}")
    # }

    def test_stadium_lot(self):  # {
        p_lot = Stadium()

        vehicle1 = Motorcycle('12-ACA-122')
        vehicle2 = Motorcycle('12-ACA-142')

        vehicle3 = Suv('17-ACA-122')
        vehicle4 = Suv('14-ACA-122')

        print(f"{'_' * 50}")
        park_vehicle1 = p_lot.park(vehicle=vehicle1)
        print(park_vehicle1)

        print(f"{'_'*50}")

        park_vehicle2 = p_lot.park(vehicle=vehicle2)
        print(park_vehicle2)

        print(f"{'_' * 50}")

        park_vehicle3 = p_lot.park(vehicle=vehicle3)
        print(park_vehicle3)

        print(f"{'_' * 50}")

        park_vehicle4 = p_lot.park(vehicle=vehicle4)
        print(park_vehicle4)

        print(f"{'_' * 50}")

        park_vehicle1.set_exit_time((datetime.utcnow() + timedelta(minutes=40, hours=3)).strftime("%d-%b-%Y %H:%M:%S"))

        unpark_vehicle1 = p_lot.unpark(vehicle=vehicle1)
        print(unpark_vehicle1)

        print(f"{'_' * 50}")

        park_vehicle2.set_exit_time((datetime.utcnow() + timedelta(minutes=59, hours=14)).strftime("%d-%b-%Y %H:%M:%S"))
        unpark_vehicle2 = p_lot.unpark(vehicle=vehicle2)
        print(unpark_vehicle2)

        print(f"{'_' * 50}")

        park_vehicle3.set_exit_time((datetime.utcnow() + timedelta(minutes=30, hours=11)).strftime("%d-%b-%Y %H:%M:%S"))
        unpark_vehicle3 = p_lot.unpark(vehicle=vehicle3)
        print(unpark_vehicle3)

        print(f"{'_' * 50}")

        park_vehicle4.set_exit_time((datetime.utcnow() + timedelta(minutes=5, hours=13)).strftime("%d-%b-%Y %H:%M:%S"))
        unpark_vehicle4 = p_lot.unpark(vehicle=vehicle4)
        print(unpark_vehicle4)

        print(f"{'_' * 50}")
    # }

    def test_airport_lot(self):  # {
        p_lot = AirportLot()

        vehicle1 = Motorcycle('11-ACA-122')
        vehicle2 = Motorcycle('12-ACA-142')
        vehicle3 = Motorcycle('13-ACA-142')

        vehicle4 = Car('17-ACA-122')
        vehicle5 = Suv('14-ACA-122')
        vehicle6 = Car('18-ACA-122')

        print(f"{'_' * 50}")
        park_vehicle1 = p_lot.park(vehicle=vehicle1)
        print(park_vehicle1)

        print(f"{'_'*50}")

        park_vehicle2 = p_lot.park(vehicle=vehicle2)
        print(park_vehicle2)

        print(f"{'_' * 50}")

        park_vehicle3 = p_lot.park(vehicle=vehicle3)
        print(park_vehicle3)

        print(f"{'_' * 50}")

        park_vehicle4 = p_lot.park(vehicle=vehicle4)
        print(park_vehicle4)

        print(f"{'_' * 50}")

        park_vehicle5 = p_lot.park(vehicle=vehicle5)
        print(park_vehicle5)

        print(f"{'_' * 50}")

        park_vehicle6 = p_lot.park(vehicle=vehicle6)
        print(park_vehicle6)

        print(f"{'_' * 50}")

        park_vehicle1.set_exit_time((datetime.utcnow() + timedelta(minutes=55, hours=0)).strftime("%d-%b-%Y %H:%M:%S"))

        unpark_vehicle1 = p_lot.unpark(vehicle=vehicle1)
        print(unpark_vehicle1)

        print(f"{'_' * 50}")

        park_vehicle2.set_exit_time((datetime.utcnow() + timedelta(minutes=59, hours=14)).strftime("%d-%b-%Y %H:%M:%S"))
        unpark_vehicle2 = p_lot.unpark(vehicle=vehicle2)
        print(unpark_vehicle2)

        print(f"{'_' * 50}")

        park_vehicle3.set_exit_time((datetime.utcnow() + timedelta(minutes=0, hours=12, days=1)).strftime("%d-%b-%Y %H:%M:%S"))
        unpark_vehicle3 = p_lot.unpark(vehicle=vehicle3)
        print(unpark_vehicle3)

        print(f"{'_' * 50}")

        park_vehicle4.set_exit_time((datetime.utcnow() + timedelta(minutes=50, hours=0)).strftime("%d-%b-%Y %H:%M:%S"))
        unpark_vehicle4 = p_lot.unpark(vehicle=vehicle4)
        print(unpark_vehicle4)

        print(f"{'_' * 50}")

        park_vehicle5.set_exit_time((datetime.utcnow() + timedelta(minutes=59, hours=23)).strftime("%d-%b-%Y %H:%M:%S"))
        unpark_vehicle5 = p_lot.unpark(vehicle=vehicle5)
        print(unpark_vehicle5)

        print(f"{'_' * 50}")

        park_vehicle6.set_exit_time((datetime.utcnow() + timedelta(minutes=0, hours=1, days=3)).strftime("%d-%b-%Y %H:%M:%S"))
        unpark_vehicle6 = p_lot.unpark(vehicle=vehicle6)
        print(unpark_vehicle6)

        print(f"{'_' * 50}")
    # }


if __name__ == '__main__':
    unittest.main()
