import sqlite3

polaczenie = sqlite3.connect('example.db')
kursor = polaczenie.cursor()

nazwa_tabeli = 'pracownicy'
szukane_pole = 'miejsce_urodzenia'
szukana_wartosc = 'Warszawa'

kursor.execute(f"SELECT * from {nazwa_tabeli} where {szukane_pole}={szukana_wartosc}")

for wiersz in kursor:
  print(wiersz)
