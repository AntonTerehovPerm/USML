from abc import ABC, abstractmethod


class AbstractCar(ABC):
    @abstractmethod
    def race(self, distance, weather):
        pass

    @property
    @abstractmethod
    def name(self):
        return None

    @property
    @abstractmethod
    def max_speed(self):
        return None

    @property
    @abstractmethod
    def drag_coef(self):
        return None

    @property
    @abstractmethod
    def time_to_max(self):
        return None
