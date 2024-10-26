# Moduły i pakiety

W Pythonie moduły i pakiety są elementami umożliwiającymi organizację i strukturyzację kodu. Dzięki nim programy stają się bardziej czytelne, łatwiejsze w utrzymaniu i skalowalne. Ułatwiają one zarządzanie dużymi projektami oraz współpracę z innymi programistami. Zrozumienie tych elementów jest niezbędne dla efektywnego programowania i utrzymania czystego, modularnego kodu.

## Moduły

Moduł to podstawowy sposób organizacji kodu. Jest to pojedynczy plik z rozszerzeniem `.py`, który może zawierać definicje funkcji, klas, zmiennych, a także kod wykonywalny. Moduły pozwalają na podzielenie kodu na mniejsze, logiczne części, co ułatwia zarządzanie i ponowne użycie kodu w innych projektach. Dzięki modułom możemy łatwo organizować nasz kod i unikać powielania funkcji, a także dzielić się nimi z innymi.

### **Przykład prostego modułu:**

Utwórz plik o nazwie `matematyka.py` z następującą zawartością:

```python
# matematyka.py

def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

PI = 3.1415
```

W tym module:

- `dodaj(a, b)` - funkcja, która zwraca sumę dwóch liczb.
- `odejmij(a, b)` - funkcja, która zwraca różnicę między dwiema liczbami.
- `PI` - zmienna przechowująca wartość liczby Pi z dokładnością do czterech miejsc po przecinku.

Moduł `matematyka.py` jest teraz samodzielnym plikiem, który możemy zaimportować do innych skryptów, aby wykorzystać jego funkcje i zmienne.

### Importowanie modułów

Aby skorzystać z funkcji i zmiennych z modułu `matematyka.py` w innym pliku, możemy go zaimportować za pomocą instrukcji `import`. Dzięki temu możemy używać wszystkich funkcji i zmiennych, które znajdują się w module, odwołując się do nich przez nazwę modułu.

### **Przykład użycia modułu:**

```python
# main.py

import matematyka

wynik = matematyka.dodaj(5, 7)
print(wynik)  # Output: 12

print(matematyka.PI)  # Output: 3.1415
```

W tym przykładzie:

- `import matematyka` wczytuje cały moduł `matematyka`, co pozwala nam na korzystanie z jego funkcji i zmiennych.
- Aby odwołać się do funkcji `dodaj` lub zmiennej `PI`, używamy prefiksu `matematyka.`.
- Dzięki temu unikamy potencjalnych konfliktów nazw, ponieważ wszystkie elementy modułu są wywoływane przez prefiks `matematyka`.

### Importowanie konkretnych elementów

Zamiast importować cały moduł, możemy importować tylko konkretne funkcje lub zmienne, co sprawia, że kod staje się bardziej zwięzły i czytelny. Dzięki temu nie musimy używać prefiksu modułu za każdym razem.

### **Przykład:**

```python
from matematyka import dodaj, PI

wynik = dodaj(10, 15)
print(wynik)  # Output: 25

print(PI)  # Output: 3.1415
```

W tym przypadku:

- `from matematyka import dodaj, PI` pozwala nam zaimportować tylko wybrane elementy z modułu `matematyka`.
- Dzięki temu możemy bezpośrednio wywołać funkcję `dodaj` oraz uzyskać dostęp do zmiennej `PI`, bez konieczności używania prefiksu `matematyka.`.

### Aliasowanie modułów i funkcji

Czasami nazwa modułu lub funkcji może być długa lub może powodować konflikt nazw z innymi elementami w kodzie. W takich przypadkach możemy nadać alias (inną nazwę) modułowi lub funkcji, co ułatwia ich używanie.

### **Przykład aliasowania modułu:**

```python
import matematyka as mat

wynik = mat.odejmij(10, 5)
print(wynik)  # Output: 5
```

Tutaj:

