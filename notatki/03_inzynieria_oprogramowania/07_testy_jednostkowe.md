
## Testy jednostkowe

Testy jednostkowe są ważnym narzędziem w procesie tworzenia oprogramowania, ponieważ pomagają zapewnić, że nasz kod działa poprawnie i jest odporny na błędy. Pozwalają również na szybkie wykrycie błędów, które pojawiły się w wyniku zmian w kodzie, dzięki czemu możemy je szybko naprawić. 

* Czerwone testy, czyli testy, które nie przeszły, pokazują, że coś, co działało wcześniej, aktualnie nie działa. Może to być spowodowane tym, że została wprowadzona jakaś zmiana w kodzie, która spowodowała, że test nie zadziałał poprawnie. Czerwone testy są sygnałem, że coś jest nie tak i konieczne jest przeanalizowanie kodu i znalezienie przyczyny problemu.
* Zielone testy, czyli testy, które przeszły, pokazują, że to, co było sprawdzane w testach działa poprawnie. Nie oznacza to jednak, że cały program działa poprawnie - mogą być jeszcze inne fragmenty kodu, które nie zostały sprawdzone w testach i które mogą działać niepoprawnie. Zielone testy są ważne, ponieważ pozwalają upewnić się, że kod działa zgodnie z założeniami, ale nie są wystarczające do całkowitego zabezpieczenia aplikacji przed błędami.

Ogólnie w Pythonie mamy dwie popularne biblioteki służące do testów jednostkowych: <code>unittest</code> i <code>pytest</code>. Obie biblioteki, dają nam możliwość tworzenia testów jednostkowych i uruchamiania ich automatycznie, co pozwala na skupienie się na kodowaniu i uniknięcie ręcznego testowania kodu. Obie biblioteki są dość proste w użyciu i oferują duże możliwości tworzenia i uruchamiania testów. Ostateczny wybór biblioteki zależy od indywidualnych potrzeb i preferencji programisty.

### Unittest

Biblioteka ta została zbudowana zgodnie z filozofią programowania obiektowego, co oznacza, że w kodzie tworzymy klasy i korzystamy z dziedziczenia. Unittest oferuje również wiele funkcji assert, które pozwalają na sprawdzenie różnych aspektów działania programu.

Przykład kodu z użyciem unittest:

```python
import unittest

class TestSMTP(unittest.TestCase):
    
    def smtp_connection(self):
    import smtplib
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

    def test_helo(self):
    response_code, msg = self.smtp_connection().ehlo()
    self.assertEqual(response_code, 250)
```

W powyższym przykładzie tworzymy klasę TestSMTP, która dziedziczy po klasie TestCase z biblioteki unittest. W tej klasie zdefiniowaliśmy funkcję smtp_connection, która tworzy połączenie z serwerem SMTP, oraz funkcję test_helo, która wywołuje metodę ehlo na połączeniu SMTP i sprawdza, czy otrzymano oczekiwany kod odpowiedzi (250).

Aby uruchomić testy jednostkowe, wystarczy wywołać odpowiednie polecenie w konsoli: 

```
python -m unittest
```

### Pytest

Pytest to również biblioteka służąca do tworzenia i uruchamiania testów jednostkowych w języku Python. Została zbudowana zgodnie z filozofią "im prościej, tym lepiej", co oznacza, że nie ma w niej klas i dziedziczenia. Pytest pozwala na tworzenie testów poprzez definiowanie funkcji oznaczonych adnotacją @pytest.fixture.

Przykład kodu z użyciem pytest:

```python
import pytest

@pytest.fixture
def smtp_connection():
    import smtplib
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

def test_helo(smtp_connection):
    response_code, msg = smtp_connection.ehlo()
    assert response_code == 250
```

Test składa się z dwóch części: dekoratora <code>@pytest.fixture</code> oraz funkcji testowej <code>test_helo()</code>.

Dekorator <code>@pytest.fixture</code> mówi nam, że funkcja <code>smtp_connection()</code> jest funkcją pomocniczą, która zostanie uruchomiona przed każdą funkcją testową. W tym przypadku <code>smtp_connection()</code> tworzy obiekt <code>SMTP</code> i zwraca go jako wartość. Funkcja ta nie jest testem jednostkowym, ale służy do przygotowania środowiska testowego.

