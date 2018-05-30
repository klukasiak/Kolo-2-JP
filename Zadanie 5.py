import re

linia = input("Podaj linie tekstu: ")

podciagi = re.findall(r"d.*r", linia)

print(max(podciagi))
