import string

t = string.Template("$x ma brata $y")

slownik1 = {"x": "James", "y": "Tunczyk"}
print(t.substitute(slownik1))

slownik2 = {"x": "Adam", "y": "Adama"}
print(t.substitute(slownik2))

slownik3 = {"x": "Brokul", "y": "Kukurydze"}
print(t.substitute(slownik3))


lista_studentow = [("Adam", 30), ("Hans", 50), ("Janes", 100)]

k = string.Template("$x otrzymal $y punktow na egzaminie")

for i in lista_studentow:
    print(k.substitute(x=i[0], y=i[1]))


lista_produktow = [
    {"nazwa": "Tunczyk", "cena": 30, "ilosc": 10},
    {"nazwa": "Brokul", "cena": 7, "ilosc": 20},
    {"nazwa": "Pomidor", "cena": 3, "ilosc": 10},
]

produkty = string.Template(
    "dodales do koszyka $ilosc produktow $nazwa w cenie $cena za sztuke."
)

for i in lista_produktow:
    print(produkty.substitute(i))
