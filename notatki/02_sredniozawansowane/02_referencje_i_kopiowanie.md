## Referencje i kopiowanie

W Pythonie rozróżniamy dwa kluczowe pojęcia: "referencję" oraz "kopiowanie".

- **Referencja** to odwołanie do pewnego obiektu w pamięci.
- **Kopiowanie** polega na tworzeniu nowego obiektu z identyczną zawartością co pierwotny obiekt.

### Referencja – wprowadzenie

Mechanizm referencji jest jednym z podstawowych aspektów pracy z danymi. Zrozumienie, jak działa przekazywanie obiektów do funkcji, przypisywanie ich do zmiennych, czy umieszczanie w strukturach danych takich jak listy lub słowniki, pozwala na uniknięcie wielu potencjalnych błędów. 

Referencje oznaczają, że zmienne nie przechowują bezpośrednio wartości obiektów, lecz wskaźniki (odwołania) do tych obiektów w pamięci. W praktyce, gdy dwie zmienne wskazują na ten sam obiekt, zmiana wprowadzona przez jedną z nich jest widoczna również przy użyciu drugiej. Mechanizm ten dotyczy większości typów złożonych (np. list, słowników, obiektów klas), ale nie prymitywów, takich jak liczby całkowite czy napisy, które są niemutowalne.

**Przykład referencji**

Przeanalizujmy prosty przykład, który ilustruje działanie referencji:

```python
lista = [[1, 2, 3], [4, 5, 6]]
kopia_listy = lista

kopia_listy.append([-1, -2, -3]) # wpłynie na obie listy
kopia_listy[0].insert(1, 1)     # wpłynie również na obie listy
print(lista)  # pokaże zmienioną listę
```

Tutaj obiekt `kopia_listy` jest w rzeczywistości tylko nową referencją do tej samej listy, co `lista`. Dodanie nowego elementu do `kopia_listy` skutkuje zmianą widoczną w `lista`. Zrozumienie tego mechanizmu jest kluczowe do pracy z mutowalnymi typami danych.

### Unikanie niepożądanych efektów – kopiowanie obiektów

W wielu przypadkach chcemy uniknąć sytuacji, w której zmiana w jednym miejscu kodu wpływa na dane w innym miejscu. Można to osiągnąć poprzez kopiowanie obiektów. Python oferuje dwa mechanizmy kopiowania: **płytkie** (shallow copy) i **głębokie** (deep copy).

Różnice między kopiowaniem płytkim a głębokim:

1. **Kopiowanie płytkie** tworzy nową kolekcję (np. listę), ale wewnętrzne elementy tej kolekcji pozostają referencjami do oryginalnych obiektów.
2. **Kopiowanie głębokie** rekurencyjnie kopiuje wszystkie elementy obiektu, tworząc zupełnie nowe, niezależne kopie.

### Kopiowanie płytkie (Shallow Copy)

Kopiowanie płytkie jest szybkie i stosunkowo oszczędne pamięciowo, ale należy być ostrożnym w przypadku struktur wielopoziomowych, takich jak listy zawierające inne listy. Elementy na głębszych poziomach pozostają wspólne dla oryginału i kopii.

**Przykład kopiowania płytkiego**

```python
import copy
lista = [[1, 2, 3], [4, 5, 6]]
kopia_plytka = copy.copy(lista)

kopia_plytka.append([-1, -2, -3])  # wpłynie tylko na `kopia_plytka`
kopia_plytka[0].insert(1, 1)      # wpłynie na obie listy, bo wewnętrzne listy są referencjami
print(lista)  # pokaże częściowo zmienioną listę
```

W tym przykładzie zauważamy, że chociaż dodanie nowego elementu do `kopia_plytka` nie wpływa na `lista`, to modyfikacje wewnętrznych list (`kopia_plytka[0]`) są widoczne w obu miejscach.

### Kopiowanie głębokie (Deep Copy)

Kopiowanie głębokie jest bardziej zasobożerne, ponieważ wymaga stworzenia nowych instancji wszystkich elementów obiektu, ale zapewnia całkowitą niezależność między oryginałem a kopią.

**Przykład kopiowania głębokiego**

