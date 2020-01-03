from app.exceptions import MaximumCapacityOfMaracanaExceededException
_MAXIMUM_PLAYERS = 11

class Maracana:
    def __init__(self):
        self._players = []

    def add(self, player):
        if self.get_quantity_of_players() is _MAXIMUM_PLAYERS:
            raise MaximumCapacityOfMaracanaExceededException()
        self._players.append(player)


    def get_quantity_of_players(self) -> int:
        return len(self._players)


