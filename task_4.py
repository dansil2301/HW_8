#хз что тут еще можно добавить
from abc import ABC


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class OffEquip:
    def __init__(self):
        self.all_eq = {}

    def add_eq(self, item: object):
        if item in self.all_eq:
            self.all_eq[item.get_class_name()] += item.number
        else:
            self.all_eq[item.get_class_name()] = item.number
        return self.all_eq

    def send_item(self, item: object, name: object):
        try:
            if self.all_eq[item.get_class_name()] - item.number > 0:
                self.all_eq[item.get_class_name()] -= item.number
            else:
                raise OwnError('На складе нету столько объектов')
        except OwnError as err:
            print(err)
        except KeyError:
            print('Такого предмета нет!')
        else:
            name.add_eq(item)

        return name.all_eq

    def __str__(self):
        return str(self.all_eq)


class OfficeEquip(ABC):
    def __init__(self, number):
        try:
            if type(number) == int:
                self.number = number
            else:
                if number.isdigit():
                    self.number = number
                else:
                    raise OwnError('Это не число')
        except OwnError as err:
            print(err)

    @classmethod
    def get_class_name(cls):
        return cls.__name__


class Printer(OfficeEquip):
    pass


class Scanner(OfficeEquip):
    pass


class Xerox(OfficeEquip):
    pass


if __name__ == '__main__':
    item = OffEquip()
    new_company = OffEquip()
    three = Printer(3)
    two = Printer(2)
    print(f'Добавляем 3 принтера на склад: {item.add_eq(three)}')

    print(f'отправляем 2 принтера в другое место: {item.send_item(two, new_company)}')
    print('Смотрим склады команий (первая, вторая):')
    print(item)
    print(new_company)