```python
import copy
lista = [[1, 2, 3], [4, 5, 6]]
kopia_gleboka = copy.deepcopy(lista)

kopia_gleboka.append([-1, -2, -3])  # wpłynie tylko na `kopia_gleboka`
kopia_gleboka[0].insert(1, 1)      # wpłynie również tylko na `kopia_gleboka`
print(lista)  # pokaże oryginalną listę, bez zmian
```

W powyższym przykładzie każda zmiana w `kopia_gleboka` jest izolowana od `lista`, co sprawia, że obie kolekcje działają zupełnie niezależnie.

### Podsumowanie tematów: referencja, kopiowanie, płytkie, głębokie

Podsumowując, ważne jest, aby być świadomym, czy pracujemy na kopii, czy na oryginalnym obiekcie, a także tego, jakie są konsekwencje naszych działań w kontekście referencji i kopiowania.

| Temat       | Opis                                                                                  | Przykład w Pythonie                   |
|-------------|----------------------------------------------------------------------------------------|---------------------------------------|
| Referencja  | Odwołanie się do tego samego obiektu w pamięci. Zmiany w obiekcie są widoczne w każdej referencji. | `a = [1, 2, 3]; b = a`    |
| Kopiowanie  | Tworzenie nowej kopii obiektu.                                                         |                                       |
| Płytkie     | Kopiowanie tylko najbliższego poziomu struktury. Zagnieżdżone obiekty pozostają współdzielone. | `import copy; b = copy.copy(a)` |
| Głębokie    | Rekurencyjne kopiowanie całej struktury, włącznie z zagnieżdżonymi obiektami.          | `import copy; b = copy.deepcopy(a)` |

### Domyślne wartości parametrów funkcji i ich mutowalność

W Pythonie wartości domyślne dla parametrów funkcji są wyliczane tylko raz w momencie definiowania funkcji, a nie za każdym razem, gdy funkcja jest wywoływana. Oznacza to, że jeśli wartość domyślna jest mutowalna, jak lista lub słownik, wszelkie modyfikacje tej wartości zostaną zachowane między kolejnymi wywołaniami funkcji. Może to prowadzić do nieoczekiwanych efektów ubocznych.

Rozważmy funkcję, która dodaje element do listy. Lista jest parametrem z domyślną wartością `[]`.

#### Przykład niepożądanego zachowania z domyślnymi wartościami parametrów

```python
def dodaj_element(element, lista=[]):
    lista.append(element)
    return lista

print(dodaj_element(1))        # [1]
print(dodaj_element(2))        # [1, 2] - a oczekiwaliśmy [2]
```

W powyższym przykładzie, za drugim razem zamiast uzyskać listę zawierającą tylko 2, otrzymujemy listę z 1 i 2, ponieważ domyślna lista została zmodyfikowana podczas pierwszego wywołania.

Jeśli chcemy uniknąć tego rodzaju problemów, jednym z podejść jest użycie wartości None jako domyślnej wartości parametru, a następnie wewnątrz funkcji zastąpienie jej nowym, pustym obiektem mutowalnym.

#### Przykład poprawnego podejścia z użyciem None

```python
def dodaj_element(element, lista=None):
    if lista is None:
        lista = []
    lista.append(element)
    return lista

print(dodaj_element(1))        # [1]
print(dodaj_element(2))        # [2] - wynik zgodny z oczekiwaniami
```

Korzystając z tego podejścia, unikamy nieoczekiwanych efektów ubocznych związanych z mutowalnymi wartościami domyślnymi.

### Zaawansowane przykłady i zastosowania

#### Kopiowanie obiektów niestandardowych

W przypadku bardziej skomplikowanych struktur danych, które zawierają zagnieżdżone obiekty lub instancje klas, kopiowanie głębokie jest zazwyczaj niezbędne. Rozważmy przykład klasy zagnieżdżającej inne obiekty.

