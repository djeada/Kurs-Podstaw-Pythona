# lista slownikow
# mini baza ksiazek w ksiegarni
# lista slownikow reprezentujaca ksiazki w ksiegarni
# dodawnie ksiazki
# usuwac
# wyswietlanie ksiazek wedlug kryterium
# znajdowanie najtanszej oraz najdrozszej ksiazki

from operator import itemgetter


def dodaj_ksiazke(ksiazki, tytul, cena):
    klucz = (tytul, cena)
    if klucz in ksiazki:
        ksiazki[klucz] += 1
    else:
        ksiazki[klucz] = 1


def usun_ksiazke(ksiazki, tytul):
    for klucz in ksiazki.keys():
        if klucz[0] == tytul:
            ksiazki[klucz] -= 1
            if ksiazki[klucz] == 0:
                del ksiazki[klucz]
            break


def wyswietl_ksiazki(ksiazki):
    for klucz, liczba in ksiazki.items():
        print(f"{klucz[0]} {klucz[1]} {liczba}")


def znajdz_najtansza_ksiazke(ksiazki):
    najtansza = min(ksiazki.keys(), key=itemgetter(1))
    print(f"Najtansza ksiazka: {najtansza[0]} {najtansza[1]}")


def znajdz_najdrozsza_ksiazke(ksiazki):
    najdrozsza = max(ksiazki.keys(), key=itemgetter(1))
    print(f"Najdrozsza ksiazka: {najdrozsza[0]} {najdrozsza[1]}")


def czy_ksiazka_jest_w_ksiegarni(ksiazki, tytul):
    for klucz in ksiazki.keys():
        if klucz[0] == tytul:
            return True
    return False


def menu():

    while True:
        print("\nMenu:")
        print("1. Dodaj ksiazke")
        print("2. Usun ksiazke")
        print("3. Wyswietl ksiazki")
        print("4. Znajdz najtansza ksiazke")
        print("5. Znajdz najdrozsza ksiazke")
        print("6. Sprawdz czy ksiazka jest w ksiegarni")
        print("7. Wyjdz")
        opcja = input("\nWybierz opcje: ")
        if opcja == "7":
            break
        yield opcja


def main():
    ksiazki = {
        (tytul, cena): ilosc
        for tytul, cena, ilosc in [
            ("Pan Tadeusz", 20, 3),
            ("Dziady", 25, 2),
            ("Lalka", 30, 1),
        ]
    }

    for opcja in menu():
        if opcja == "1":
            tytul = input("Podaj tytul: ")
            cena = float(input("Podaj cene: "))
            dodaj_ksiazke(ksiazki, tytul, cena)
        elif opcja == "2":
            tytul = input("Podaj tytul: ")
            usun_ksiazke(ksiazki, tytul)
        elif opcja == "3":
            wyswietl_ksiazki(ksiazki)
        elif opcja == "4":
            znajdz_najtansza_ksiazke(ksiazki)
        elif opcja == "5":
            znajdz_najdrozsza_ksiazke(ksiazki)
        elif opcja == "6":
            tytul = input("Podaj tytul: ")
            if czy_ksiazka_jest_w_ksiegarni(ksiazki, tytul):
                print("Ksiazka jest w ksiegarni")
            else:
                print("Ksiegarnia nie posiada takiej ksiazki")


if __name__ == "__main__":
    main()
