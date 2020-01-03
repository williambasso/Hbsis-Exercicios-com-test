from app.ball.types_of_balls.ball import Ball


class BallOfChampionship(Ball):
    def __init__(self, brand: str, color: str):
        super().__init__(brand,color)
