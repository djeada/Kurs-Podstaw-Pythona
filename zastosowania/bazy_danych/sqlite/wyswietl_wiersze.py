import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

nazwa_tabeli = 'pracownicy'
szukane_pole = 'miejsce_urodzenia'
szukana_wartosc = 'Warszawa'

c.execute(f"SELECT * from {nazwa_tabeli} where {szukane_pole}={szukana_wartosc}")
for row in c:
  print row
