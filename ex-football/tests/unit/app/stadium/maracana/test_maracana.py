import unittest, pytest
from unittest.mock import Mock

from app.stadium.maracana.maracana import Maracana
from app.exceptions import MaximumCapacityOfMaracanaExceededException

class TestStadiumMaracana(unittest.TestCase):
    def test_stadium_maracana_should_have_11_players(self):
        maracana = Maracana()
        maracana.add(Mock())
        maracana.add(Mock())
        maracana.add(Mock())
        maracana.add(Mock())
        maracana.add(Mock())
        maracana.add(Mock())
        maracana.add(Mock())
        maracana.add(Mock())
        maracana.add(Mock())
        maracana.add(Mock())
        maracana.add(Mock())
        self.assertEqual(maracana.get_quantity_of_players(), 11)

    def test_stadium_maracana_shoul_have_only_11_players(self):
        maracana = Maracana()
        with pytest.raises(MaximumCapacityOfMaracanaExceededException) as ex:
            maracana.add(Mock())
            maracana.add(Mock())
            maracana.add(Mock())
            maracana.add(Mock())
            maracana.add(Mock())
            maracana.add(Mock())
            maracana.add(Mock())
            maracana.add(Mock())
            maracana.add(Mock())
            maracana.add(Mock())
            maracana.add(Mock())
            maracana.add(Mock())
        self.assertEqual(11, maracana.get_quantity_of_players())
        self.assertEqual(str(ex.value), 'Capacidade de players no stadium excedida')


