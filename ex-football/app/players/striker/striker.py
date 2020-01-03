from app.players.player import Player


class Striker(Player):
    def __init__(self,name: str):
        super().__init__(name)