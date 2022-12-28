# napisy to ciagi znakow
napis = "Ala ma kota"
print(napis[0])
print(napis[1:3])
print(napis[-1])

# napisy sa niezmienne
# napis[0] = 'a' # TypeError: 'str' object does not support item assignment

# dlugosc napisu
print(len(napis))

# sprawdzanie czy napis jest w napisie
print("Ala" in napis)

# zliczanie wystapien napisu w napisie
print("a".count(napis))

# laczenie napisow
napis1 = "Ala"
napis2 = "ma kota"
napis3 = napis1 + napis2

print(napis3)

# mnozenie napisow
print(napis1 * 3)

# formatowanie napisow
imie = "Ala"
wiek = 20
print("Czesc, nazywam sie {} i mam {} lat".format(imie, wiek))
print(f"Czesc, nazywam sie {imie} i mam {wiek} lat")

# przydatne metody dla napisow
print(napis.lower())
print(napis.upper())
print(napis.title())
print(napis.capitalize())
print(napis.swapcase())
print(napis.replace("Ala", "Ola"))
print(napis.split())
print(napis.split("a"))

print("a".isalpha())
print("a".islower())
print("a".isupper())
print("a".isnumeric())
print("a".isalnum())
print("a".isspace())