```python
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

# Tworzenie oryginalnego węzła z dziećmi
original_node = Node(1, [Node(2), Node(3)])

# Kopiowanie płytkie
shallow_copied_node = copy.copy(original_node)
shallow_copied_node.children.append(Node(4))

print([child.value for child in original_node.children])  # [2, 3, 4] - zmienione przez shallow_copied_node

# Kopiowanie głębokie
deep_copied_node = copy.deepcopy(original_node)
deep_copied_node.children.append(Node(5))

print([child.value for child in original_node.children])  # [2, 3, 4] - bez zmian
print([child.value for child in deep_copied_node.children])  # [2, 3, 4, 5] - zmienione tylko przez deep_copied_node
```

W tym przykładzie, kopiowanie płytkie `shallow_copy` zmienia dzieci w oryginalnym węźle, ponieważ lista `children` jest tylko referencją. Kopiowanie głębokie `deep_copy` zapewnia, że każda część struktury danych jest niezależna.

#### Zastosowania praktyczne

Kopiowanie głębokie i płytkie jest kluczowe w wielu scenariuszach programistycznych, takich jak:

- W aplikacjach, które wymagają zarządzania stanem obiektów, kopiowanie odgrywa kluczową rolę, ponieważ pozwala uniknąć nieoczekiwanych efektów ubocznych wynikających z modyfikacji współdzielonych danych.
- Podczas implementacji algorytmów przetwarzania danych, kopiowanie danych wejściowych zapewnia, że oryginalne dane pozostają nienaruszone, co jest szczególnie istotne w środowiskach, gdzie dane mogą być wykorzystywane wielokrotnie.
- W testach jednostkowych możliwość tworzenia kopii obiektów pozwala na izolowanie testów, dzięki czemu każdy test działa na niezależnym stanie i nie wpływa na wyniki innych testów.
- Przy projektowaniu systemów opartych na współbieżności kopiowanie obiektów jest niezbędne, aby uniknąć problemów związanych z jednoczesnym dostępem wielu wątków do tych samych danych.
- W przypadku pracy z mutowalnymi strukturami danych, kopiowanie pozwala na tworzenie niezależnych wersji, co jest istotne podczas porównywania różnych wariantów przetwarzania lub wprowadzania zmian.
- Mechanizm kopiowania płytkiego jest często stosowany w sytuacjach, gdzie nie jest konieczne kopiowanie złożonych struktur danych, ponieważ umożliwia szybkie tworzenie kopii przy zachowaniu referencji do istniejących elementów.
- Kopiowanie głębokie znajduje zastosowanie w sytuacjach, gdzie wymagane jest pełne odseparowanie kopii od oryginału, co zapobiega propagacji zmian między obiektami.
- W pracy z hierarchią klas kopiowanie jest szczególnie istotne, ponieważ pozwala na zachowanie integralności zarówno obiektów bazowych, jak i pochodnych, co jest kluczowe w przypadku złożonych relacji dziedziczenia.
- Kopiowanie danych w aplikacjach wielopoziomowych, takich jak systemy oparte na modelu MVC, pozwala na oddzielenie logiki biznesowej od warstwy prezentacji, co zwiększa modularność i łatwość utrzymania kodu.
- W systemach rozproszonych kopiowanie głębokie jest wykorzystywane do przesyłania danych między węzłami w sposób, który zapewnia ich integralność i niezależność od stanu pierwotnego.
- W bibliotekach przetwarzających dane wielowymiarowe, takich jak NumPy, kopiowanie płytkie umożliwia szybkie operacje na danych, natomiast kopiowanie głębokie jest konieczne w przypadku modyfikacji oryginalnych struktur danych. 

### Kopiowanie a dziedziczenie – wprowadzenie

Kopiowanie w kontekście dziedziczenia w Pythonie może być bardziej skomplikowane niż w przypadku prostych obiektów, szczególnie gdy mamy do czynienia z hierarchią klas. Klasy dziedziczące mogą mieć własne unikalne atrybuty oraz dziedziczyć cechy i metody z klas bazowych. W takich sytuacjach kopiowanie obiektów musi uwzględniać zarówno atrybuty klasy bazowej, jak i klasy pochodnej.

Mechanizmy kopiowania – płytkie i głębokie – działają na obiektach dziedziczących zgodnie z ogólnymi zasadami, ale istotne jest zrozumienie, jak zmiany wprowadzone w jednym obiekcie wpływają na inne, szczególnie gdy obiekty te współdzielą dane poprzez referencje.

