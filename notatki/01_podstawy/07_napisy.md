### Napisy

Napisy to typ danych tekstowych, które składają się z ciągu znaków. Nnapisy mogą być używane do wielu różnych celów, takich jak:

* Wypisywanie tekstu na ekranie.
* Przechowywanie danych tekstowych w programie.
* Przetwarzanie i modyfikowanie tekstu.

Możemy deklarować je używając apostrofów lub cudzysłowów. 

    napis = 'James' 
    napis = "James" 
    napis = '''James''' 

Napisy są indeksowane, co oznacza, że możemy odwołać się do konkretnego znaku w napisie za pomocą jego indeksu. Możemy również wyodrębnić fragment napisu, zwany składnią wycinka (slice).

    napis = "James" 
    print(napis[1]) # a
    print(napis[2:5]) # mes

Napisy są niemodyfikowalne, co oznacza, że nie możemy bezpośrednio zmienić poszczególnych znaków w napisie. Możemy jednak tworzyć nowe napisy na podstawie istniejących napisów, zmieniając ich zawartość lub łącząc je ze sobą.

    napis = "pierwotny"
    napis = "nowy"
    
f-string to sposób formatowania napisów w Pythonie, który pozwala na wstawienie do napisu wartości zmiennych wewnątrz tekstu. W celu użycia f-string, należy przed cudzysłowami postawić literkę "f", a w odpowiednim miejscu między nawiasami klamrowymi nazwę zmiennej, której chcemy użyć.

Przykład:

    imie = "Jan"
    wiek = 30

    napis = f"Mam na imię {imie} i mam {wiek} lat."
    print(napis)

W powyższym przykładzie zmienna "imie" zostanie zamieniona na "Jan", a zmienna "wiek" na "30". Ostatecznie w wyniku wywołania print(napis) na ekranie pojawi się napis "Mam na imię Jan i mam 30 lat.".

f-string pozwala również na użycie wyrażeń arytmetycznych w napisach.

Przykład:

    a = 10
    b = 20

    napis = f"Suma a i b wynosi {a + b}."
    print(napis)

W powyższym przykładzie zostanie wyświetlony napis "Suma a i b wynosi 30.".