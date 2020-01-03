import unittest

from app.players.defender.defender import Defender


class TestDefender(unittest.TestCase):
    def test_defender_should_have_one_name_and_be_defender(self):
        defender = Defender('Sasuke')
        self.assertEqual(defender.get_name(), 'Sasuke')
        self.assertIsInstance(defender, Defender)