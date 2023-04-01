## Kod bajtowy
Moduł `dis` służy do wyświetlania kodu bajtowego dla funkcji lub bloków kodu. Aby wyświetlić kod bajtowy dla funkcji, użyj funkcji `dis()` w nastęþujący sposób:

```python
from dis import dis

def suma(a, b):
  return a + b

dis(suma)
```

Aby wyświetlić kod bajtowy dla bloku kodu, użyj funkcji `disassemble()`:

```python
from dis import disassemble

code = """
def suma(a, b):
  return a + b
"""

disassemble(code)
```

Kod bajtowy jest przydatny w przypadku gdy chcesz zrozumieć, jak interpreter konwertuje kod napisany w Pythonie na instrukcje, które są wykonywane przez maszynę. Może to być również pomocne przy optymalizacji kodu lub tworzeniu wtyczek do Pythona w innych językach.
    
Aby uzyskać kod z zewnętrznych bibliotek musimy użyć modułu <code>inspect</code>. Biblioteka ta umożliwia uzyskanie informacji o strukturze programu. Może być używana do zapisywania lub odczytywania kodu źródłowego, dokumentacji i innych informacji o obiektach.

Niektóre przydatne funkcje w module inspect to:

* `inspect.getsource(object)` - zwraca kod źródłowy obiektu jako string
* `inspect.getdoc(object)` - zwraca dokumentację obiektu jako string
* `inspect.getmembers(object)` - zwraca listę krotek (name, value) dla wszystkich atrybutów obiektu
* `inspect.isclass(object)` - zwraca True, jeśli obiekt jest klasą
* `inspect.isfunction(object)` - zwraca True, jeśli obiekt jest funkcją
* `inspect.ismethod(object)` - zwraca True, jeśli obiekt jest metodą

Przykład użycia:

```python
import inspect
import tkinter

print(inspect.getsource(tkinter.Tk)) # podejzyj kod klasy Tk z modulu tkinter
print(inspect.getdoc(tkinter.Tk)) # podejzyj docstring klasy Tk z modulu tkinter
```
