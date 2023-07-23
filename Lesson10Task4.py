#Создайте класс Сотрудник.
#Воспользуйтесь классом человека из прошлого задания.
#У сотрудника должен быть:
#шестизначный идентификационный номер
#уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

from Lesson10Task3 import Persen

class Enpl(Persen):
    MAX_LEVEL = 7
    def __init__(self, last_neme: str, fers_neme: str, patronomic: str, age: int, id: int):
        super().__init__(last_neme, fers_neme, patronomic, age)
        if 100_000 <= id <= 999_999:
            self.id = id
        else:
            self.id = 100_000

    def get_level(self):
        z = sum(int(num) for num in str(self.id))
        return z % self.MAX_LEVEL

enp = Enpl('Иванов', 'Иван', 'Иванович', 35, 100_257)
print(enp.get_level())