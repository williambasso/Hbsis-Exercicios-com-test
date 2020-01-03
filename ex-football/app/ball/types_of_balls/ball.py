from abc import ABC

class Ball(ABC):
    def __init__(self, brand, color):
        self._brand = brand
        self._color = color

    def get_brand(self):
        return self._brand

    def get_color(self):
        return self._color