- `import matematyka as mat` oznacza, że moduł `matematyka` jest dostępny pod krótszą nazwą `mat`.
- Teraz możemy odwoływać się do funkcji i zmiennych tego modułu, używając prefiksu `mat`, co może być bardziej wygodne.

### **Przykład aliasowania funkcji:**

```python
from matematyka import dodaj as d

wynik = d(3, 4)
print(wynik)  # Output: 7
```

W tym przypadku:

- `from matematyka import dodaj as d` pozwala nam zaimportować funkcję `dodaj` i przypisać jej nazwę `d`.
- Dzięki temu możemy wywołać funkcję jako `d(3, 4)`, co jest krótsze i może być bardziej czytelne w niektórych kontekstach.

### Korzyści z używania modułów

- Funkcje i klasy z modułu mogą być używane w wielu programach.
- Podział kodu na moduły sprawia, że jest on bardziej czytelny i łatwiejszy w nawigacji.
- Moduły mają własną przestrzeń nazw, co pomaga w uniknięciu konfliktów.

## Pakiety

Pakiet to struktura, która umożliwia grupowanie powiązanych modułów w jednym katalogu. Dzięki pakietom możemy organizować kod na wyższym poziomie niż przy użyciu pojedynczych modułów, co jest szczególnie przydatne w większych projektach. Pakiet to po prostu folder, który zawiera moduły (pliki `.py`) oraz specjalny plik `__init__.py`. Obecność pliku `__init__.py` informuje Pythona, że dany folder powinien być traktowany jako pakiet, co pozwala na jego importowanie w innych częściach programu.

### **Struktura pakietu:**

```
projekt/
├── kalkulator/
│   ├── __init__.py
│   ├── arytmetyka.py
│   └── geometry.py
└── main.py
```

- `kalkulator/` - katalog, który pełni rolę pakietu. Zawiera moduły związane z obliczeniami matematycznymi.
- `__init__.py` - plik specjalny, który sprawia, że Python rozpoznaje katalog `kalkulator` jako pakiet. Może być pusty, ale często zawiera kod inicjalizacyjny lub importy.
- `arytmetyka.py` - moduł w pakiecie, który może zawierać funkcje do operacji arytmetycznych (np. dodawanie, odejmowanie).
- `geometry.py` - moduł w pakiecie, który może zawierać funkcje związane z obliczeniami geometrycznymi (np. pole powierzchni, obwód).

### Tworzenie pakietu

Aby utworzyć pakiet, wykonaj następujące kroki:

1. **Stwórz folder o nazwie pakietu** - np. `kalkulator`, który będzie zawierał wszystkie moduły powiązane z tym pakietem.
2. **Utwórz plik `__init__.py` wewnątrz katalogu** - może być pusty lub zawierać kod, który będzie wykonywany podczas importowania pakietu.
3. **Dodaj moduły (pliki `.py`) do katalogu pakietu** - umieść tam pliki, takie jak `arytmetyka.py` czy `geometry.py`.

### **Przykład modułu w pakiecie:**

W pliku `arytmetyka.py` możemy zdefiniować podstawowe operacje matematyczne:

```python
# arytmetyka.py

def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b
```

W tym przykładzie:

- Funkcja `dodaj(a, b)` zwraca sumę dwóch liczb.
- Funkcja `odejmij(a, b)` zwraca różnicę między dwiema liczbami.
- Moduł `arytmetyka.py` może być zaimportowany do innych części projektu, aby korzystać z tych funkcji.

### Importowanie modułów z pakietu

Aby skorzystać z funkcji i klas zawartych w modułach pakietu, używamy notacji kropkowej (`.`). Możemy zaimportować cały moduł z pakietu, a następnie odwoływać się do jego zawartości za pomocą prefiksu modułu.

### **Przykład importowania modułu z pakietu:**

```python
# main.py

from kalkulator import arytmetyka

wynik = arytmetyka.dodaj(2, 3)
print(wynik)  # Output: 5
```

W tym przykładzie:

