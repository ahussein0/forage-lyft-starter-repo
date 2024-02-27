import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex



from datetime import datetime
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine

class Car:
    def __init__(self, engine, last_service_date):
        self.engine = engine
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.needs_battery_service() or self.engine.needs_service()

    def needs_battery_service(self):
        raise NotImplementedError

class Calliope(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(CapuletEngine(last_service_date, current_mileage, last_service_mileage), last_service_date)

    def needs_battery_service(self):
        return self.last_service_date.year <= datetime.today().year - 3

class Glissade(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(WilloughbyEngine(last_service_date, current_mileage, last_service_mileage), last_service_date)

    def needs_battery_service(self):
        return self.last_service_date.year <= datetime.today().year - 3

class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(SternmanEngine(last_service_date, warning_light_is_on), last_service_date)

    def needs_battery_service(self):
        return self.last_service_date.year <= datetime.today().year - 5

class Rorschach(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(WilloughbyEngine(last_service_date, current_mileage, last_service_mileage), last_service_date)

