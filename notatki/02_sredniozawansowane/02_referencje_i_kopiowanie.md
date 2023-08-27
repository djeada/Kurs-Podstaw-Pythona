## Referencje i kopiowanie

W Pythonie rozróżniamy dwa kluczowe pojęcia: "referencję" oraz "kopiowanie".

- **Referencja** to odwołanie do pewnego obiektu w pamięci.
- **Kopiowanie** polega na tworzeniu nowego obiektu z identyczną zawartością co pierwotny obiekt.

W Pythonie, gdy przekazujemy obiekty do funkcji, przypisujemy je do innych zmiennych, lub umieszczamy je w kolekcjach, operujemy na referencjach. W praktyce oznacza to, że modyfikacje wprowadzone na jednym "egzemplarzu" obiektu odzwierciedlają się na wszystkich jego "egzemplarzach".

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

```python
import copy
lista = [[1, 2, 3], [4, 5, 6]]
kopia_gleboka = copy.deepcopy(lista)

kopia_gleboka.append([-1, -2, -3])  # wpłynie tylko na `kopia_gleboka`
kopia_gleboka[0].insert(1, 1)      # wpłynie również tylko na `kopia_gleboka`
print(lista)  # pokaże oryginalną listę, bez zmian
```

Podsumowując, ważne jest, aby być świadomym, czy pracujemy na kopii, czy na oryginalnym obiekcie, a także tego, jakie są konsekwencje naszych działań w kontekście referencji i kopiowania.

### Domyślne wartości parametrów funkcji i ich mutowalność

W Pythonie wartości domyślne dla parametrów funkcji są wyliczane tylko raz w momencie definiowania funkcji, a nie za każdym razem, gdy funkcja jest wywoływana. Oznacza to, że jeśli wartość domyślna jest mutowalna, jak lista lub słownik, wszelkie modyfikacje tej wartości zostaną zachowane między kolejnymi wywołaniami funkcji. Może to prowadzić do nieoczekiwanych efektów ubocznych.

Rozważmy funkcję, która dodaje element do listy. Lista jest parametrem z domyślną wartością `[]`.

```python
def dodaj_element(element, lista=[]):
    lista.append(element)
    return lista

print(dodaj_element(1))        # [1]
print(dodaj_element(2))        # [1, 2] - a oczekiwaliśmy [2]
```

W powyższym przykładzie, za drugim razem zamiast uzyskać listę zawierającą tylko 2, otrzymujemy listę z 1 i 2, ponieważ domyślna lista została zmodyfikowana podczas pierwszego wywołania.

Jeśli chcemy uniknąć tego rodzaju problemów, jednym z podejść jest użycie wartości None jako domyślnej wartości parametru, a następnie wewnątrz funkcji zastąpienie jej nowym, pustym obiektem mutowalnym.

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
