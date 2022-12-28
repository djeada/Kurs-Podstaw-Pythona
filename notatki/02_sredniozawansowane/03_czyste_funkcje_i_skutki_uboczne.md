### Czyste funkcje i skutki uboczne

NW przeciwieństwie do funkcji produkujących skutki uboczne, czyste funkcje nie wpływają na środowisko poza swoim zasięgiem. 

Skutki uboczne to m.in.
* Zmiany w plikach.
* Zmiany w bazie danych.
* Wysyłanie informacji przez sieć.
* Zmiany w globalnych zmiennych.

Przykłady czystych funkcji to:

* Funkcja zwracająca wartość pola trójkąta na podstawie jego boków.
* Funkcja zwracająca iloczyn elementów w liscie.
* Funkcja zwracająca największy element w liscie.
* Funkcja zwracająca nową listę z liczbami parzystymi z oryginalnej listy.
* Funkcja zwracająca nowy słownik z tylko niektórymi kluczami z oryginalnego słownika.
* Funkcja zwracająca nowy napis z dużymi literami z oryginalnego napisu.

Czyste funkcje najlepiej pracują z niemutowalnymi obiektami. Można zaimplementować czystą funkcję także z użyciem mutowalnych obiektów, o ile nie modyfikujemy ich stanu podczas działania funkcji. Ważne jest, aby czysta funkcja nie powodowała żadnych skutków ubocznych, czyli żadnych zmian w stanie obiektów poza wartościami, które zwraca.

Obiekty mutowalne to obiekty, które po utworzeniu można zmienić. W Pythonie obiekty mutowalne to np. listy, słowniki i zbiory (set). Obiekty mutowalne są niebezpieczne, ponieważ ich stan może zostać zmieniony w nieoczekiwany sposób, dlatego lepiej preferować obiekty niemutowalne, które zapewniają większe bezpieczeństwo, choć za cenę mniejszej wydajności. Aby zwiększyć bezpieczeństwo, lepiej stosować funkcje, które zamiast modyfikować stan obiektów mutowalnych, zwracają nowy obiekt, nie ruszając przekazanych jako parametry obiektów.

Przykłady obiektów mutowalnych:

    lista = [1, 2, 3]
    lista.append(4)
    print(lista) # [1, 2, 3, 4]

    slownik = {'klucz': 'wartosc'}
    slownik['nowy_klucz'] = 'nowa_wartosc'
    print(slownik) # {'klucz': 'wartosc', 'nowy_klucz': 'nowa_wartosc'}

    zbior = {1, 2, 3}
    zbior.add(4)
    print(zbior) # {1, 2, 3, 4}

Przykłady obiektów niemutowalnych:

    liczba = 5
    liczba = 6 # możemy zmienić wartość zmiennej, ale nie możemy zmienić samej liczby

    napis = 'napis'
    napis[1] = 'a' # nie możemy zmienić poszczególnych znaków w napisie

    krotka = (1, 2, 3)
    krotka[1] = 4 # nie możemy zmienić wartości elementów w krotce