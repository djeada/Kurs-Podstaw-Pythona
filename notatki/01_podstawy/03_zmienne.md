## Zmienne

Zmienne pełnią kluczową rolę w programowaniu, umożliwiając przechowywanie i manipulację danymi. Dzięki nim możemy zapisywać, modyfikować i odzyskiwać wartości w trakcie wykonywania programu.

### Deklaracja i inicjalizacja

W Pythonie nie ma potrzeby jawnego deklarowania typu zmiennej. Język ten jest dynamicznie typowany, co oznacza, że typ zmiennej jest określany w trakcie jej inicjalizacji.

### Typy podstawowe

W Pythonie mamy kilka podstawowych typów danych:

- **Liczby całkowite (`int`)**: np. `5`, `-3`, `42`
- **Liczby zmiennoprzecinkowe (`float`)**: np. `3.14`, `-0.001`, `4.0`
- **Napisy (`str`)**: np. `"Hello"`, `'Python'`
- **Typ logiczny (`bool`)**: przyjmuje jedną z dwóch wartości: `True` lub `False`

### Nazewnictwo zmiennych

- Nazwa zmiennej musi zaczynać się od litery lub znaku podkreślenia (`_`), po którym może następować dowolna kombinacja liter, cyfr i znaków podkreślenia.
- Nazwy zmiennych są wrażliwe na wielkość liter, co oznacza, że `zmienna`, `Zmienna` i `ZMIENNA` to trzy różne zmienne.
- Chociaż Python nie ma ograniczenia co do długości nazw zmiennych, zaleca się nadawanie krótkich, ale jednoznacznych nazw, które opisują przeznaczenie zmiennej.

### Przykład:

Rozważmy poniższy kod:

```python
a = 3
b = a
b = 5
print(a) # Co zostanie wypisane?
```

W tym przypadku, mimo że wartość b została zmieniona na 5, wartość zmiennej a pozostaje bez zmian, więc odpowiedź to 3.
