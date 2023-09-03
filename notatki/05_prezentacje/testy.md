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

* **Rakieta Ariane 5 ECA (2002)**: Rakieta uległa samozniszczeniu kilka sekund po starcie z powodu błędu w systemie sterującym chłodzeniem.
  
* **Wojna w Zatoce Perskiej (1991)**: Błąd w systemie obrony przeciwrakietowej Patriot spowodował niedokładność przy zaokrąglaniu, co doprowadziło do niezidentyfikowania nadchodzącej rakiety Scud. Ostatecznie atak rakietowy spowodował śmierć 28 amerykańskich żołnierzy. [Więcej informacji](https://www-users.cse.umn.edu/~arnold/455.f96/disasters.html).

Ostatecznie testy mają kluczowe znaczenie dla jakości i bezpieczeństwa oprogramowania. Dlatego inwestowanie w solidne praktyki testowania jest niezbędne dla każdej firmy zajmującej się tworzeniem oprogramowania.

### Proces testowania

Testowanie jest kluczowym etapem w cyklu życia oprogramowania. Oto podstawowe kroki procesu testowania:

1. **Zdefiniuj cel testu**:
    - Określ, jakie zachowanie lub funkcjonalność chcesz przetestować.
    - Ustal spodziewane wyniki.

2. **Przygotuj dane**:
    - Wybierz odpowiednie dane wejściowe i/lub konfigurację programu.
    - W niektórych przypadkach może to obejmować przygotowanie środowiska testowego lub mockowania zewnętrznych zasobów.

3. **Wykonaj test**:
    - Uruchom testowany fragment kodu z przygotowanymi danymi wejściowymi.

4. **Walidacja**:
    - Porównaj faktyczny wynik z oczekiwanym wynikiem.
    - Ustal, czy test przeszedł pomyślnie czy zakończył się niepowodzeniem.

5. **Raportowanie**:
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

1. **Napisz test**: Zanim napiszesz jakikolwiek kod produkcyjny, stworz test jednostkowy dla nowej funkcji lub poprawki.
2. **Uruchom testy**: Wszystkie nowo dodane testy powinny zakończyć się niepowodzeniem, ponieważ jeszcze nie ma dla nich implementacji.
3. **Napisz kod**: Twórz minimalną ilość kodu, która pozwoli testom przejść.
4. **Uruchom wszystkie testy**: Upewnij się, że wszystkie testy, zarówno stare, jak i nowe, przechodzą pomyślnie.
5. **Refaktoryzacja**: Dąż do poprawy i uproszczenia kodu, dbając o jego jakość i zachowując zielony stan testów.

Korzyści z TDD:

- **Zwiększona jakość kodu**: Testy tworzone przed implementacją zmuszają do dokładnego przemyślenia rozwiązania.
- **Wczesne wykrywanie błędów**: Błędy są identyfikowane i korygowane natychmiast po ich wprowadzeniu.
- **Samodzielna dokumentacja**: Testy pokazują, jak dana funkcja powinna działać i co robi.
- **Ułatwia refaktoryzację**: Możliwość modyfikacji kodu z pewnością, że nie wprowadzi to nowych błędów.

Potencjalne wyzwania:

- **Krzywa uczenia**: TDD może być trudne do opanowania, zwłaszcza dla początkujących programistów.
- **Większy początkowy nakład czasowy**: Tworzenie testów przed implementacją może wydłużyć czas tworzenia funkcji, jednak zwykle skraca czas potrzebny na późniejsze debugowanie.
- **Nie dla wszystkiego**: W pewnych sytuacjach, jak np. prototypowanie, TDD może nie być optymalnym rozwiązaniem.
