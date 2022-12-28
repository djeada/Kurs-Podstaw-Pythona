### Funkcje

Funkcje są blokami instrukcji zamkniętymi pod jedną nazwą i pozwalającymi na kontrolowanie z zewnątrz poprzez przekazywanie argumentów. Definicja funkcji polega na określeniu, które instrukcje należą do ciała funkcji, ile argumentów oczekuje funkcja oraz jaką nazwą będzie ona wywoływana w innych miejscach kodu. Definicja sama w sobie nie uruchamia jeszcze żadnych instrukcji - potrzebne jest użycie nazwy funkcji wraz z wartościami argumentów w innym miejscu kodu, aby instrukcje zostały wykonane. Funkcje mają następującą postać:

    def nazwa_funkcji(argumenty):
        kod # cialo funkcji

Ciało funkcji może być dowolnie rozbudowane, ale zaleca się dzielenie większych funkcji na mniejsze, które mają jasno określony cel. W ten sposób zmniejsza się złożoność kodu i ułatwia jego czytanie.

Zdefiniowaną funkcję wywołujemy w kodzie poprzez jej nazwę. Przykład:

    # w tym miejscu definiujemy funkcję
    def ryba():
       print('rybka')

    # w tym miejscu wywołujemy funkcję
    ryba()

Funkcje mogą mieć dowolną ilość argumentów - możliwe jest stworzenie funkcji bez argumentów lub funkcji z 10 argumentami. Przykład:

    def ryba(argument):
        # oczekujemy, że argument będzie liczbą naturalną
        for i in range(argument):
            print('ryba')

Słowo kluczowe <code>return</code> powoduje opuszczenie funkcji (instrukcje umieszczone poniżej nie są wykonywane). <code>return</code> pozwala również na przekazanie wartości z wnętrza funkcji do reszty programu. Taka wartość po wywołaniu funkcji jest często zapisywana w zmiennej w innym miejscu programu. Na przykład:

    def suma_trzech(a, b, c):
        return a + b + c

    suma_a = suma_trzech(3, 6, 2)
    suma_b = suma_trzech(4, 1, 7)

    print(suma_a)  # wyświetli 11
    print(suma_b)  # wyświetli 12

Możemy również zdefiniować funkcję z domyślnymi argumentami, które zostaną użyte, jeśli nie zostaną przekazane żadne inne. Domyślne argumenty muszą być umieszczone po argumentach obowiązkowych, a ich ilość nie może przekroczyć ilości argumentów obowiązkowych. Przykład:

    def suma_trzech(a, b, c=0):
        return a + b + c

    suma_a = suma_trzech(3, 6)  # a + b + c = 3 + 6 + 0 = 9
    suma_b = suma_trzech(4, 1, 7)  # a + b + c = 4 + 1 + 7 = 12

    print(suma_a)  # wyświetli 9
    print(suma_b)  # wyświetli 12

Istnieje też sposób na zdefiniowanie funkcji z nieograniczoną liczbą argumentów obowiązkowych, przy czym nie możemy ich użyć w połączeniu z argumentami domyślnymi. Przykład:

    def suma_n(*args):
        return sum(args)

    suma_a = suma_n(1, 2, 3, 4)  # 1 + 2 + 3 + 4 = 10
    suma_b = suma_n(10, 20, 30)  # 10 + 20 + 30 = 60

    print(suma_a)  # wyświetli 10
    print(suma_b)  # wyświetli 60
    
Ostatni sposób przkazywania arugmentów, to argumenty nazwane, które są przekazywane w postaci słownika. Przykład:

    def suma_n(**kwargs):
        return sum(kwargs.values())

    suma_a = suma_n(a=1, b=2, c=3, d=4)  # 1 + 2 + 3 + 4