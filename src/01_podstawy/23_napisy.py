"""
Modul demonstracyjny: Napisy (str) w Pythonie.

Omawiane zagadnienia:
- Tworzenie i indeksowanie napisow
- Wycinki (slicing)
- Metody napisow (upper, lower, split, join, replace, strip...)
- Formatowanie (f-string, format, %)
- Sprawdzanie zawartosci (in, startswith, endswith)
- Napisy wieloliniowe
- Kodowanie znakow
"""

# =============================================================================
# 1. Tworzenie napisow
# =============================================================================

print("=== 1. Tworzenie napisow ===")

# Rozne sposoby tworzenia
pojedyncze = 'Ala ma kota'
podwojne = "Python jest super"
wieloliniowy = """To jest napis
ktory zajmuje
wiele linii."""
surowy = r"C:\Users\nowy\plik.txt"  # surowy napis (raw string)

print(f"Pojedyncze: '{pojedyncze}'")
print(f"Surowy (bez escape): '{surowy}'")
print(f"Wieloliniowy:\n{wieloliniowy}")

# =============================================================================
# 2. Indeksowanie i wycinki
# =============================================================================

print("\n=== 2. Indeksowanie i slicing ===")

napis = "Programowanie"
print(f"napis = '{napis}'")
print(f"napis[0]     = '{napis[0]}'")       # pierwszy znak
print(f"napis[-1]    = '{napis[-1]}'")      # ostatni znak
print(f"napis[0:7]   = '{napis[0:7]}'")     # pierwsze 7 znakow
print(f"napis[7:]    = '{napis[7:]}'")      # od 7. do konca
print(f"napis[::2]   = '{napis[::2]}'")     # co drugi znak
print(f"napis[::-1]  = '{napis[::-1]}'")    # odwrocony

# Napisy sa NIEMUTOWALNE
# napis[0] = 'p'  # TypeError!
nowy = 'p' + napis[1:]
print(f"Nowy (mala litera): '{nowy}'")

# =============================================================================
# 3. Operacje na napisach
# =============================================================================

print("\n=== 3. Operacje podstawowe ===")

a = "Hello"
b = "World"
print(f"Konkatenacja: '{a}' + ' ' + '{b}' = '{a + ' ' + b}'")
print(f"Powielanie: '{a}' * 3 = '{a * 3}'")
print(f"Dlugosc: len('{a}') = {len(a)}")
print(f"Zawiera 'llo': {'llo' in a}")
print(f"Nie zawiera 'xyz': {'xyz' not in a}")

# =============================================================================
# 4. Metody napisow - zmiana wielkosci liter
# =============================================================================

print("\n=== 4. Wielkość liter ===")

tekst = "ala MA kota I psa"
print(f"Tekst:       '{tekst}'")
print(f"upper():     '{tekst.upper()}'")
print(f"lower():     '{tekst.lower()}'")
print(f"title():     '{tekst.title()}'")
print(f"capitalize():'{tekst.capitalize()}'")
print(f"swapcase():  '{tekst.swapcase()}'")

# =============================================================================
# 5. Metody - wyszukiwanie i zamiana
# =============================================================================

print("\n=== 5. Wyszukiwanie i zamiana ===")

zdanie = "Python jest prosty. Python jest potezny."
print(f"Zdanie: '{zdanie}'")
print(f"count('Python'):    {zdanie.count('Python')}")
print(f"find('prosty'):     {zdanie.find('prosty')}")
print(f"find('trudny'):     {zdanie.find('trudny')}")  # -1 jesli nie ma
print(f"startswith('Pyth'): {zdanie.startswith('Pyth')}")
print(f"endswith('.'):      {zdanie.endswith('.')}")
print(f"replace('Python', 'Java'): '{zdanie.replace('Python', 'Java')}'")

# =============================================================================
# 6. Metody - dzielenie i laczenie
# =============================================================================

print("\n=== 6. split() i join() ===")

