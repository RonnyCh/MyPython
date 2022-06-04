# test module


def calc(a):

    def times10(b):
        d = b * 5
        return d

    b = a * 10
    x = times10(b)
    return x

calc(10)