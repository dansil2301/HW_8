class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div(a, b):
    return a / b


if __name__ == '__main__':
    a = int(input('input a number: '))
    b = int(input('input a number: '))

    try:
        if b != 0:
            print(a / b)
        else:
            raise OwnError("u can't divide by 0")
    except OwnError as err:
        print(err)
