from CompetitionPackage import AbstractCar


class Car(AbstractCar):
    CAR_SPECS = {
        'ferrary': {"max_speed": 340, "drag_coef": 0.324, "time_to_max": 26},
        'bugatti': {"max_speed": 407, "drag_coef": 0.39, "time_to_max": 32},
        'toyota': {"max_speed": 180, "drag_coef": 0.25, "time_to_max": 40},
        'lada': {"max_speed": 180, "drag_coef": 0.32, "time_to_max": 56},
        'sx4': {"max_speed": 180, "drag_coef": 0.33, "time_to_max": 44},
    }

    def __init__(self, name, max_speed=None, drag_coef=None, time_to_max=None):
        self.__name = name

        if None in [max_speed, drag_coef, time_to_max]:
            if name not in Car.CAR_SPECS:
                raise KeyError(f"Не удалось найти существующую спецификацию для {name}. Задайте спецификацию вручную")

            self.__max_speed = Car.CAR_SPECS[name]['max_speed']
            self.__drag_coef = Car.CAR_SPECS[name]['drag_coef']
            self.__time_to_max = Car.CAR_SPECS[name]['time_to_max']
        else:
            self.__max_speed = max_speed
            self.__drag_coef = drag_coef
            self.__time_to_max = time_to_max

    @property
    def name(self):
        return self.__name

    @property
    def max_speed(self):
        return self.__max_speed

    @property
    def drag_coef(self):
        return self.__drag_coef

    @property
    def time_to_max(self):
        return self.__time_to_max

    def race(self, distance, weather):
        car = self
        time = 0

        for distance in range(distance):
            wind_speed = weather.wind_speed

            if time == 0:
                speed = 1
            else:
                speed = car.max_speed if time > car.time_to_max else (time / car.time_to_max) * car.max_speed
                if speed > wind_speed:
                    speed -= (car.drag_coef * wind_speed)

            time += float(1) / speed

        return time
