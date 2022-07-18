class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def to_int(cls, data):
        try:
            day = int(data[0:2])
            month = int(data[3:5])
            year = int(data[6:8])
        except:
            print('Неправильный ввод данных')
            day, month, year = 0, 0, 0
        return day, month, year

    @staticmethod
    def valid_data(data):
        day = ''
        month = ''
        year = ''
        months = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        out = 'Все верно'
        if len(data) == 10:
            if data[2] == '-' and data[5] == '-':
                day, month, year = Data.to_int(data)
            else:
                out = 'Ошибка'
        else:
            out = 'Ошибка'

        try:
            if months[month] < day or day <= 0 or year < 0:
                out = 'Ошибка'
        except:
            out = 'Ошибка'

        return out


if __name__ == '__main__':
    print(Data.valid_data('03-03-1233'))
    print(Data.to_int('03-03-1233'))
