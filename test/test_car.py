import unittest
from datetime import datetime, timedelta
from car import Calliope, Glissade, Palindrome, Rorschach, Thovex
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine

class TestCar(unittest.TestCase):
    def test_calliope_needs_service(self):
        car = Calliope(datetime.today() - timedelta(days=3*365), 35000, 5000)
        self.assertTrue(car.needs_service())

    def test_glissade_needs_service(self):
        car = Glissade(datetime.today() - timedelta(days=3*365), 65000, 5000)
        self.assertTrue(car.needs_service())

    def test_palindrome_needs_service(self):
        car = Palindrome(datetime.today() - timedelta(days=5*365), True)
        self.assertTrue(car.needs_service())

    def test_rorschach_needs_service(self):
        car = Rorschach(datetime.today() - timedelta(days=5*365), 65000, 5000)
        self.assertTrue(car.needs_service())

    def test_thovex_needs_service(self):
        car = Thovex(datetime.today() - timedelta(days=5*365), 35000, 5000)
        self.assertTrue(car.needs_service())

    def test_calliope_does_not_need_service(self):
        car = Calliope(datetime.today(), 20000, 5000)
        self.assertFalse(car.needs_service())

    def test_glissade_does_not_need_service(self):
        car = Glissade(datetime.today(), 40000, 5000)
        self.assertFalse(car.needs_service())

    def test_palindrome_does_not_need_service(self):
        car = Palindrome(datetime.today(), False)
        self.assertFalse(car.needs_service())

    def test_rorschach_does_not_need_service(self):
        car = Rorschach(datetime.today(), 40000, 5000)
        self.assertFalse(car.needs_service())

    def test_thovex_does_not_need_service(self):
        car = Thovex(datetime.today(), 20000, 5000)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