**Przykład kopiowania w klasach dziedziczących**

Przeanalizujmy przykład klas `Base` i `Derived`, gdzie `Derived` dziedziczy atrybuty i metody z `Base`. Rozważmy zastosowanie zarówno kopiowania płytkiego, jak i głębokiego:

```python
import copy

class Base:
    def __init__(self, base_attr):
        self.base_attr = base_attr

class Derived(Base):
    def __init__(self, base_attr, derived_attr):
        super().__init__(base_attr)
        self.derived_attr = derived_attr

original_obj = Derived(1, 2)

# Kopiowanie płytkie
shallow_copied_obj = copy.copy(original_obj)
shallow_copied_obj.base_attr = 10
shallow_copied_obj.derived_attr = 20

print(original_obj.base_attr)  # 1 - bez zmian, bo to wartość podstawowa
print(original_obj.derived_attr)  # 2 - bez zmian
```

W tym przykładzie `shallow_copied_obj` jest kopią płytką obiektu `original_obj`. Zmiana wartości `base_attr` i `derived_attr` w kopii nie wpływa na oryginalny obiekt, ponieważ atrybuty te przechowują proste wartości (niemutowalne liczby całkowite). W przypadku bardziej złożonych atrybutów, takich jak listy lub inne obiekty, sytuacja byłaby inna.

**Kopiowanie głębokie w klasach dziedziczących**

Kopiowanie głębokie pozwala na stworzenie całkowicie niezależnej kopii obiektu, wraz z jego strukturą wewnętrzną. Dotyczy to zarówno atrybutów klasy bazowej, jak i pochodnej.

```python
# Kopiowanie głębokie
deep_copied_obj = copy.deepcopy(original_obj)
deep_copied_obj.base_attr = 100
deep_copied_obj.derived_attr = 200

print(original_obj.base_attr)  # 1 - bez zmian
print(original_obj.derived_attr)  # 2 - bez zmian
```

W przypadku kopiowania głębokiego, obiekt `deep_copied_obj` jest całkowicie niezależny od `original_obj`. Zmiany dokonane na kopii nie mają wpływu na oryginał, co jest szczególnie istotne w przypadku złożonych struktur danych przechowywanych w atrybutach.

### Kluczowe różnice między kopiowaniem płytkim a głębokim w dziedziczeniu

**Kopiowanie płytkie:**

- Tworzy nowy obiekt na najwyższym poziomie, ale nie kopiuje w głąb obiektów powiązanych z jego atrybutami.
- W przypadku klas dziedziczących, kopiuje jedynie referencje do obiektów z atrybutów klasy bazowej i pochodnej.
- Może prowadzić do współdzielenia danych między kopiami, co jest ryzykowne w bardziej złożonych scenariuszach.

**Kopiowanie głębokie:**

- Rekurencyjnie kopiuje cały obiekt oraz wszystkie obiekty, do których się odwołuje.
- Zapewnia całkowitą niezależność między kopią a oryginałem.
- W przypadku klas dziedziczących, głębokie kopiowanie obejmuje zarówno atrybuty klasy bazowej, jak i pochodnej.

### Wnioski i dobre praktyki

1. **Dobór odpowiedniej metody kopiowania zależy od natury obiektów, z którymi pracujesz.** Jeśli obiekty są proste i niemutowalne, kopiowanie płytkie zwykle wystarczy. W przypadku złożonych struktur danych lub atrybutów, głębokie kopiowanie jest bardziej bezpieczne.
2. **Zwracaj uwagę na mutowalne atrybuty w klasach dziedziczących.** Mogą one powodować niespodziewane efekty, szczególnie w przypadku kopiowania płytkiego.
3. **Testuj wpływ modyfikacji kopii na oryginalny obiekt.** Zrozumienie, jak zmiany wprowadzane w kopii wpływają na oryginał, pozwala na lepsze projektowanie kodu.
4. **Używaj modułu `copy`, który dostarcza zarówno `copy()` (kopiowanie płytkie), jak i `deepcopy()` (kopiowanie głębokie), do obsługi kopiowania w Pythonie.**
