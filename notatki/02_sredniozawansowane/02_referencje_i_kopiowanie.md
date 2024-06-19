## Referencje i kopiowanie

W Pythonie rozróżniamy dwa kluczowe pojęcia: "referencję" oraz "kopiowanie".

- **Referencja** to odwołanie do pewnego obiektu w pamięci.
- **Kopiowanie** polega na tworzeniu nowego obiektu z identyczną zawartością co pierwotny obiekt.

W Pythonie, gdy przekazujemy obiekty do funkcji, przypisujemy je do innych zmiennych, lub umieszczamy je w kolekcjach, operujemy na referencjach. W praktyce oznacza to, że modyfikacje wprowadzone na jednym "egzemplarzu" obiektu odzwierciedlają się na wszystkich jego "egzemplarzach".

### Przykład referencji w Pythonie

```python
lista = [[1, 2, 3], [4, 5, 6]]
kopia_listy = lista

kopia_listy.append([-1, -2, -3]) # wpłynie na obie listy
kopia_listy[0].insert(1, 1)     # wpłynie również na obie listy
print(lista)  # pokaże zmienioną listę
```

Aby uniknąć niechcianych efektów, można skorzystać z mechanizmów kopiowania: płytkiego (shallow copy) lub głębokiego (deep copy).

### Kopiowanie płytkie (Shallow Copy)

Tworzy nową kolekcję na najwyższym poziomie, ale elementy wewnętrzne (np. listy w liście) są nadal referencjami.

#### Przykład kopiowania płytkiego

```python
import copy
lista = [[1, 2, 3], [4, 5, 6]]
kopia_plytka = copy.copy(lista)

kopia_plytka.append([-1, -2, -3])  # wpłynie tylko na `kopia_plytka`
kopia_plytka[0].insert(1, 1)      # wpłynie na obie listy, bo wewnętrzne listy są referencjami
print(lista)  # pokaże częściowo zmienioną listę
```

### Kopiowanie głębokie (Deep Copy)

Tworzy całkowicie nową kopię obiektu i wszystkich jego wewnętrznych elementów. Jest to kopiowanie "w głąb".

#### Przykład kopiowania głębokiego

```python
import copy
lista = [[1, 2, 3], [4, 5, 6]]
kopia_gleboka = copy.deepcopy(lista)

kopia_gleboka.append([-1, -2, -3])  # wpłynie tylko na `kopia_gleboka`
kopia_gleboka[0].insert(1, 1)      # wpłynie również tylko na `kopia_gleboka`
print(lista)  # pokaże oryginalną listę, bez zmian
```

Podsumowując, ważne jest, aby być świadomym, czy pracujemy na kopii, czy na oryginalnym obiekcie, a także tego, jakie są konsekwencje naszych działań w kontekście referencji i kopiowania.

### Podsumowanie tematów: referencja, kopiowanie, płytkie, głębokie

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

1. **Zarządzanie stanem w aplikacjach**: W aplikacjach webowych lub GUI, gdzie zarządzanie stanem obiektów jest istotne, kopiowanie zapewnia, że zmiany w jednej części aplikacji nie wpływają nieoczekiwanie na inne części.
2. **Algorytmy przetwarzania danych**: W algorytmach przetwarzania danych, gdzie często modyfikujemy dane wejściowe, tworzenie kopii danych jest istotne, aby uniknąć efektów ubocznych.
3. **Testowanie**: W testach jednostkowych, tworzenie kopii obiektów może pomóc w izolowaniu testów i zapewnieniu, że każdy test jest niezależny od innych.

### Kopiowanie a dziedziczenie

W kontekście dziedziczenia, kopiowanie może być bardziej skomplikowane. Rozważmy przykład klas dziedziczących, gdzie musimy kopiować zarówno obiekty bazowe, jak i obiekty pochodne.

```python
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
print(original_obj.derived_attr)  # 2

- bez zmian, bo to wartość podstawowa

# Kopiowanie głębokie
deep_copied_obj = copy.deepcopy(original_obj)
deep_copied_obj.base_attr = 100
deep_copied_obj.derived_attr = 200

print(original_obj.base_attr)  # 1 - bez zmian
print(original_obj.derived_attr)  # 2 - bez zmian
```

W kontekście dziedziczenia, zarówno płytkie, jak i głębokie kopiowanie zachowują struktury obiektów bazowych i pochodnych, ale głębokie kopiowanie zapewnia, że wszystkie atrybuty są całkowicie niezależne.
