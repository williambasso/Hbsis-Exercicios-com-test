from abc import ABC

class Player(ABC):
    def __init__(self,name: str):
        self._name = name

    def get_name(self):
        return self._name