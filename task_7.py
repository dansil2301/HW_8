class Complex:
    def __init__(self, c_number):
        number = c_number[0:c_number.find(' ')].strip()
        sign = '+' if '+' in c_number else '-'
        comp = c_number[c_number.rfind(' '):len(c_number) - 1].strip()
        comp = ('-' if sign == '-' else '') + comp
        comp = (comp + '1') if comp == '-' else comp if comp != '' else '1'
        self.c_number = (number, comp)

    def __add__(self, other):
        c_number = str(int(self.c_number[0]) + int(other.c_number[0]))
        intern = int(self.c_number[1]) + int(other.c_number[1])
        c_number += ' - ' if intern < 0 else ' + '
        intern = -1 * intern if intern < 0 else intern
        c_number +=(str(intern) if intern != 1 else '') + 'i' if intern != 0 else ''
        return c_number

    def __mul__(self, other):
        c_number = str(int(self.c_number[0]) * int(other.c_number[0]) - int(self.c_number[1]) * int(other.c_number[1]))
        intern = int(self.c_number[0]) * int(other.c_number[1]) + int(self.c_number[1]) * int(other.c_number[0])
        c_number += ' - ' if intern < 0 else ' + '
        intern = -1 * intern if intern < 0 else intern
        c_number += (str(intern) if intern != 1 else '') + 'i'
        return c_number


if __name__ == '__main__':
    number1 = Complex('3 - 5i')
    number2 = Complex('2 - 6i')

    print(number2 + number1)
    print(number2 * number1)
