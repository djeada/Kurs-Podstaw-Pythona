
### Dekoratory
Przy pomocy dekoratorów możemy rozszerzać funkcjonalność istniejących funkcji bez ich modyfikowania. Możemy też używać ich jako dodatkowego sposobu na zabezpieczenie funkcji przed nieprawidłowym wykorzystaniem lub po prostu jako mechanizmu ułatwiającego debugowanie.

Aby zachować informacje o funkcji dekorowanej, możemy użyć dekoratora <code>functools.wraps()</code>:

```python
import functools

def dekoruj(funkcja):
  @functools.wraps(funkcja)
  def funkcja_wew():
    print('przetwarzam dane')
    funkcja()
  return funkcja_wew

@dekoruj
def foo():
  print('foo')

foo()
```

Dzięki temu wszystkie informacje o funkcji <code>foo</code>, takie jak jej nazwa czy dokumentacja, zostaną zachowane po dekoracji.

Możemy też przekazywać argumenty do dekoratora i funkcji dekorowanej:

```python
import functools

def dekoruj(funkcja):
  @functools.wraps(funkcja)
  def funkcja_wew(*args, **kwargs):
    print('przetwarzam dane')
    funkcja(*args, **kwargs)
  return funkcja_wew

@dekoruj
def foo(a, b):
  print(f'a: {a}; b: {b}')

foo(1, 2)
```
