import unittest, pytest
from app.person.person import Person



class TestPerson(unittest.TestCase):

    def setUp(self) -> None:
        self.person = Person('WilliaM Basso', '18')

    def test_person_should_have_name_and_age(self):
        self.assertEqual(self.person.get_name(), 'WilliaM Basso')
        self.assertEqual(self.person.get_age(), '18')

    def test_person_should_be_of_legal_age(self):
        self.assertEqual(self.person.over_18_years(), 'Adult')

    def test_should_a_quantity_of_lower_letters_in_name(self):
        self.assertEqual(self.person.quantity_of_lower_letters_in_name(), 9)

    def test_should_a_quantity_of_upper_letters_in_name(self):
        self.assertEqual(self.person.quantity_of_upper_letters_in_name(), 3)










