class Odd(Exception):
    def __str__(self):
        return "Liczba jest nieparzysta!"


class Number:
    def __init__(self, liczba):
        if liczba % 2 != 0:
            raise Odd()


try:
    Number(10)
    print("Success")
    Number(11)
    print("Success")
except Odd as od:
    print(od)