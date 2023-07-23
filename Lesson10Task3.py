#Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
#У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
#Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

class Persen:
    def __init__(self, last_neme: str, fers_neme: str, patronomic: str, age: int):
        self.last_name = last_neme
        self.ferss_neme = fers_neme
        self.patronomic = patronomic
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.ferss_neme} {self.patronomic}'

    def birthday(self):
        self._age += 1

    def get_ege(self):
        return self._age

persen1 = Persen('Иванов', 'Иван', 'Иванович', 35)

print(persen1.full_name())
print(persen1.get_ege())
persen1.birthday()
print(persen1.get_ege())
print(persen1._age)
