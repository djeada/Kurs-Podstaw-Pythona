## Tkinter
Tkinter jest modułem biblioteki standardowej, który służy do tworzenia interfejsów graficznych (GUI). Możemy z niego korzystać, aby tworzyć proste aplikacje okienkowe.

Tworzenie okna głównego za pomocą Tkinter wygląda następująco:

```python

import tkinter as tk

root = tk.Tk()
root.mainloop()
```

Możemy dodać różne elementy interfejsu, takie jak przyciski, etykiety, pola tekstowe i inne. Przykład dodania przycisku:

```python
import tkinter as tk

def przycisk_klik():
    print("Kliknięto przycisk")

root = tk.Tk()
przycisk = tk.Button(root, text="Kliknij mnie", command=przycisk_klik)
przycisk.pack()
root.mainloop()
```

Możemy również ustawić różne opcje dla elementów interfejsu, takie jak rozmiar, kolor tła, itp. Przykład:

```python
import tkinter as tk

root = tk.Tk()
etykieta = tk.Label(root, text="Witaj w Tkinter", font=("Helvetica", 16), bg="yellow")
etykieta.pack()
root.mainloop()
```

Tkinter oferuje również możliwość tworzenia layoutów za pomocą ramki (frame). Możemy umieścić różne elementy w ramce i ustalić ich położenie za pomocą siatki (grid). Przykład:

```python
import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

przycisk1 = tk.Button(frame, text="Przycisk 1")
przycisk2 = tk.Button(frame, text="Przycisk 2")
przycisk3 = tk.Button(frame, text="Przycisk 3")

przycisk1.grid(row=0, column=0)
przycisk2.grid(row=0, column=1)
przycisk3.grid(row=0, column=2)

root.mainloop()
```

### Zdarzenia

mamy możliwość obsługi zdarzeń za pomocą metody `bind()`. Zdarzenia mogą być generowane przez użytkownika lub system. Do najczęściej używanych zdarzeń należą:

* `<Button-1>` - kliknięcie lewym przyciskiem myszy na komponencie
* `<ButtonRelease-1>` - puszczenie lewego przycisku myszy nad komponentem
* `<Double-Button-1>` - podwójne kliknięcie lewym przyciskiem myszy na komponencie
* `<Enter>` - najechanie myszką na komponent
* `<Leave>` - zjechanie myszką z komponentu
* `<Key>` - naciśnięcie dowolnego klawisza na klawiaturze
* `<Return>` - naciśnięcie klawisza Enter

Aby obsłużyć zdarzenie, wystarczy wywołać metodę `bind()` na obiekcie komponentu, przekazując do niej nazwę zdarzenia oraz funkcję obsługi zdarzenia.

Przykładowo, jeśli chcemy wyświetlić komunikat po najechaniu myszką na przycisk, możemy użyć następującego kodu:

```python
from tkinter import Button, Tk

def mouse_over(event):
    print("Myszka najechała na przycisk")

root = Tk()
button = Button(root, text="Przycisk")
button.bind("<Enter>", mouse_over)
button.pack()
root.mainloop()
```

Możemy też użyć dekoratora `@event_decorator` do obsługi zdarzeń. W tym przypadku nie musimy już ręcznie wywoływać metody `bind()`, a dekorator automatycznie połączy funkcję z odpowiednim zdarzeniem.

```python
from tkinter import Button, Tk

root = Tk()
button = Button(root, text="Przycisk")

@button.event_decorator("<Enter>")
def mouse_over(event):
    print("Myszka najechała na przycisk")

button.pack()
root.mainloop()
```
