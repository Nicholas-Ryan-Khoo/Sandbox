from car import Car
from random import randint


class UnreliableCar(Car):
    """Version of car that includes reliability"""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        self.reliability = reliability
        super().__init__(name, fuel)

    def drive(self, distance):
        """Driving the car"""
        rand_num = randint(1, 100)
        if rand_num >= self.reliability:
            distance = 0

        dist_driven = super().drive(distance)
        return dist_driven
