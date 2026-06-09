import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'lesson18'))
from classes import Vehicle, Airplane, Truck, GolfCart
import io
from contextlib import redirect_stdout


class TestVehicle(unittest.TestCase):

    def test_vehicle_make(self):
        car = Vehicle('Tesla', 'Model 3')
        self.assertEqual(car.make, 'Tesla')

    def test_vehicle_model(self):
        car = Vehicle('Tesla', 'Model 3')
        self.assertEqual(car.model, 'Model 3')

    def test_vehicle_moves(self):
        car = Vehicle('Tesla', 'Model 3')
        f = io.StringIO()
        with redirect_stdout(f):
            car.moves()
        self.assertIn('Moves along', f.getvalue())

    def test_vehicle_get_make_model(self):
        car = Vehicle('Tesla', 'Model 3')
        f = io.StringIO()
        with redirect_stdout(f):
            car.get_make_model()
        self.assertIn('Tesla', f.getvalue())
        self.assertIn('Model 3', f.getvalue())


class TestAirplane(unittest.TestCase):

    def test_airplane_inherits_make(self):
        cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
        self.assertEqual(cessna.make, 'Cessna')

    def test_airplane_faa_id(self):
        cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
        self.assertEqual(cessna.faa_id, 'N-12345')

    def test_airplane_moves(self):
        cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
        f = io.StringIO()
        with redirect_stdout(f):
            cessna.moves()
        self.assertIn('Flies along', f.getvalue())


class TestTruck(unittest.TestCase):

    def test_truck_moves(self):
        mack = Truck('Mack', 'Pinnacle')
        f = io.StringIO()
        with redirect_stdout(f):
            mack.moves()
        self.assertIn('Rumbles along', f.getvalue())


class TestGolfCart(unittest.TestCase):

    def test_golfcart_inherits_moves(self):
        golfwagon = GolfCart('Yamaha', 'GC100')
        f = io.StringIO()
        with redirect_stdout(f):
            golfwagon.moves()
        self.assertIn('Moves along', f.getvalue())

    def test_golfcart_is_vehicle(self):
        golfwagon = GolfCart('Yamaha', 'GC100')
        self.assertIsInstance(golfwagon, Vehicle)


if __name__ == "__main__":
    unittest.main()