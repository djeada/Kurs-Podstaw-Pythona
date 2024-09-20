## Testy

Testy w kontekście inżynierii oprogramowania odnoszą się do procesu weryfikacji i walidacji kodu, aby zapewnić, że działa on zgodnie z oczekiwaniami i spełnia określone wymagania. Testy pomagają w wykrywaniu błędów i niespójności, które mogą prowadzić do nieprawidłowego działania oprogramowania.

### Klasyfikacja testów

W zależności od zakresu i celu testowania można wyróżnić różne rodzaje testów:

#### Testy jednostkowe (Unit Tests)

- Skupiają się na pojedynczym fragmencie kodu, np. funkcji lub metodzie.
- Służą do sprawdzenia poprawności działania poszczególnych elementów kodu w izolacji.
- Są zazwyczaj pisane przez deweloperów.

#### Testy integracyjne (Integration Tests)

- Testują interakcje pomiędzy różnymi fragmentami oprogramowania.
- Mogą sprawdzać, jak różne moduły lub usługi współpracują ze sobą.

#### Testy systemowe (System Tests)

- Testują kompletny, zintegrowany system, aby ocenić czy spełnia on określone wymagania.
- Sprawdzają działanie systemu jako całości, w tym interakcje z zewnętrznymi systemami.

#### Testy akceptacyjne (Acceptance Tests)

- Mają na celu potwierdzenie, czy system spełnia oczekiwania użytkowników końcowych i biznesowych.
- Mogą być prowadzone przez zespoły QA, klienta lub użytkowników.

### Przykłady bugów prowadzących do katastrof

Błędy w oprogramowaniu mogą prowadzić do poważnych konsekwencji, zwłaszcza gdy dotyczą krytycznych systemów, takich jak lotnictwo czy obrona.

