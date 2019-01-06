from CompetitionPackage import NotificationManager, Weather


class Competition(NotificationManager):
    __instance = None

    def __new__(cls, *args):
        if Competition.__instance is None:
            Competition.__instance = object.__new__(cls)
        return Competition.__instance

    def __init__(self, distance, weather=None):
        super().__init__()
        self.distance = distance
        self.weather = weather or Weather()

    def start(self, cars):
        results = []
        for car in cars:
            time = car.race(self.distance, self.weather)
            results.append((car.name, time))

        print("---")
        results_sorted = sorted(results, key=lambda x: x[1])
        winner_name = results_sorted[0][0]
        winner_time = results_sorted[0][1]
        print("Winner is", results_sorted[0][0])

        self.notify_subscribers(f"{winner_name} came first with {winner_time}")