Natomiast funkcja testowa <code>test_helo()</code> jest testem jednostkowym. Funkcja ta przyjmuje jako argument obiekt <code>smtp_connection</code>, który został wcześniej utworzony przez dekorator <code>@pytest.fixture</code>. Funkcja testowa wywołuje na tym obiekcie funkcję <code>ehlo()</code> i sprawdza, czy kod odpowiedzi oraz wiadomość zwracana przez funkcję są takie same, jak oczekiwane wartości. Jeśli tak, to test zostaje zaliczony, w przeciwnym razie test zostaje uznany za nieudany (tzw. "czerwony test").

Aby uruchomić testy jednostkowe, wystarczy wywołać odpowiednie polecenie w konsoli: 

```
pytest
```

### Korzyści z testów jednostkowych

* Pomagają innym programistom zrozumieć cel danego fragmentu kodu produkcyjnego.
* Gdy programy są małe, programista może ręcznie sprawdzić ich działanie z każdą modyfikacją. Wraz ze wzrostem złożoności, ręczne testowanie wszystkich części programu staje się niemożliwe. Testy jednostkowe można uruchomić automatycznie.
* Wymuszają separację zadań między poszczególnymi fragmentami kodu.
* Pozwalają na szybkie sprawdzenie poprawności działania kodu po dokonaniu zmian w kodzie produkcyjnym.

### TDD

Technika "test driven development" (TDD) to sposób pisania programów, w którym testy są pisane przed kodem produkcyjnym. Proces tworzenia programu składa się z trzech etapów:

1. Testy jednostkowe.
2. Kod produkcyjny.
3. Refkatoryzajca kodu produkcyjnego.

Programista nigdy nie przechodzi do implementacji nowych funkcjonalności, dopóki wszystkie trzy etapy nie zostały zakończone dla aktualnie implementowanych funkcjonalności.

### Losowe dane nie mają miejsca w testach

Załóżmy, że masz własną implementację jednego z algorytmów sortowania. Jeśli chcesz porównać wynik jego działania, z wynikiem działania funkcji <code>sorted()</code> z biblioteki standardowej to ręcznie przygotuj listy wejściowe.

```python
import pytest

def test_wlasne_sortowanie():
    lista_a  = [1, 1, 1]
    lista_b = [3, 5, 2]
    lista_c = [-1, 2, 3, -1, 0]
    # import random
    # lista_d = [random.randint(-10, 10) for _ in range(5)] # ZLE
    
    assert wlasne_sortowanie(lista_a) == sorted(lista_a)
    assert wlasne_sortowanie(lista_b) == sorted(lista_b)
    assert wlasne_sortowanie(lista_c) == sorted(lista_c)
```

Powyższy fragment kodu zawiera przykład użycia pytest do testowania funkcji <code>wlasne_sortowanie</code>. W tym przypadku, trzy listy są tworzone jako dane wejściowe: <code>lista_a</code>, <code>lista_b</code> i <code>lista_c</code>. Następnie są one porównywane z oczekiwanymi wynikami po wywołaniu funkcji <code>sorted()</code> na tych samych danych wejściowych za pomocą polecenia <code>assert</code>. Jeśli wynik zwrócony przez <code>wlasne_sortowanie()</code> jest różny od oczekiwanego wyniku, zostanie wygenerowany błąd, który poinformuje o niepowodzeniu testu.

### Od znalezienia buga do poprawnie działającego kodu

Zauważono błąd w twoim programie. Co należy zrobić?