- **Rakieta Ariane 5 ECA (2002)** uległa samozniszczeniu kilka sekund po starcie z powodu błędu w systemie sterującym chłodzeniem, co doprowadziło do katastrofy.
- W czasie **Wojny w Zatoce Perskiej (1991)** błąd w systemie obrony przeciwrakietowej Patriot, wynikający z niedokładności przy zaokrąglaniu, uniemożliwił zidentyfikowanie nadlatującej rakiety Scud. W efekcie atak rakietowy zakończył się śmiercią 28 amerykańskich żołnierzy. [Więcej informacji](https://www-users.cse.umn.edu/~arnold/455.f96/disasters.html).

Ostatecznie testy mają kluczowe znaczenie dla jakości i bezpieczeństwa oprogramowania. Dlatego inwestowanie w solidne praktyki testowania jest niezbędne dla każdej firmy zajmującej się tworzeniem oprogramowania.

### Proces testowania

Testowanie jest kluczowym etapem w cyklu życia oprogramowania. Oto podstawowe kroki procesu testowania:

I. **Zdefiniuj cel testu**:
   
- Określ, jakie zachowanie lub funkcjonalność chcesz przetestować.
- Ustal spodziewane wyniki.

II. **Przygotuj dane**:

- Wybierz odpowiednie dane wejściowe i/lub konfigurację programu.
- W niektórych przypadkach może to obejmować przygotowanie środowiska testowego lub mockowania zewnętrznych zasobów.

III. **Wykonaj test**:

- Uruchom testowany fragment kodu z przygotowanymi danymi wejściowymi.

IV. **Walidacja**:

- Porównaj faktyczny wynik z oczekiwanym wynikiem.
- Ustal, czy test przeszedł pomyślnie czy zakończył się niepowodzeniem.

V. **Raportowanie**:

- Zapisz wynik testu, w tym wszelkie znalezione błędy lub nieprawidłowości.
- Ustal dalsze kroki, takie jak naprawa błędów lub przeprowadzenie dalszych testów.

### Testy jednostkowe

* Testy jednostkowe skupiają się na **indywidualnych jednostkach** kodu, takich jak funkcje, metody lub klasy.
* Mają na celu zapewnienie, że każda jednostka działa poprawnie **w izolacji**.
* Są **szybkie** w wykonaniu, co pozwala deweloperom na szybkie wykrywanie błędów.
* Dobre testy jednostkowe nie powinny zależeć od wewnętrznej implementacji kodu, ale tylko od jego interfejsu.
* Zapewniają wsparcie dla **refaktoryzacji**, umożliwiając bezpieczne wprowadzanie zmian w kodzie.

### Przykład Testu

Załóżmy, że chcemy przetestować funkcję `znajdz_klucz(lista, klucz)`, która zwraca indeks pierwszego wystąpienia klucza w liście lub `-1`, jeśli klucz nie występuje.

Przeprowadzamy następujące testy:

1. **Podstawowe zachowanie**: Sprawdzenie, czy funkcja zwraca oczekiwany indeks dla przypadku, gdy klucz znajduje się w liście.
2. **Skrajne przypadki**: Sprawdzenie, czy funkcja zwraca `-1`, gdy klucz nie znajduje się w liście.

```python
def test_find_key():
    assert find_key([1,2,3,4,5], 3) == 2  # Podstawowe zachowanie
    assert find_key([1,2,3,4,5], 6) == -1  # Skrajny przypadek
```

Pamiętaj, aby testować różne przypadki, w tym przypadki skrajne oraz możliwe błędy na poziomie brzegowym, aby zapewnić skuteczność testów.

### Pokrycie kodu produkcyjnego (code coverage)

Pokrycie kodu to wskaźnik ilustrujący, jaki procent kodu źródłowego został uruchomiony podczas testów. Choć wysoki wskaźnik pokrycia jest pożądany, nie zawsze gwarantuje pełną jakość testów.

Przykład:

```python
#1# def fun(a, b):
#2#   a += 1
#3#   b += 2
#4#   if a + b > 22:
#5#     a += 1
#6#   return a + b
```

Przeprowadzając testy fun(a,b), jeżeli pominiemy dane powodujące spełnienie warunku w linii #4#, nie osiągniemy 100% pokrycia. Dodając odpowiednie przypadki testowe, zbliżymy się do pełnego pokrycia.

### Czy zielone testy są gwarancją poprawności?

Samo istnienie zielonych testów (testy, które zakończyły się sukcesem) nie gwarantuje oprogramowania wolnego od błędów.

- Niepełne pokrycie: nawet jeśli wszystkie testy przechodzą, mogą istnieć nieprzetestowane ścieżki kodu.
- Za małe zestawy danych: testy mogą przechodzić dla małych danych, ale zawodzić dla dużych zbiorów.
- Zewnętrzne przypadki: jak w przykładzie z systemem Klarna, który miał wyciek danych pomimo zielonych testów. [Czytaj więcej](https://www.klarna.com/se/blogg/detailed-incident-report-incorrect-cache-configuration-leading-to-klarna-app-exposing-personal-information/).

### Test Driven Development (TDD)

Test Driven Development (TDD) to metoda tworzenia oprogramowania, w której programista najpierw tworzy testy jednostkowe opisujące oczekiwaną funkcjonalność, a następnie pisze kod, który te testy spełnia. TDD pomaga zapewnić wysoką jakość kodu oraz wcześnie wykrywać potencjalne błędy.

Proces TDD:

- Na początku należy **napisać test**, zanim stworzy się jakikolwiek kod produkcyjny, opracowując test jednostkowy dla nowej funkcji lub poprawki.
- Kolejnym krokiem jest **uruchomienie testów**, przy czym nowo dodane testy powinny początkowo zakończyć się niepowodzeniem, ponieważ nie ma jeszcze dla nich odpowiedniej implementacji.
- Następnie należy **napisać kod**, tworząc minimalną ilość kodu wymaganą do przejścia testów.
- Po napisaniu kodu trzeba **uruchomić wszystkie testy**, aby upewnić się, że zarówno nowe, jak i stare testy przechodzą pomyślnie.
- Ostatnim krokiem jest **refaktoryzacja**, czyli poprawa i uproszczenie kodu bez wpływu na działanie testów, dbając o jego jakość.

Korzyści z TDD:

- **Zwiększona jakość kodu** wynika z tego, że testy tworzone przed implementacją zmuszają programistę do dokładnego przemyślenia rozwiązania.
- Dzięki TDD możliwe jest **wczesne wykrywanie błędów**, ponieważ są one identyfikowane i naprawiane natychmiast po ich wprowadzeniu.
- **Samodzielna dokumentacja** to dodatkowa korzyść, ponieważ testy pokazują, jak dana funkcja powinna działać i jakie jest jej przeznaczenie.
- TDD **ułatwia refaktoryzację**, ponieważ umożliwia modyfikację kodu z pewnością, że zmiany nie wprowadzą nowych błędów.

Potencjalne wyzwania:

- **Krzywa uczenia** w TDD może być stroma, zwłaszcza dla początkujących programistów, którzy mogą mieć trudności z opanowaniem tej techniki.
- **Większy początkowy nakład czasowy** jest często potrzebny na tworzenie testów przed implementacją, choć to może skrócić czas potrzebny na późniejsze debugowanie.
- TDD **nie jest optymalne dla wszystkiego**, zwłaszcza w sytuacjach takich jak prototypowanie, gdzie szybka iteracja ma pierwszeństwo przed testowaniem.