- `from kalkulator import arytmetyka` importuje moduł `arytmetyka` z pakietu `kalkulator`.
- Następnie wywołujemy funkcję `dodaj` z modułu `arytmetyka` używając notacji `arytmetyka.dodaj`.
- Dzięki temu możemy korzystać z funkcji modułu bez konieczności pisania całej ścieżki do pliku.

### Importowanie konkretnych funkcji z modułu w pakiecie

Jeżeli chcemy zaimportować tylko wybrane funkcje lub klasy z modułu, możemy to zrobić bezpośrednio, co sprawia, że kod staje się bardziej zwięzły.

### **Przykład:**

```python
from kalkulator.arytmetyka import odejmij

wynik = odejmij(10, 4)
print(wynik)  # Output: 6
```

W tym przypadku:

- `from kalkulator.arytmetyka import odejmij` importuje tylko funkcję `odejmij` z modułu `arytmetyka` w pakiecie `kalkulator`.
- Dzięki temu możemy bezpośrednio wywoływać funkcję `odejmij` bez potrzeby używania prefiksu `arytmetyka.`.

### Używanie pliku `__init__.py`

Plik `__init__.py` w pakiecie pełni kilka ważnych funkcji:

- Możemy w nim umieścić kod, który powinien być wykonany podczas pierwszego importu pakietu.
- Używając zmiennej `__all__`, możemy kontrolować, które moduły są importowane, gdy ktoś użyje `from pakiet import *`.
- Możemy zdefiniować, które moduły mają być widoczne na zewnątrz pakietu, a które powinny pozostać ukryte.

### **Przykład `__init__.py`:**

```python
# __init__.py

__all__ = ['arytmetyka', 'geometry']
```

Dzięki powyższemu ustawieniu:

- Jeśli ktoś użyje `from kalkulator import *`, zaimportowane zostaną tylko moduły `arytmetyka` i `geometry`.
- Moduły, które nie są wymienione w `__all__`, nie zostaną automatycznie zaimportowane, co pomaga w zarządzaniu widocznością zawartości pakietu.

### **Przykład użycia `from pakiet import *`:**

```python
# main.py

from kalkulator import *

wynik = arytmetyka.dodaj(5, 5)
print(wynik)  # Output: 10
```

W tym przypadku:

- `from kalkulator import *` zaimportuje moduły `arytmetyka` i `geometry`, ponieważ są one wymienione w `__all__` pliku `__init__.py`.
- Następnie możemy bezpośrednio używać funkcji z tych modułów.

## Importowanie modułów i pakietów

Importowanie modułów i pakietów w Pythonie jest kluczowe dla efektywnego zarządzania przestrzenią nazw i unikania duplikacji kodu. Oto różne metody importowania:

### Zaimportowanie całego modułu

Pozwala to na dostęp do wszystkich funkcji, klas i zmiennych w module, używając notacji z kropką.

**Przykład:**

```python
import os

current_directory = os.getcwd()
print(current_directory)
```

### Zaimportowanie modułu z aliasem

Umożliwia korzystanie z krótszej nazwy modułu w kodzie.

**Przykład:**

```python
import numpy as np

array = np.array([1, 2, 3])
print(array)
```

### Zaimportowanie konkretnych funkcji z modułu

Importuje tylko określone funkcje lub klasy.

**Przykład:**

```python
from math import sqrt, pi

print(sqrt(16))  # Output: 4.0
print(pi)        # Output: 3.141592653589793
```

### Zaimportowanie funkcji z aliasem

Pozwala na zmianę nazwy importowanej funkcji.

**Przykład:**

```python
from math import factorial as fac

print(fac(5))  # Output: 120
```

### Zaimportowanie całej zawartości modułu

Importuje wszystkie publiczne elementy modułu.

**Przykład:**

```python
from random import *

print(randint(1, 10))
```

**Uwaga:** Ta metoda może prowadzić do konfliktów nazw i jest ogólnie odradzana.

## Wykonywanie kodu podczas importowania