sciezka = "/home/user/dokumenty/plik.txt"
czesci = sciezka.split("/")
print(f"split('/'): {czesci}")

csv_linia = "Jan,Kowalski,30,Warszawa"
dane = csv_linia.split(",")
print(f"split(','): {dane}")

# join - laczenie
slowa = ["Python", "jest", "super"]
polaczone = " ".join(slowa)
print(f"' '.join({slowa}): '{polaczone}'")

# join z separatorem
numery = ["1", "2", "3", "4", "5"]
print(f"'-'.join: '{'-'.join(numery)}'")

# splitlines
wieloliniowy = "Linia 1\nLinia 2\nLinia 3"
linie = wieloliniowy.splitlines()
print(f"splitlines: {linie}")

# =============================================================================
# 7. Metody - obcinanie (strip)
# =============================================================================

print("\n=== 7. strip() ===")

z_spacjami = "   Tekst z spacjami   "
print(f"Oryginal: '{z_spacjami}'")
print(f"strip():  '{z_spacjami.strip()}'")
print(f"lstrip(): '{z_spacjami.lstrip()}'")
print(f"rstrip(): '{z_spacjami.rstrip()}'")

# strip konkretnych znakow
url = "...www.example.com..."
print(f"strip('.'): '{url.strip('.')}'")

# =============================================================================
# 8. Formatowanie napisow
# =============================================================================

print("\n=== 8. Formatowanie ===")

imie = "Jan"
wiek = 30
wzrost = 1.756

# f-string (Python 3.6+) - zalecane
print(f"f-string: {imie}, {wiek} lat, {wzrost:.2f}m")

# format()
print("format(): {}, {} lat, {:.2f}m".format(imie, wiek, wzrost))

# Formatowanie zaawansowane
liczba = 1234567.89
print(f"  Separatory:  {liczba:,.2f}")
print(f"  Wyrownananie: '{imie:<10}' (lewo)")
print(f"  Wyrownananie: '{imie:>10}' (prawo)")
print(f"  Wyrownananie: '{imie:^10}' (srodek)")
print(f"  Wypelnienie:  '{imie:*^10}'")
print(f"  Binarnie:     {42:b}")
print(f"  Szesnastkowo: {255:x}")
print(f"  Osemkowo:     {8:o}")

# =============================================================================
# 9. Metody sprawdzajace zawartosc
# =============================================================================

print("\n=== 9. Metody sprawdzajace ===")

testy = ["abc", "ABC", "123", "abc123", "   ", "Hello World"]
for t in testy:
    print(f"  '{t:12s}' -> alpha={t.isalpha()}, digit={t.isdigit()}, "
          f"alnum={t.isalnum()}, space={t.isspace()}")

# =============================================================================
# 10. Przydatne wzorce
# =============================================================================

print("\n=== 10. Przydatne wzorce ===")

# Odwracanie napisu
tekst = "Python"
odwrocony = tekst[::-1]
print(f"Odwrocony '{tekst}': '{odwrocony}'")

# Sprawdzanie palindromu
slowo = "kajak"
jest_palindrom = slowo == slowo[::-1]
print(f"'{slowo}' to palindrom: {jest_palindrom}")

# Zliczanie slow
zdanie = "ala ma kota a kot ma ale"
slownik_slow = {}
for slowo in zdanie.split():
    slownik_slow[slowo] = slownik_slow.get(slowo, 0) + 1
print(f"Zliczanie slow: {slownik_slow}")

# Zamiana znakow (translate)
tablica = str.maketrans("aeiou", "AEIOU")
print(f"translate (samogloski): '{zdanie.translate(tablica)}'")

# Wyodrebnianie cyfr z tekstu
mieszany = "Mam 2 koty i 3 psy, razem 5 zwierzat"
cyfry = [znak for znak in mieszany if znak.isdigit()]
print(f"Cyfry z '{mieszany[:30]}...': {cyfry}")
