import unittest

from app.ball.types_of_balls.ball_of_championship.ball_of_championship import BallOfChampionship


class TestBallOfChampionship(unittest.TestCase):
    def test_ball_of_championship_have_color_and_be_brand(self):
        ball_of_championship = BallOfChampionship('Nike','Vermelho')
        self.assertEqual('Nike', ball_of_championship.get_brand())
        self.assertEqual('Vermelho', ball_of_championship.get_color())

