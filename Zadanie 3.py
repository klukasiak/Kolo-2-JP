class Short:
    lancuch = ''
    liczba = 0

    def __init__(self, lancuch, liczba):
        self.lancuch = lancuch
        self.liczba = liczba

    def first(self):
        for i in range(0, self.liczba):
            print(self.lancuch[i], end='')


prefiks = Short('Dziendobry', 5)
prefiks.first()
