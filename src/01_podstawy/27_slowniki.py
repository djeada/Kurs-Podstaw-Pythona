"""
Modul demonstracyjny: Slowniki (dict) w Pythonie.

Omawiane zagadnienia:
- Tworzenie slownikow
- Dostep do wartosci ([], get, setdefault)
- Dodawanie, modyfikowanie, usuwanie elementow
- Iteracja po kluczach, wartosciach, parach
- Metody slownikowe
- Slowniki zagniezdzone
- Sortowanie slownikow
- Wzorce: zliczanie, grupowanie, defaultdict
"""

from collections import defaultdict, Counter

# =============================================================================
# 1. Tworzenie slownikow
# =============================================================================

print("=== 1. Tworzenie slownikow ===")

# Rozne sposoby tworzenia
pusty = {}
prosty = {"imie": "Jan", "wiek": 30, "miasto": "Warszawa"}
z_konstruktora = dict(imie="Anna", wiek=25, miasto="Krakow")
z_zip = dict(zip(["a", "b", "c"], [1, 2, 3]))
comprehension = {n: n**2 for n in range(1, 6)}

print(f"Prosty: {prosty}")
print(f"Z konstruktora: {z_konstruktora}")
print(f"Z zip: {z_zip}")
print(f"Comprehension: {comprehension}")

# =============================================================================
# 2. Dostep do wartosci
# =============================================================================

print("\n=== 2. Dostep do wartosci ===")

osoba = {"imie": "Jan", "wiek": 30, "miasto": "Warszawa"}

# Bezposredni dostep (KeyError jesli nie istnieje)
print(f"osoba['imie'] = {osoba['imie']}")

# get() - bezpieczny dostep z wartoscia domyslna
print(f"osoba.get('wiek') = {osoba.get('wiek')}")
print(f"osoba.get('email', 'brak') = {osoba.get('email', 'brak')}")

# setdefault - ustawia wartosc jesli klucz nie istnieje
email = osoba.setdefault("email", "jan@example.com")
print(f"setdefault('email'): {email}")
print(f"Osoba po setdefault: {osoba}")

# =============================================================================
# 3. Modyfikowanie slownikow
# =============================================================================

print("\n=== 3. Modyfikowanie ===")

dane = {"a": 1, "b": 2}
print(f"Poczatkowe: {dane}")

# Dodawanie/zmiana
dane["c"] = 3
dane["a"] = 10
print(f"Po zmianach: {dane}")

# update() - laczenie slownikow
dane.update({"d": 4, "e": 5})
print(f"Po update: {dane}")

# Operator | (Python 3.9+)
extra = {"f": 6, "g": 7}
polaczony = dane | extra
print(f"Polaczony (|): {polaczony}")

# Usuwanie
usuniety = dane.pop("b")
print(f"Po pop('b'): {dane} (usunieto wartosc: {usuniety})")

# pop z domyslna wartoscia (bez KeyError)
nieistniejacy = dane.pop("xyz", None)
print(f"pop('xyz', None): {nieistniejacy}")

# del - usuwanie klucza
del dane["c"]
print(f"Po del 'c': {dane}")

# =============================================================================
# 4. Iteracja
# =============================================================================

print("\n=== 4. Iteracja ===")

oceny = {"matematyka": 5, "fizyka": 4, "informatyka": 5, "polski": 3, "angielski": 4}

# Po kluczach
print("Klucze:", list(oceny.keys()))

# Po wartosciach
print("Wartosci:", list(oceny.values()))

# Po parach klucz-wartosc
print("Przedmioty i oceny:")
for przedmiot, ocena in oceny.items():
    gwiazdki = "*" * ocena
    print(f"  {przedmiot:15s} {ocena} {gwiazdki}")

# =============================================================================
# 5. Sortowanie
# =============================================================================

print("\n=== 5. Sortowanie ===")

# Po kluczach
po_kluczach = dict(sorted(oceny.items()))
print(f"Po kluczach: {po_kluczach}")

# Po wartosciach (malejaco)
po_wartosciach = dict(sorted(oceny.items(), key=lambda x: x[1], reverse=True))
print(f"Po wartosciach (desc): {po_wartosciach}")

# =============================================================================
# 6. Sprawdzanie przynaleznosci
# =============================================================================

print("\n=== 6. Sprawdzanie przynaleznosci ===")

print(f"'matematyka' in oceny: {'matematyka' in oceny}")
print(f"'biologia' in oceny: {'biologia' in oceny}")
print(f"5 in oceny.values(): {5 in oceny.values()}")

# =============================================================================
# 7. Slowniki zagniezdzone
# =============================================================================

print("\n=== 7. Slowniki zagniezdzone ===")

studenci = {
    "Jan": {"wiek": 22, "kierunek": "Informatyka", "srednia": 4.5},
    "Anna": {"wiek": 21, "kierunek": "Matematyka", "srednia": 4.8},
    "Piotr": {"wiek": 23, "kierunek": "Fizyka", "srednia": 3.9},
}

for imie, dane in studenci.items():
    print(f"  {imie}: {dane['kierunek']}, srednia: {dane['srednia']}")

# Dostep do zagniezdzonej wartosci
print(f"\nSrednia Anny: {studenci['Anna']['srednia']}")

# =============================================================================
# 8. Wzorce: zliczanie i grupowanie
# =============================================================================

print("\n=== 8. Zliczanie i grupowanie ===")

# Zliczanie reczne
tekst = "programowanie w pythonie"
licznik_znakow = {}
for znak in tekst:
    licznik_znakow[znak] = licznik_znakow.get(znak, 0) + 1
print(f"Znaki w '{tekst}':")
for znak, ile in sorted(licznik_znakow.items(), key=lambda x: -x[1])[:5]:
    print(f"  '{znak}': {ile}")

# Counter (wygodniejszy)
slowa = "ala ma kota a kot ma ale ala ma tez psa".split()
najczestsze = Counter(slowa).most_common(3)
print(f"\nNajczestsze slowa: {najczestsze}")

# defaultdict - grupowanie
owoce = [("czerwone", "jablko"), ("zolte", "banan"),
          ("czerwone", "wisnia"), ("zolte", "cytryna"),
          ("zielone", "kiwi"), ("czerwone", "truskawka")]

grupy = defaultdict(list)
for kolor, owoc in owoce:
    grupy[kolor].append(owoc)

print("\nOwoce wg koloru:")
for kolor, lista_owocow in grupy.items():
    print(f"  {kolor}: {lista_owocow}")

# =============================================================================
# 9. Przydatne operacje
# =============================================================================

print("\n=== 9. Przydatne operacje ===")

# Odwracanie slownika (klucze <-> wartosci)
oryg = {"a": 1, "b": 2, "c": 3}
odwrocony = {v: k for k, v in oryg.items()}
print(f"Odwrocony: {oryg} -> {odwrocony}")

# Filtrowanie slownika
tylko_piatki = {k: v for k, v in oceny.items() if v == 5}
print(f"Tylko piatki: {tylko_piatki}")

# Laczenie list w slownik
klucze = ["x", "y", "z"]
wartosci = [10, 20, 30]
slownik = dict(zip(klucze, wartosci))
print(f"Z zip: {slownik}")

# Kopie (plytka)
kopia = oceny.copy()
kopia["matematyka"] = 3
print(f"Oryg matematyka: {oceny['matematyka']}, kopia: {kopia['matematyka']}")