1. Próbuj odtworzyć problematyczną sytuację. Na przykład, jeśli twoja aplikacja zamyka się po wciśnięciu przycisku mającego przenieść użytkownika na inną stronę, najpierw manualnie wykonaj wszystkie kroki prowadzące do pojawienia się niechcianego efektu.
1. Zlokalizuj w kodzie, który fragment jest odpowiedzialny za pojawienie się znalezionego błędu.
1. Dodaj test, który sprawdzi, czy niepożądana sytuacja występuje po wykonaniu zlokalizowanego fragmentu kodu. Na przykład, jeśli błąd pojawia się po wywołaniu funkcji <code>foo()</code>, najpierw znajdź test <code>test_foo()</code> i upewnij się, że funkcja <code>foo()</code> jest wywoływana z parametrami, przy których pojawia się błąd. Dodaj test wykrywający wystąpienie niepożądanej sytuacji. Po uruchomieniu testu otrzymasz czerwony komunikat. 
1. W kolejnym kroku przyjdzie ci naprawić funkcję <code>foo()</code>. Możesz to zrobić na różne sposoby, ale pamiętaj, że celem jest zamienienie czerwonego komunikatu z testu na zielony. Możesz zmienić sposób działania funkcji, zmienić sposób przekazywania argumentów lub wyeliminować jakiś błąd. Ważne, by po zmianach test <code>test_foo()</code> przeszedł pomyślnie.
1. Gdy test przechodzi pomyślnie, możesz przejść do kolejnego etapu, czyli refaktoryzacji kodu. To etap, w którym dbamy o to, by kod był czytelny, elegancki i łatwy do zrozumienia. Może to oznaczać przemianowanie zmiennych, zmianę sposobu ich deklaracji, a nawet usunięcie niepotrzebnych linii kodu. Refaktoryzacja powinna być przeprowadzana zgodnie z zasadami zdrowego rozsądku i nie powinna wpływać na poprawność funkcji.
1. W przyszłości dbaj o to, by test już zawsze pozostał zielony.

### Inne typy testów

* Testy jednostkowe to testy sprawdzające odizolowane jednostki kodu, najczęściej pojedyncze funkcje.
* Testy integracyjne to testy sprawdzające, jak różne elementy systemu współpracują ze sobą.
* Testy całego systemu (end-to-end) to testy sprawdzające, jak system działa jako całość, od wejścia aż do wyjścia.

Ogólnie rzecz biorąc, im mniej testów jednostkowych, tym więcej testów integracyjnych i testów całego systemu jest potrzebnych, aby zapewnić odpowiedni poziom testowania. Ważne jest, aby zachować odpowiedni balans między różnymi typami testów.

Zgodnie z zaleceniami autora <a href="https://www.oreilly.com/library/view/software-engineering-at/9781492082781/">"Software Engineering at Google"</a> testy należy rozdzielić w następujących proporcjach:

* 80% testy jednostkowe
* 15% testy integracyjne
* 5% testy całego systemu (end-to-end)

### Generowanie danych testowych automatycznie

Przy tworzeniu aplikacji, warto również zadbać o skrypty generujące dane testowe, które są potrzebne do pracy aplikacji. Na przykład, jeśli piszesz aplikację komunikującą się z bazą danych MySQL, powinieneś mieć skrypt, który automatycznie utworzy taką bazę danych i wypełni ją przykładowymi danymi. Dzięki temu, podczas pisania kodu, możesz od razu sprawdzić, czy działa on poprawnie, bez konieczności czekania na uruchomienie testów w środowisku produkcyjnym. Ponadto, masz możliwość automatycznego testowania całej aplikacji.

### Organizacja projektu z testami

Aby zachować porządek w projekcie, warto rozdzielić kod produkcyjny i testy jednostkowe do osobnych folderach. W ten sposób łatwiej będzie zarządzać plikami i szybko odnaleźć potrzebne testy.

Przykładowo, struktura projektu może wyglądać następująco:

```bash
projekt
├── przykladowy_pakiet
│   ├── __init__.py
│   └── modul_a.py
│   └── modul_b.py
└── tests
    ├── __init__.py
    └── test_modul_a.py
    └── test_modul_b.py
```

W ten sposób z jednej strony ograniczymy wielkość plików z testami, a z drugiej strony ułatwimy wszystkim życie, gdyż znacznie łatwiej będzie zlokalizować konkretny test.

### Automatyzacja testów

W momencie, gdy nasz projekt zaczyna rosnąć w skali, warto zastanowić się nad automatyzacją testów. Możliwe opcje to użycie narzędzi takich jak <a href="https://travis-ci.org/">Travis CI</a>, <a href="https://jenkins.io/">Jenkins</a>, czy <a href="https://circleci.com/">CircleCI</a>. Dzięki temu każdorazowa zmiana w kodzie źródłowym automatycznie uruchamia wszystkie testy, dzięki czemu mamy pewność, że zmiany nie zepsuły istniejącej funkcjonalności.

Automatyzacja testów to także dobre rozwiązanie, gdy nie chcemy tracić czasu na ręczne wykonywanie testów na wszystkich możliwych platformach i przeglądarkach. W takim przypadku warto zainwestować w narzędzia do testowania aplikacji w różnych przeglądarkach i systemach operacyjnych, takie jak <a href="https://www.selenium.dev/">Selenium</a>.
