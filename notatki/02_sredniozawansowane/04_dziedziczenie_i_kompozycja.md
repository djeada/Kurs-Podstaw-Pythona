### Dziedziczenie i kompozycja

Dziedziczenie i kompozycja to dwie techniki pozwalające na użycie kodu z innych klas w nowo tworzonej klasie. Dziedziczenie kopiuje wszystkie elementy z klasy nadrzędnej do klasy podrzędnej i pozwala na bezpośredni dostęp do pól i metod klasy nadrzędnej oraz możliwość zmiany ich definicji w klasie podrzędnej. Jest to używane, gdy nowa klasa jest specjalnym rodzajem już istniejącej klasy.

    class Czlowiek:
        def __init__(self, imie: str, nazwisko: str, miejsce_urodzenia: str, zawod: str):
            self.imie = imie
            self.nazwisko = nazwisko
            self.miejsce_urodzenia = miejsce_urodzenia
            self.zawod = zawod

        def __str__(self):
            return f"{self.imie} {self.nazwisko} {self.miejsce_urodzenia} {self.zawod}"


    class Student(Czlowiek):
        def __init__(self, imie: str, nazwisko: str, miejsce_urodzenia: str, numer_albumu: int, kierunek_studiow: str):
            super().__init__(imie, nazwisko, miejsce_urodzenia, 'student')
            self.numer_albumu = numer_albumu
            self.kierunek_studiow = kierunek_studiow

        def __str__(self):
            return f"{super().__str__()} {self.numer_albumu} {self.kierunek_studiow}"

        def __repr__(self):
            return f"{super().__repr__()} {self.numer_albumu} {self.kierunek_studiow}"

W powyższym przykładzie, klasa `Człowiek` jest klasą nadrzędną, a klasa `Student` jest klasą podrzędną. Klasa `Student` dziedziczy po klasie `Człowiek`, co oznacza, że posiada wszystkie pola i metody zdefiniowane w klasie `Człowiek`. Może również zmienić definicję metod z klasy nadrzędnej poprzez nadpisanie ich w klasie podrzędnej. W tym przykładzie, klasa `Student` nadpisuje metodę `str()` klasy `Człowiek`, aby dodać dodatkowe informacje o numerze albumu i kierunku studiów studenta. Klasa `Student` również nadpisuje metodę `repr()` klasy Człowiek, co oznacza, że jej reprezentacja tekstowa będzie również zawierać te dodatkowe informacje.

Kompozycja zaś polega na umieszczeniu obiektu jednej klasy jako pola w innej klasie. W nowo definiowanej klasie nie ma bezpośredniego dostępu do pól ani metod klasy skomponowanej, ale można do nich dotrzeć poprzez instancję tej klasy. Kompozycja jest używana, gdy nowa klasa reprezentuje całość, której istniejąca klasa jest częścią.
 
    class Pensja:

        def __init__(self, pensja: int, stopa_podwyzki: float):
            self.pensja = pensja
            self.stopa_podwyzki = stopa_podwyzki

        def __str__(self):
            return f"Pensja: {self.pensja}, stopa podwyzki: {self.stopa_podwyzki}"

    class Pracownik:

            def __init__(self, imie: str, nazwisko:str, pensja: Pensja):
                self.imie = imie
                self.nazwisko = nazwisko
                self.pensja = pensja # kompozycja, pensja jest czescia pracownika

            def __str__(self):
                return f"Pracownik: {self.imie} {self.nazwisko}, zarabia rocznie: {self.pensja.roczna_pensja()}"

Ten przykład ilustruje kompozycję, gdzie klasa `Pracownik` zawiera instancję klasy `Pensja` jako jedno z pól. W klasie `Pracownik` mamy metodę `roczna_pensja`, która zwraca wartość zapisaną w polu pensja pomnożoną przez stopę podwyżki. Klasa `Pracownik` nie ma bezpośredniego dostępu do pól lub metod klasy `Pensja`, ale może je użyć poprzez instancję tej klasy zapisaną w polu pensja. W ten sposób nowo definiowana klasa `Pracownik` reprezentuje pewną całość, w której istniejąca klasa `Pensja` jest jej częścią.