W Pythonie kod znajdujący się poza definicjami funkcji i klas w module jest wykonywany natychmiast podczas importowania tego modułu. Oznacza to, że jeśli w module znajdują się instrukcje, które nie są umieszczone w funkcjach lub klasach, zostaną one wykonane, gdy tylko zaimportujemy moduł w innym pliku. Może to prowadzić do nieoczekiwanych efektów, takich jak wywoływanie funkcji lub drukowanie komunikatów, których nie planowaliśmy podczas importu.

### **Przykład problematycznego modułu:**

Załóżmy, że mamy moduł `misja.py` z następującą zawartością:

```python
# misja.py

def przygotuj_misje():
    print("Przygotowanie misji...")

def start_misji():
    print("Start misji!")

start_misji()  # Ta funkcja zostanie wywołana podczas importowania
```

W tym przykładzie:

- Funkcja `start_misji()` jest wywoływana bezpośrednio w module, poza definicjami funkcji.
- Kiedy zaimportujemy ten moduł w innym pliku, kod znajdujący się poza funkcjami zostanie wykonany automatycznie.

### **Importowanie modułu:**

Jeśli teraz zaimportujemy moduł `misja` w innym pliku:

```python
import misja
```

To w konsoli zostanie wyświetlone:

```
Start misji!
```

Dzieje się tak dlatego, że Python wykonuje kod umieszczony poza definicjami funkcji natychmiast podczas importowania modułu. W tym przypadku nie chcieliśmy, aby funkcja `start_misji()` została uruchomiona podczas importu — powinna być wywoływana tylko wtedy, gdy rzeczywiście tego chcemy.

### Rozwiązanie problemu

Aby uniknąć niechcianego wykonywania kodu podczas importowania, używamy konstrukcji:

```python
if __name__ == "__main__":
    # Kod, który zostanie wykonany tylko przy bezpośrednim uruchomieniu modułu
```

Dzięki tej konstrukcji możemy określić, które fragmenty kodu mają być uruchamiane tylko wtedy, gdy moduł jest uruchamiany jako główny program, a nie podczas jego importowania.

### **Poprawiony moduł:**

```python
# misja.py

def przygotuj_misje():
    print("Przygotowanie misji...")

def start_misji():
    print("Start misji!")

if __name__ == "__main__":
    start_misji()
```

W tym przykładzie:

- Kod `if __name__ == "__main__":` sprawia, że funkcja `start_misji()` zostanie uruchomiona tylko wtedy, gdy moduł `misja.py` zostanie uruchomiony bezpośrednio jako skrypt, a nie podczas importowania go w innym pliku.
- Teraz, gdy zaimportujemy moduł `misja` w innym pliku, funkcja `start_misji()` nie zostanie wywołana automatycznie, co eliminuje niepożądane efekty.

### Wyjaśnienie działania `if __name__ == "__main__":`

- **`__name__`:** To specjalna zmienna, która jest automatycznie ustawiana przez Pythona. Jej wartość zależy od tego, w jaki sposób uruchamiany jest moduł:
- Jeżeli moduł jest uruchamiany bezpośrednio jako główny skrypt (np. `python misja.py`), wówczas `__name__` przyjmuje wartość `"__main__"`.
- Jeżeli moduł jest importowany w innym pliku, `__name__` przyjmuje nazwę tego modułu (np. `"misja"`).
- **Konstrukcja `if __name__ == "__main__":`** umożliwia nam określenie, które fragmenty kodu mają być uruchamiane tylko wtedy, gdy moduł jest uruchamiany bezpośrednio jako skrypt. Pozwala to na oddzielenie kodu testowego lub przykładów użycia od kodu, który powinien być dostępny po zaimportowaniu modułu.

### **Przykład zastosowania:**

```python
# narzedzia.py

def testuj_funkcje():
    print("Testowanie funkcji...")

if __name__ == "__main__":
    testuj_funkcje()
```

W tym module:

