import unittest, pytest
from app.cpf.cpf import Cpf
from app.person.exceptions import CaracteresCpfExcedidosException

class TestCpf(unittest.TestCase):
    def setUp(self) -> None:
        self.cpf = Cpf('11872742912')


    def test_should_have_a_cpf(self):
        self.assertEqual(self.cpf.get_value(), '11872742912')

    def test_cpf_should_have_only_11_characters(self):
        self.assertEqual(self.cpf.quantity_of_numbers(), 11)

    def test_cpf_not_should_have_more_of_11_characters(self):
        with pytest.raises(CaracteresCpfExcedidosException) as ex:
            Cpf('118727429122')
        self.assertEqual(str(ex.value),'Caracteres excedidos')

    def test_should_show_quantity_of_numbers_even_in_cpf(self):
        self.assertEqual(self.cpf.quantity_of_numbers_even(), 5)

    def test_should_show_a_quantity_of_numbers_odd_in_cpf(self):
        self.assertEqual(self.cpf.quantity_of_numbers_odd(), 6)