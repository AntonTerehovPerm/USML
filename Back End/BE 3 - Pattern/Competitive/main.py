from CompetitionPackage import *

if __name__ == "__main__":
    weather = Weather(35)
    competition = Competition(10000, weather)

    competition.subscribe(EmailSubscriber("test@example.com"))
    competition.subscribe(SmsSubscriber("+79990000000"))

    cars = [
        Car('ferrary'),
        Car('bugatti'),
        Car('toyota'),
        Car('lada'),
        Car('sx4'),
        Car('drandulet', max_speed=120, drag_coef=0.42, time_to_max=63)
    ]

    cars = map(lambda x: VerboseCar(x), cars)

    competition.start(cars)