- Funkcja `testuj_funkcje()` zostanie wywołana tylko wtedy, gdy uruchomimy skrypt `narzedzia.py` bezpośrednio z linii poleceń.
- Gdy `narzedzia.py` jest importowane w innym skrypcie, kod w bloku `if __name__ == "__main__":` nie zostanie wykonany.

### **Uruchamianie `narzedzia.py` bezpośrednio:**

Jeśli uruchomimy plik `narzedzia.py` bezpośrednio z linii poleceń:

```
python narzedzia.py
```

To na wyjściu zobaczymy:

```
Testowanie funkcji...
```

Ponieważ w tym przypadku `__name__` przyjmuje wartość `"__main__"`, kod w bloku `if __name__ == "__main__":` zostaje wykonany.

### **Importowanie `narzedzia.py` w innym pliku:**

Jeśli zaimportujemy `narzedzia.py` w innym pliku:

```python
# main.py

import narzedzia
```

Nie zobaczymy żadnego komunikatu w konsoli, ponieważ kod w bloku `if __name__ == "__main__":` nie zostanie wykonany — `__name__` w module `narzedzia` nie ma wartości `"__main__"` podczas importu.

## Importowanie relatywne i absolutne

W Pythonie możemy importować moduły i funkcje na dwa główne sposoby: za pomocą importów absolutnych oraz względnych. Obie metody mają swoje zastosowania i są wybierane w zależności od struktury projektu oraz potrzeb programisty.

### Importy absolutne

Importy absolutne odwołują się do modułów, używając ich pełnej ścieżki, poczynając od katalogu głównego projektu. Oznacza to, że określamy dokładnie, skąd ma pochodzić importowany moduł, bez względu na to, w którym miejscu struktury katalogów znajduje się plik, który wykonuje import.

**Przykład importu absolutnego:**

```python
from kalkulator.arytmetyka import dodaj
```

W tym przykładzie:
- `from kalkulator.arytmetyka import dodaj` wskazuje, że funkcja `dodaj` powinna zostać zaimportowana z modułu `arytmetyka`, który znajduje się w pakiecie `kalkulator`.
- Ścieżka do modułu `arytmetyka` jest podana w sposób pełny, poczynając od katalogu `kalkulator`.

Zaletą importów absolutnych jest to, że są one jasne i czytelne – widać dokładnie, z którego modułu pochodzi import. Dzięki temu łatwiej jest zrozumieć strukturę projektu, zwłaszcza gdy jest on duży i zawiera wiele pakietów.

### Importy względne

Importy względne odwołują się do modułów na podstawie ich położenia względem bieżącego modułu, w którym wykonujemy import. Są przydatne, gdy chcemy odwołać się do modułów, które znajdują się w tym samym pakiecie lub w pokrewnych pakietach. W przypadku importów względnych używamy kropek (`.`) do wskazania położenia modułów:

- Jedna kropka (`.`) odnosi się do bieżącego pakietu.
- Dwie kropki (`..`) odnoszą się do jednego poziomu wyżej, czyli do pakietu nadrzędnego.

**Przykład importu względnego:**

```python
from .arytmetyka import dodaj  # Importuje funkcję dodaj z modułu arytmetyka w bieżącym pakiecie
```

W tym przykładzie:
- `from .arytmetyka import dodaj` wskazuje, że funkcja `dodaj` jest importowana z modułu `arytmetyka`, który znajduje się w tym samym pakiecie co bieżący plik.
- Użycie jednej kropki (`.`) sprawia, że odwołujemy się do modułu `arytmetyka` w ramach tego samego pakietu.

Importy względne są szczególnie przydatne w dużych projektach, w których moduły są zorganizowane w hierarchiczne struktury pakietów. Pozwalają one na łatwe przenoszenie całych pakietów bez konieczności zmieniania ścieżek importu, co ułatwia refaktoryzację kodu.

### **Uwaga:** Ograniczenia importów względnych

