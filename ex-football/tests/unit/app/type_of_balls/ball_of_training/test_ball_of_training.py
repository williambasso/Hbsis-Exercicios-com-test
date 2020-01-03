import unittest

from app.ball.types_of_balls.ball_of_training.bola_treino import BallOfTraining


class TestBolaTreino(unittest.TestCase):
    def test_bola_de_treino_tem_cor_e_tem_marca(self):
        bola_treino = BallOfTraining('Adidas','Azul')
        self.assertEqual('Adidas', bola_treino.get_brand())
        self.assertEqual('Azul', bola_treino.get_color())

