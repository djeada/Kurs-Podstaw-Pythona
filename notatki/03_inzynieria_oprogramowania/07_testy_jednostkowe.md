## Testy jednostkowe

Testy jednostkowe stanowią kluczowy element w procesie wytwarzania oprogramowania, mając na celu weryfikację indywidualnych fragmentów kodu (zazwyczaj funkcji lub metod). Pozwalają programiście mieć pewność, że napisane przez niego komponenty działają zgodnie z oczekiwaniami oraz pomagają w identyfikacji i naprawie błędów na wczesnym etapie. 

#### Czerwone testy  

- Oznaczają testy, które nie przeszły. Jeśli test, który wcześniej działał, staje się czerwony, wskazuje to na potencjalny problem w kodzie.
- Czerwone testy sygnalizują, że coś jest nie tak. Może to być spowodowane wprowadzeniem zmiany, która zakłóciła wcześniejsze działanie kodu.
- W przypadku czerwonych testów należy dokładnie przeanalizować zmiany w kodzie oraz zidentyfikować przyczynę problemu, a następnie naprawić błąd.

#### Zielone testy

- To testy, które przeszły pomyślnie.
- O ile zielone testy są wskaźnikiem poprawności danego fragmentu kodu, nie gwarantują one jednak, że cała aplikacja jest wolna od błędów. Dlatego ważne jest, aby testować różne aspekty kodu i uwzględniać różne scenariusze.
- Zielone testy pozwalają na refaktoryzację kodu, zachowując pewność, że funkcjonalność nie została naruszona.

### Korzyści z testów jednostkowych

- Testy jednostkowe służą jako doskonała dokumentacja. Pozwalają innym programistom zrozumieć, jak dany fragment kodu ma działać oraz jakie są oczekiwane rezultaty jego działania.
- W początkowej fazie projektu możliwe jest ręczne testowanie każdej modyfikacji. Jednak w miarę rosnącej złożoności projektu staje się to bardzo nieefektywne. Testy jednostkowe można łatwo zautomatyzować, co pozwala na sprawdzanie poprawności kodu w sposób szybki i systematyczny.
- Pisanie testów jednostkowych wymusza modularność i separację zadań w kodzie, co prowadzi do bardziej klarownej i zrozumiałej struktury kodu.
- Testy jednostkowe dają pewność, że dokonane zmiany w kodzie nie wprowadziły niechcianych błędów w innych częściach systemu, które były wcześniej już przetestowane.

### TDD (Test Driven Development)

Technika "test driven development" (TDD) to podejście do tworzenia oprogramowania, w którym testy są tworzone przed kodem źródłowym. Proces tworzenia oprogramowania w podejściu TDD jest cykliczny i składa się z trzech głównych etapów:

1. Zanim zostanie napisany jakikolwiek kod, programista tworzy test jednostkowy, który definiuje oczekiwane zachowanie nowej funkcjonalności. Ten krok nazywamy "pisaniem testu". Na tym etapie test nie przechodzi, ponieważ brakuje odpowiedniej implementacji.
2. Następnie programista pisze minimalny kod potrzebny do przejścia testu. Ten krok nazywamy "pisaniem kodu". Celem nie jest tworzenie idealnego rozwiązania, ale napisanie kodu, który sprawi, że test będzie przechodził.
3. Kiedy test przechodzi, programista optymalizuje kod, eliminując redundancje i zapewniając, że struktura kodu jest klarowna i zgodna ze standardami. Ten krok nazywamy "refaktoryzacją".

Korzystanie z TDD pomaga w utrzymaniu czystego kodu, minimalizuje ryzyko błędów i zachęca do myślenia o projektowaniu i architekturze systemu od samego początku procesu tworzenia oprogramowania.

### Organizacja projektu z testami

Dla wielu projektów, zwłaszcza tych większych, odpowiednia organizacja plików i katalogów jest kluczem do utrzymania przejrzystości i efektywności. Rozdzielenie kodu produkcyjnego od testów nie tylko pomaga w zarządzaniu plikami, ale także ułatwia konfigurację narzędzi CI/CD oraz automatyzację testów.