- Importy względne można stosować **tylko wewnątrz pakietów**. Oznacza to, że działają one poprawnie jedynie wtedy, gdy moduł, w którym używamy importu względnego, jest częścią pakietu.
- Importy względne **nie działają w skryptach uruchamianych bezpośrednio**, czyli takich, które są uruchamiane jako główny plik programu (np. za pomocą `python skrypt.py`). W takim przypadku Python nie wie, w jakim kontekście należy interpretować kropki w importach względnych.

### Przykład sytuacji, kiedy import względny może nie działać:

Jeżeli mamy strukturę katalogów:

```
projekt/
├── kalkulator/
│   ├── __init__.py
│   ├── arytmetyka.py
│   └── geometry.py
└── main.py
```

i w pliku `arytmetyka.py` znajduje się import względny:

```python
# arytmetyka.py

from .geometry import oblicz_pole
```

To ten import będzie działał, gdy `arytmetyka.py` zostanie zaimportowany jako część pakietu `kalkulator`, na przykład w `main.py`:

```python
# main.py

from kalkulator import arytmetyka
```

Ale jeśli spróbujemy uruchomić `arytmetyka.py` bezpośrednio:

```
python kalkulator/arytmetyka.py
```

otrzymamy błąd, ponieważ importy względne nie działają, gdy plik jest uruchamiany bezpośrednio.

### Kiedy używać importów absolutnych, a kiedy względnych?

**Importy absolutne**:

- Stosuj, gdy chcesz, aby struktura importów była jasna i niezależna od położenia pliku wykonującego import.
- Przydają się, gdy projekt jest złożony, a pełna ścieżka modułów pomaga zrozumieć zależności.
- Są bardziej uniwersalne i działają niezależnie od tego, czy moduł jest uruchamiany bezpośrednio, czy jest importowany.

**Importy względne**:

- Stosuj wewnątrz pakietów, gdy chcesz odwoływać się do modułów na podstawie ich położenia względem bieżącego modułu.
- Ułatwiają przenoszenie całych pakietów bez konieczności zmieniania ścieżek importu.
- Są bardziej podatne na błędy w przypadku refaktoryzacji struktury pakietu lub uruchamiania plików bezpośrednio.

## Dobre praktyki

- Grupy powiązanych funkcji i klas umieszczaj w tym samym module lub pakiecie.
- Używaj opisowych nazw dla modułów i pakietów, pisanych małymi literami.
- Uważaj na nazwy modułów, które mogą kolidować z wbudowanymi modułami Pythona lub popularnymi bibliotekami.
- Dodawaj docstringi do modułów, funkcji i klas, aby ułatwić zrozumienie kodu przez innych programistów.
- Używaj go do inicjalizacji pakietu i kontrolowania, które moduły są eksportowane.
- Unikaj używania `from modul import *`, aby zapobiec konfliktom nazw i poprawić czytelność kodu.

## Praktyczne przykłady

### Tworzenie pakietu `analiza_danych`

W poniższym przykładzie tworzymy pakiet `analiza_danych`, który będzie zawierał moduły odpowiedzialne za różne etapy analizy danych.

**Struktura pakietu:**

```
projekt/
├── analiza_danych/
│   ├── __init__.py
│   ├── wczytywanie.py
│   ├── przetwarzanie.py
│   └── wizualizacja.py
└── main.py
```

- `analiza_danych/` - katalog, który jest traktowany jako pakiet w Pythonie. W nim znajdują się wszystkie pliki odpowiadające za różne funkcjonalności.
- `__init__.py` - plik, który pozwala traktować katalog `analiza_danych` jako pakiet. Zawiera on importy z modułów wewnątrz pakietu.
- `wczytywanie.py` - moduł odpowiedzialny za wczytywanie danych.
- `przetwarzanie.py` - moduł, w którym są zawarte funkcje przetwarzające dane (np. filtrowanie, agregacja).
- `wizualizacja.py` - moduł zajmujący się tworzeniem wykresów i wizualizacją wyników.
- `main.py` - główny skrypt, który korzysta z funkcji dostępnych w pakiecie `analiza_danych`.

### Moduł `wczytywanie.py`

