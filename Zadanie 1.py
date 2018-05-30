napis = input("Podaj ciag znakow: ")

if len(napis) % 2 == 0:
    polowa = len(napis) // 2
else:
    polowa = (len(napis) // 2) + 1

for i in range(0, polowa):
    print(napis[i], end='')
