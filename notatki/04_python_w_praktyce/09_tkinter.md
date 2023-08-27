## Tkinter - Tworzenie interfejsów graficznych

Tkinter to wbudowany moduł w Pythonie do tworzenia interfejsów graficznych (GUI). Dzięki niemu można szybko i prosto tworzyć aplikacje okienkowe. Poniżej znajdują się podstawowe informacje oraz przykłady wykorzystania Tkinter.

### Inicjalizacja okna głównego

Aby rozpocząć pracę z Tkinter, najpierw trzeba stworzyć główne okno aplikacji:

```python
import tkinter as tk

root = tk.Tk()
root.title("Moja aplikacja")  # Nadanie tytułu oknu
root.geometry("300x200")     # Ustawienie wymiarów okna
root.mainloop()
```

### Dodawanie elementów do okna

Tkinter oferuje szeroką gamę widżetów (elementów interfejsu), takich jak przyciski, etykiety czy pola tekstowe.

#### Przycisk

```python
def on_button_click():
    print("Kliknięto przycisk!")

button = tk.Button(root, text="Kliknij", command=on_button_click)
button.pack(pady=20)
```

#### Etykieta

```python
label = tk.Label(root, text="To jest etykieta", font=("Arial", 14))
label.pack(pady=20)
```

### Układanie i kompozycja widżetów

Tworzenie skutecznych interfejsów graficznych wymaga nie tylko dodawania odpowiednich widżetów, ale także ich odpowiedniego układania. W Tkinter mamy do dyspozycji kilka metod umożliwiających kontrolę nad rozmieszczeniem komponentów w oknie.

#### Główne metody układania

1. **pack()**: Automatycznie układa widżety jeden za drugim, w zależności od wybranej orientacji (pionowej lub poziomej).
2. **grid()**: Pozwala układać widżety w siatce, podobnej do tabeli, gdzie każdy widżet jest przypisany do określonego wiersza i kolumny.
3. **place()**: Umożliwia dokładne umiejscowienie widżetu w określonym miejscu, podając konkretne współrzędne x i y.

#### Użycie ramek dla lepszej organizacji

Ramki (ang. `Frame`) w Tkinter to narzędzie, które pozwala na grupowanie widżetów. Dzięki temu możemy lepiej zarządzać układem oraz stosować różne metody kompozycji dla różnych grup widżetów.

Przykład użycia ramek:

```python
import tkinter as tk

root = tk.Tk()

# Tworzenie ramki
frame = tk.Frame(root, bg="lightgray", bd=5, relief="ridge")  # Dodane tło i obramowanie dla lepszej wizualizacji
frame.pack(pady=20, padx=20)

button1 = tk.Button(frame, text="Przycisk 1")
button2 = tk.Button(frame, text="Przycisk 2")

# Umieszczanie przycisków w siatce wewnątrz ramki
button1.grid(row=0, column=0, padx=10)
button2.grid(row=0, column=1, padx=10)

root.mainloop()
```

- Ramki są świetnym narzędziem do tworzenia segmentów w interfejsie, takich jak paski narzędzi, sekcje formularzy czy panele nawigacyjne.
- Wybór metody układania zależy od konkretnego przypadku. W niektórych sytuacjach `pack()` będzie idealny, podczas gdy w innych `grid()` lub `place()` dadzą więcej kontroli.
- Unikaj mieszania metod układania (np. `pack()` z `grid()`) w obrębie jednej ramki, ponieważ może to prowadzić do nieoczekiwanych wyników.

### Obsługa zdarzeń

W Tkinter, zdarzenia odgrywają kluczową rolę, umożliwiając interakcję użytkownika z interfejsem graficznym. Aby odpowiedzieć na różne akcje użytkownika, takie jak kliknięcia myszą czy naciśnięcia klawisza, używamy mechanizmu obsługi zdarzeń.

#### Podstawowe zdarzenia

Oto niektóre z najczęściej używanych zdarzeń w Tkinter:

* `<Button-1>`: Kliknięcie lewym przyciskiem myszy na komponencie.
* `<ButtonRelease-1>`: Puszczenie lewego przycisku myszy nad komponentem.
* `<Double-Button-1>`: Podwójne kliknięcie lewym przyciskiem myszy na komponencie.
* `<Enter>`: Najechanie myszką na komponent.
* `<Leave>`: Zjechanie myszką z komponentu.
* `<Key>`: Naciśnięcie dowolnego klawisza na klawiaturze.
* `<Return>`: Naciśnięcie klawisza Enter.

#### Metoda `bind()`

Aby obsłużyć zdarzenie, można użyć metody `bind()`, która jest dostępna dla wszystkich komponentów w Tkinter. Metoda ta przyjmuje dwa argumenty: nazwę zdarzenia oraz funkcję (lub metodę), która ma zostać wywołana, gdy zdarzenie wystąpi.

Przykład obsługi zdarzenia najechania myszką na przycisk:

```python
from tkinter import Button, Tk

def on_mouse_enter(event):
    print("Myszka najechała na przycisk")

root = Tk()
button = Button(root, text="Najedź na mnie!")
button.bind("<Enter>", on_mouse_enter)
button.pack()
root.mainloop()
```

#### Uwaga o dekoratorze @event_decorator

Dekorator `@event_decorator` nie jest standardową częścią biblioteki Tkinter. Jeżeli chcesz z niego korzystać, potrzebujesz dodatkowej biblioteki lub samodzielnej implementacji tego dekoratora. W standardowym Tkinter, obsługa zdarzeń opiera się głównie na użyciu metody `bind()`.

#### Łączenie wielu zdarzeń

Możesz również połączyć kilka zdarzeń z jednym komponentem, co pozwala na tworzenie bardziej złożonych interakcji:

```python

def on_mouse_leave(event):
    print("Myszka opuściła przycisk")

button.bind("<Leave>", on_mouse_leave)
```

W ten sposób, korzystając z różnych zdarzeń i odpowiednich funkcji obsługi, możesz tworzyć interaktywne i dynamiczne interfejsy użytkownika w Tkinter.

### Zakończenie pracy

Po dodaniu wszystkich elementów i konfiguracji interfejsu, należy wywołać funkcję `mainloop()` na obiekcie głównego okna. Dzięki temu aplikacja będzie działać do momentu zamknięcia okna przez użytkownika.
