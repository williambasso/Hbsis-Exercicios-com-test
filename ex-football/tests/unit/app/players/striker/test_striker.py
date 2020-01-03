import unittest

from app.players.striker.striker import Striker


class TestStriker(unittest.TestCase):
    def test_striker_should_have_one_name_and_be_striker(self):
        striker = Striker('Neymar')
        self.assertEqual(striker.get_name(), 'Neymar')
        self.assertIsInstance(striker, Striker)