Przykładowa struktura folderów dla projektu z testami może wyglądać tak:

```bash
projekt/
│
├── przykladowy_pakiet/
│   ├── __init__.py
│   ├── modul_a.py
│   └── modul_b.py
│
└── tests/
    ├── __init__.py
    ├── test_modul_a.py
    └── test_modul_b.py
```

Kluczową ideą jest tu utrzymanie logicznej struktury, która odzwierciedla organizację kodu produkcyjnego. Dzięki temu, w miarę rozrostu projektu, łatwo będzie dodawać, modyfikować i lokalizować testy.

### Narzędzia do testów jednostkowych w Pythonie:

W Pythonie istnieją dwie główne biblioteki do pisania i uruchamiania testów jednostkowych:

| **Cecha**                          | **unittest**                                                                            | **pytest**                                                                                           |
|------------------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Typ                                | Standardowa biblioteka w Pythonie do testów jednostkowych                               | Zewnętrzna biblioteka, która stała się bardzo popularna w społeczności Pythona                        |
| Tworzenie testów                   | Umożliwia tworzenie testów, zestawów testów oraz uruchamianie ich                         | Charakteryzuje się prostotą i bardziej naturalnym stylem pisania testów                               |
| Mechanizmy asercji                 | Posiada wbudowane mechanizmy asercji                                                    | Posiada bogatą funkcjonalność w zakresie parametryzacji testów, używania tzw. "fixtures" oraz wtyczek |
| Przygotowanie środowiska testów    | Posiada setup i teardown dla przygotowywania środowiska testów                           | -                                                                                                    |

Ostateczny wybór pomiędzy `unittest` a `pytest` zależy od potrzeb projektu i preferencji zespołu. Niezależnie od wyboru, regularne pisanie i uruchamianie testów jednostkowych jest kluczem do tworzenia niezawodnego oprogramowania.

### Przykład testu unittest

`unittest` to standardowa biblioteka w Pythonie przeznaczona do tworzenia testów jednostkowych. Podąża ona za paradygmatem programowania obiektowego, co oznacza, że testy są organizowane w postaci klas, a mechanizmy takie jak dziedziczenie mogą być wykorzystywane do tworzenia hierarchii testów czy rozszerzania funkcjonalności.

Kluczowe cechy `unittest`:

- Struktura oparta na klasach: każdy zestaw testów to klasa dziedzicząca po `unittest.TestCase`.
- Bogaty zestaw funkcji `assert` do weryfikacji warunków (np. `assertEqual`, `assertTrue`).
- Możliwość definiowania metod `setUp` i `tearDown` do przygotowywania i sprzątania po teście.

Przykład kodu z użyciem `unittest`:

```python
import unittest

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

class TestRomanNumerals(unittest.TestCase):

    def test_conversion(self):
        self.assertEqual(int_to_roman(1), 'I')
        self.assertEqual(int_to_roman(4), 'IV')
        self.assertEqual(int_to_roman(40), 'XL')
        self.assertEqual(int_to_roman(99), 'XCIX')
        self.assertEqual(int_to_roman(1000), 'M')
```

W powyższym przykładzie:

- Funkcja `int_to_roman` konwertuje liczby całkowite na ich reprezentacje w postaci rzymskiej.
- Klasa `TestRomanNumerals` dziedziczy po `unittest.TestCase` i służy do testowania funkcji `int_to_roman`.
- Metoda test_conversion przeprowadza serię testów, sprawdzając różne przypadki konwersji.

Aby uruchomić testy jednostkowe, można użyć następującego polecenia w konsoli:

```python
python -m unittest nazwa_pliku_testowego.py
```

Pamiętaj, by nazwy plików z testami zaczynały się od słowa "test", ponieważ unittest szuka takich plików podczas skanowania katalogów.

### Przykład testu pytest

`pytest` to popularna i wszechstronna biblioteka do tworzenia testów w Pythonie. W porównaniu z `unittest`, `pytest` oferuje bardziej skondensowany i czytelny sposób definiowania testów, eliminując potrzebę tworzenia klas i korzystania z funkcji `assert`. Dodatkowo, `pytest` jest znany ze swojego rozbudowanego wyjścia i możliwości diagnozy, które pomagają w identyfikowaniu i rozwiązywaniu problemów w testach.

