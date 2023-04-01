## Referencje i kopiowanie

Dwa niezwykle istotne pojęcia w programowaniu to "referencja" i "kopiowanie". Referencja to odwołanie do oryginalnego obiektu, a kopiowanie to tworzenie nowego obiektu z tą samą zawartością co oryginalny. W języku Python przekazywanie obiektów do funkcji lub przypisywanie ich do nowych nazw odbywa się poprzez referencje. To oznacza, że zarówno oryginalny obiekt, jak i nowy obiekt będą wskazywać na to samo miejsce w pamięci. Wszelkie zmiany wprowadzone w jednym obiekcie będą widoczne również w drugim.  

```python
lista = [[1, 2, 3], [4, 5, 6]]
nowa_lista = lista

nowa_lista.append([-1, -2, -3]) # modyfikuje obie listy
nowa_lista[0].insert(1, 1)      # modyfikuje obie listy
print(lista)
```

Aby uniknąć takiej sytuacji, możemy skorzystać z kopiowania płytkiego lub głębokiego.
 
 1. Kopiowanie płytkie

Kopiowanie płytkie pozwoli na utworzenie nowego obiektu dla zewnętrznej struktury danych, ale wewnętrzne struktury danych będą przekazywane przez referencję. W naszym przykładzie z listą 2d, kopiowanie płytkie utworzy nowy obiekt dla zewnętrznej listy, ale wewnętrzne listy będą przekazane przez referencję.
    
```python
import copy
lista = [[1, 2, 3], [4, 5, 6]]
nowa_lista = copy.copy(lista)

nowa_lista.append([-1, -2, -3]) # modyfikuje jedynie nowa liste
nowa_lista[0].insert(1, 1)      # modyfikuje obie listy
print(lista)
```

 2. Kopiowanie głębokie 

Kopiowanie głębokie pozwoli natomiast na utworzenie nowych obiektów dla zarówno zewnętrznej, jak i wewnętrznych struktur danych.

```python
import copy
lista = [[1, 2, 3], [4, 5, 6]]
nowa_lista = copy.deepcopy(lista)

nowa_lista.append([-1, -2, -3]) # modyfikuje jedynie nowa liste
nowa_lista[0].insert(1, 1)      # modyfikuje jedynie nowa liste
print(lista)
```
