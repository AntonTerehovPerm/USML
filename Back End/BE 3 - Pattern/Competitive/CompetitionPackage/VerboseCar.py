from CompetitionPackage import NullCarDecorator


class VerboseCar(NullCarDecorator):
    def __init__(self, obj):
        super().__init__(obj)

    def race(self, distance, weather):
        print("Car <%s> on start" % self.obj.name)
        time = self.obj.race(distance, weather)
        print("Car <%s> result: %f" % (self.obj.name, time))
        return time
