class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age


    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


    def quantity_of_lower_letters_in_name(self):
        quantity_lower_letters = 0
        for i in self.get_name():
            if i.islower():
                quantity_lower_letters += 1
        return quantity_lower_letters


    def quantity_of_upper_letters_in_name(self):
        quantity_upper_letters = 0
        for i in self.get_name():
            if i.isupper():
                quantity_upper_letters += 1
        return quantity_upper_letters


    def over_18_years(self):
        if self.get_age().isnumeric() and int(self.get_age()) >= 18:
            return 'Adult'






