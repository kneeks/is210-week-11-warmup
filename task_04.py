#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using subclassing, to demonstrate both the has-a and is-a concepts."""


import car

TIRES = 4


class CustomCar(car.Car):
    """subclass from Car()"""
    def __init__(self, color, tires=None):
        """
        Override the class constructor CustomCar() has inherited from Car()

        Args:
            color(str): can by any color
            tires(list): list of custom tires defaulted to None

        Attributes:
            car.Car(class): calls Car() class from car.py
            tires(list): to get tires in order to find milage
        """
        car.Car.__init__(self, color)
        self.tires = tires if tires is not None else[
            CustomTire() for index in range(TIRES)]


class CustomTire(car.Tire):
    """subclass of class Tire() in car

    Attributes:
        __maximum_miles(int): num of miles on tire
    """
    __maximum_miles = 500
