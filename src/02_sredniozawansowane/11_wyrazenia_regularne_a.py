import re


def wyodrebnij_date(dane):
    pracownik, data, odczyt = dane.split("/")
    miesiac, dzien, rok = data.split(" ")
    if dzien[-1] == ",":
        dzien = dzien[:-1]

    return miesiac, dzien, rok


def wyodrebnij_date_regex(dane):
    wynik = re.search("(.*)/(.*)/(.*)", dane)
    data = wynik.group(2)  # czesc tekstu odpowiadajaca drugiemu nawiasowi
    data = re.sub("[^\w\s]", "", data)  # usun znaki interpunkcyjne
    miesiac, dzien, rok = re.split("[\s/]", data)  # rozbij przy pomocy spacji
    return miesiac, dzien, rok


if __name__ == "__main__":
    dane = "Kowalski/Maj 15, 1983/1721.3"

    print(f"Zwykly sposob: {wyodrebnij_date(dane)}")
    print(f"Regex: {wyodrebnij_date_regex(dane)}")
