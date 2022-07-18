class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    ls = []

    while True:
        n = input('input a number: ')

        if n == 'stop':
            break

        try:
            if n.isdigit():
                ls.append(n)
            else:
                raise OwnError('not a number!')
        except OwnError as err:
            print(err)

    print(ls)
