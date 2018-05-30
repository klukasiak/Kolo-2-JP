plik = open("Dane.txt", "r+")
liczby = plik.read()
listaLiczb = liczby.split(' ')

suma = 0
for i in listaLiczb:
    suma += int(i)

print(suma)
