from app.person.exceptions import CaracteresCpfExcedidosException

_MAXIMO_DIGITOS_CPF = 11
class Cpf:
    def __init__(self,value):
        Cpf._verify_len_(value)
        self._value = value


    def get_value(self):
        return self._value


    def quantity_of_numbers(self):
        list = []
        for i in self.get_value():
            list.append(int(i))
        len_list = len(list)
        return len_list

    def quantity_of_numbers_even(self):
        quantity_even = 0
        for i in self.get_value():
            if i.isnumeric() and int(i) % 2 == 0:
                quantity_even += 1
        return quantity_even


    def quantity_of_numbers_odd(self):
        quantity_odd = 0
        for i in self.get_value():
            if i.isnumeric() and int(i) % 2 == 1:
                quantity_odd += 1
        return quantity_odd

    @staticmethod
    def _verify_len_(value):
        if len(value) > 11 or len(value) < 11:
            raise CaracteresCpfExcedidosException
