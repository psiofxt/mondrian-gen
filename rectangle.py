# stdlib
import random
from math import sqrt


class Rectangle():
    """
    Class responsible for representing a rectangle object. Each rectangle
    has coordinates for its four corners as well as a unique id
    """
    counter = 0

    def __init__(self, upper_left_coord, lower_right_coord):
        if not isinstance(upper_left_coord, tuple) and \
           not isinstance(lower_right_coord, tuple):
           raise Exception("Rectangle arguments must be tuples")
        if not isinstance(upper_left_coord[0], int) and \
           not isinstance(upper_left_coord[1], int) and \
           not isinstance(lower_right_coord[0], int) and \
           not isinstance(lower_right_coord[1], int):
           raise Exception("Tuple entries must be integers")

        self.x1 = upper_left_coord[0]
        self.y1 = upper_left_coord[1]
        self.x2 = lower_right_coord[0]
        self.y2 = upper_left_coord[1]
        self.x3 = lower_right_coord[0]
        self.y3 = lower_right_coord[1]
        self.x4 = upper_left_coord[0]
        self.y4 = lower_right_coord[1]
        self.id = Rectangle.counter
        self.params = {
            'id': Rectangle.counter
        }
        Rectangle.counter += 1

    colors = ['white',
              'black',
              'red',
              'blue',
              'yellow']

    def __repr__(self):
        return f'{self.__class__.__name__} : {self.id}'

    def __getitem__(self, key):
        return self.params[key]

    def update_all(self, params):
        for key, value in params.items():
            setattr(self, key, value)
            self.params[key] = value

    def calculate_area(self):
        side_one = sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        side_two = sqrt((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2)

        return side_one * side_two

    def calculate_center(self):
        middle_x = (self.x1 + self.x2) / 2
        middle_y = (self.y2 + self.y3) / 2

        return (middle_x, middle_y)