Kluczowe cechy `pytest`:

- Testy mogą być definiowane jako proste funkcje, bez potrzeby opakowywania ich w klasach.
- Intuicyjne funkcje asercji - nie trzeba korzystać z metody `assertEqual` ani innych metod specyficznych dla `unittest`. Wystarczy użyć standardowego Pythonowego `assert`.
- Bogaty zestaw wtyczek i integracja z wieloma narzędziami i bibliotekami trzecich stron.
  
Przykład kodu z użyciem `pytest`:

```python
def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

def test_int_to_roman():
    assert int_to_roman(1) == 'I'
    assert int_to_roman(4) == 'IV'
    assert int_to_roman(40) == 'XL'
    assert int_to_roman(99) == 'XCIX'
    assert int_to_roman(1000) == 'M'
```

W powyższym przykładzie:

- Funkcja `int_to_roman` konwertuje liczby całkowite na ich reprezentacje w postaci rzymskiej.
- Funkcja `test_int_to_roman` przeprowadza serię testów, sprawdzając różne przypadki konwersji.

Aby uruchomić testy napisane z użyciem pytest, można użyć następującego polecenia w konsoli:

```python
pytest nazwa_pliku_testowego.py
```

Pamiętaj, by nazwy plików z testami oraz same funkcje testowe zaczynały się od słowa "test", ponieważ pytest szuka takich funkcji/plików podczas skanowania katalogów.

### Od znalezienia buga do poprawnie działającego kodu

Odkrycie błędu w twoim kodzie to dopiero początek drogi. Oto kroki, które warto podjąć, aby odnaleźć i skutecznie naprawić problem:

1. Spróbuj dokładnie odtworzyć sytuację, w której wystąpił błąd. Wiedza o tym, jak i kiedy błąd się pojawia, jest kluczowa, aby zrozumieć jego przyczynę. Na przykład, jeśli twoja aplikacja zamyka się po naciśnięciu pewnego przycisku, zacznij od manualnego przejścia przez wszystkie kroki prowadzące do tego efektu.
2. Odszukaj w kodzie miejsce, które prawdopodobnie odpowiada za zaistniały problem.
3. Utwórz test, który symuluje odnaleziony błąd. Jeśli problem pojawia się po wywołaniu funkcji `foo()`, dodaj lub modyfikuj istniejący test `test_foo()` w taki sposób, aby odzwierciedlał sytuację prowadzącą do błędu. Po uruchomieniu tego testu powinieneś otrzymać czerwony komunikat, informujący o niepowodzeniu testu.
4. Teraz Twoim celem jest modyfikacja kodu tak, aby test przeszedł pomyślnie. Konieczne może być dostosowanie funkcji, zmiana argumentów przekazywanych do funkcji lub wyeliminowanie innych błędów. Pamiętaj, że kluczową sprawą jest to, by po wprowadzeniu zmian test `test_foo()` zakończył się sukcesem.
5. Gdy test już przechodzi, warto zadbać o to, by Twój kod był jak najbardziej optymalny i czytelny. Refaktoryzacja może obejmować zmianę nazw zmiennych, reorganizację kodu czy usuwanie zbędnych fragmentów. Ważne jest jednak, aby w trakcie refaktoryzacji nie wprowadzić nowych błędów - dlatego po każdej większej zmianie warto ponownie uruchomić testy.
6. W przyszłości regularnie uruchamiaj testy, aby upewnić się, że wszystko działa jak należy. Pamiętaj, że każda modyfikacja kodu powinna być poprzedzona aktualizacją lub dodaniem odpowiednich testów. Dzięki temu zapewnisz ciągłość jakości i unikniesz powrotu starych błędów.

### Inne typy testów

W procesie tworzenia oprogramowania wykorzystuje się różne rodzaje testów, aby upewnić się, że system działa prawidłowo na różnych poziomach. Oto trzy główne typy testów:

* **Testy jednostkowe**: Są to testy, które skupiają się na pojedynczych, izolowanych jednostkach kodu, takich jak funkcje czy metody. Mają na celu upewnienie się, że dany fragment kodu działa poprawnie w izolacji.

* **Testy integracyjne**: Te testy koncentrują się na interakcjach między różnymi częściami systemu, takimi jak moduły, komponenty czy serwisy. Ich celem jest sprawdzenie, czy różne elementy aplikacji poprawnie ze sobą współpracują.

* **Testy całego systemu (end-to-end)**: Jak sama nazwa wskazuje, te testy sprawdzają system jako całość, od wejścia do wyjścia. Celem jest upewnienie się, że cały system działa prawidłowo, uwzględniając wszystkie jego składniki.

Optymalne testowanie oprogramowania wymaga odpowiedniego balansu między tymi typami testów. Zbyt mało testów jednostkowych może prowadzić do konieczności intensywniejszego testowania na wyższych poziomach. Według rekomendacji zawartych w książce ["Software Engineering at Google"](https://www.oreilly.com/library/view/software-engineering-at/9781492082781/), proporcje podziału testów powinny być następujące:

* 70-80% testy jednostkowe
* 15-20% testy integracyjne
* 5-10% testy całego systemu (end-to-end)

### Automatyczne generowanie danych testowych

Podczas tworzenia aplikacji niezmiernie ważne jest, aby mieć dostęp do rzetelnych danych testowych. Może to być kluczowe, szczególnie gdy aplikacja wymaga interakcji z bazami danych lub innymi zewnętrznymi źródłami danych. Skrypty generujące dane testowe pozwalają szybko i efektywnie wypełniać system wartościami, które są zbliżone do rzeczywistych. Dzięki temu programiści i testerzy mogą ocenić, jak aplikacja zachowa się w prawdziwym środowisku, bez ryzyka wprowadzenia błędów w produkcji.

### Automatyzacja testów

Automatyzacja testów jest kluczowym elementem współczesnego procesu rozwoju oprogramowania, umożliwiając szybsze wykrywanie błędów i pewność, że wprowadzone zmiany nie wpłynęły negatywnie na istniejącą funkcjonalność. Współczesne narzędzia do automatyzacji testów i integracji ciągłej (CI/CD) umożliwiają nie tylko automatyczne uruchamianie testów, ale także automatyczne wdrażanie aplikacji w odpowiednich środowiskach.

Oto kilka powszechnie używanych narzędzi i platform:

| **Cecha**                  | **Travis CI**                                                                                   | **Jenkins**                                                                                      | **GitLab CI/CD**                                                                                          | **CircleCI**                                                                                                 | **Selenium**                                                                                                   |
|----------------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Typ**                    | Chmurowa usługa CI                                                                              | Narzędzie CI/CD open source                                                                      | Zintegrowany system CI/CD                                                                                   | Chmurowa platforma CI/CD                                                                                    | Narzędzie do testowania aplikacji webowych                                                                   |
| **Integracja z GitHubem**  | Idealna dla projektów hostowanych na GitHubie                                                   | Możliwa                                                                                           | Zintegrowany z GitLabem                                                                                    | Możliwa                                                                                                     | Nie dotyczy                                                                                                   |
| **Konfiguracja**           | Prosta konfiguracja                                                                             | Elastyczna konfiguracja, bogaty ekosystem wtyczek                                                | Definiowanie potoków pracy przy użyciu plików konfiguracyjnych                                             | Automatyczne budowanie, testowanie i wdrażanie aplikacji                                                   | Symulacja interakcji użytkownika, używanie z wieloma językami programowania                                   |
| **Środowisko uruchomieniowe** | Chmura                                                                                         | Lokalny serwer lub chmura                                                                         | GitLab                                                                                                      | Chmura                                                                                                       | Różne przeglądarki                                                                                             |
| **Popularność**            | Często wybierana w projektach open source                                                       | Znane z elastyczności                                                                             | Popularne wśród użytkowników GitLaba                                                                        | Popularne                                                                                                    | Popularne narzędzie do testowania aplikacji webowych                                                         |


