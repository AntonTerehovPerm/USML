from random import randint


class Weather:
    def __init__(self, max_wind_speed=20):
        self._max_wind_speed = max_wind_speed

    @property
    def wind_speed(self):
        return randint(0, self._max_wind_speed)
