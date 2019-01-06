from CompetitionPackage import AbstractCar


class NullCarDecorator(AbstractCar):
    def __init__(self, obj):
        self.obj = obj

    def race(self, distance, weather):
        return self.obj.race(distance, weather)

    @property
    def name(self):
        return self.obj.name

    @property
    def max_speed(self):
        return self.obj.max_speed

    @property
    def drag_coef(self):
        return self.obj.drag_coef

    @property
    def time_to_max(self):
        return self.obj.time_to_max
