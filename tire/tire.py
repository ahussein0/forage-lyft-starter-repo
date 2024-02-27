class Tire:
    def __init__(self, wear_values):
        self.wear_values = wear_values

    def needs_service(self):
        raise NotImplementedError


class CarriganTire(Tire):
    def needs_service(self):
        return any(wear >= 0.9 for wear in self.wear_values)


class OctoprimeTire(Tire):
    def needs_service(self):
        return sum(self.wear_values) >= 3