```python
def wczytaj_csv(sciezka):
    # Kod do wczytywania pliku CSV
    pass
```

W module `wczytywanie.py` znajduje się funkcja `wczytaj_csv`, która przyjmuje argument `sciezka`, czyli ścieżkę do pliku CSV, który chcemy wczytać. Ta funkcja mogłaby używać bibliotek takich jak `pandas`, aby załadować dane z pliku do DataFrame'a:

```python
import pandas as pd

def wczytaj_csv(sciezka):
    return pd.read_csv(sciezka)
```

Powyższy kod wczytuje dane z pliku CSV i zwraca je w postaci DataFrame, co jest bardzo wygodne przy dalszej analizie danych.

### Moduł `przetwarzanie.py`

```python
def filtruj_dane(dane):
    # Kod do filtrowania danych
    pass
```

Funkcja `filtruj_dane` w module `przetwarzanie.py` zajmuje się przetwarzaniem danych. Jako argument przyjmuje `dane`, które mogą być np. DataFrame'em wczytanym wcześniej. Przykładowo, możemy chcieć odfiltrować dane na podstawie pewnych warunków:

```python
def filtruj_dane(dane, kolumna, wartosc):
    return dane[dane[kolumna] > wartosc]
```

W tym przykładzie funkcja filtruje wiersze, w których wartość w danej kolumnie jest większa od podanej wartości. Dzięki temu możemy łatwo wybrać tylko te dane, które spełniają określone kryteria.

### Moduł `wizualizacja.py`

```python
def wykres_liniowy(dane):
    # Kod do tworzenia wykresu liniowego
    pass
```

Moduł `wizualizacja.py` zawiera funkcję `wykres_liniowy`, która tworzy wykresy na podstawie dostarczonych danych. Zwykle takie wykresy są generowane za pomocą bibliotek takich jak `matplotlib` lub `seaborn`:

```python
import matplotlib.pyplot as plt

def wykres_liniowy(dane, x, y):
    plt.figure(figsize=(10, 6))
    plt.plot(dane[x], dane[y], marker='o')
    plt.title('Wykres Liniowy')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(True)
    plt.show()
```

W powyższym kodzie funkcja `wykres_liniowy` rysuje wykres, gdzie `x` i `y` to nazwy kolumn, które mają być użyte do osi X i Y. Wykres zostanie wyświetlony za pomocą `matplotlib`.

### Plik `__init__.py`

```python
from .wczytywanie import wczytaj_csv
from .przetwarzanie import filtruj_dane
from .wizualizacja import wykres_liniowy

__all__ = ['wczytaj_csv', 'filtruj_dane', 'wykres_liniowy']
```

Plik `__init__.py` pozwala na łatwy dostęp do funkcji pakietu `analiza_danych` z zewnątrz. Importując te funkcje wewnątrz `__init__.py`, możemy je potem bezpośrednio zaimportować w innych plikach, takich jak `main.py`. `__all__` definiuje listę funkcji, które są dostępne do importu z poziomu pakietu.

### Użycie pakietu w `main.py`

```python
from analiza_danych import wczytaj_csv, filtruj_dane, wykres_liniowy

dane = wczytaj_csv('dane.csv')
dane_przefiltrowane = filtruj_dane(dane, 'kolumna', 100)
wykres_liniowy(dane_przefiltrowane, 'czas', 'wartość')
```

W pliku `main.py` importujemy funkcje `wczytaj_csv`, `filtruj_dane` i `wykres_liniowy` z pakietu `analiza_danych` i używamy ich do przetworzenia danych. 

1. Funkcja `wczytaj_csv` ładuje dane z pliku `dane.csv` do DataFrame'a.
2. Funkcja `filtruj_dane` przefiltrowuje dane, wybierając tylko te, gdzie wartość w kolumnie `'kolumna'` jest większa niż 100.
3. Funkcja `wykres_liniowy` generuje wykres liniowy, pokazując zależność między kolumnami `'czas'` i `'wartość'`.
