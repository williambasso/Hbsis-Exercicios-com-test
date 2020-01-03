import unittest

from app.players.goalkeeper.goalkeeper import Goalkeeper


class TestGoalkeeper(unittest.TestCase):
    def test_goalkeeper_should_have_one_name_and_be_goalkeeper(self):
        goalkeeper = Goalkeeper('Jiraya')
        self.assertEqual(goalkeeper.get_name(), 'Jiraya')
        self.assertIsInstance(goalkeeper, Goalkeeper)