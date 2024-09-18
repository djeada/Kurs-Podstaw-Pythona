## Tkinter - Tworzenie interfejsów graficznych

Tkinter jest standardowym modułem Pythona służącym do tworzenia interfejsów graficznych użytkownika (GUI). Dzięki niemu możemy szybko i efektywnie tworzyć aplikacje okienkowe, które są interaktywne i przyjazne dla użytkownika. W poniższych sekcjach omówimy szczegółowo, jak zainicjalizować okno główne, dodawać do niego elementy, układać widżety oraz obsługiwać zdarzenia.

### Inicjalizacja okna głównego

Aby rozpocząć pracę z Tkinter, musimy najpierw zaimportować moduł i zainicjalizować główne okno aplikacji, które będzie kontenerem dla wszystkich innych widżetów.

```python
import tkinter as tk

root = tk.Tk()
root.title("Moja aplikacja")  # Nadanie tytułu oknu
root.geometry("300x200")      # Ustawienie wymiarów okna
root.mainloop()
```

- Importujemy moduł `tkinter` i nadajemy mu alias `tk` dla wygody. Dzięki temu możemy korzystać z elementów Tkintera, odwołując się do nich jako `tk.Element`.
- Inicjalizujemy główne okno aplikacji, tworząc instancję klasy `Tk()`. Obiekt `root` będzie podstawą naszego interfejsu graficznego.
- Metoda `title()` pozwala nam nadać oknu tytuł, który pojawi się na pasku tytułowym.
- Metoda `geometry()` umożliwia ustawienie rozmiaru okna w pikselach. Format to `"szerokośćxwysokość"`.
- Metoda `mainloop()` uruchamia pętlę zdarzeń Tkintera, dzięki czemu aplikacja pozostaje aktywna i reaguje na interakcje użytkownika.

### Dodawanie elementów do okna

Tkinter oferuje bogaty zestaw widżetów (elementów interfejsu), takich jak przyciski, etykiety, pola tekstowe czy pola wyboru. Po zainicjalizowaniu głównego okna możemy dodawać do niego te elementy, aby stworzyć interaktywny interfejs.

#### Przycisk

Przyciski są podstawowymi elementami interfejsu, które pozwalają użytkownikowi na wykonywanie określonych akcji.

```python
def on_button_click():
    print("Kliknięto przycisk!")

button = tk.Button(root, text="Kliknij", command=on_button_click)
button.pack(pady=20)
```

- Tworzymy funkcję, która zostanie wywołana po kliknięciu przycisku. W tym przypadku wypisuje ona komunikat w konsoli.
- Tworzymy instancję przycisku, przypisując mu tekst oraz funkcję obsługującą zdarzenie kliknięcia poprzez parametr `command`.
- Używamy metody `pack()`, aby dodać przycisk do okna. Parametr `pady` dodaje pionowe odstępy nad i pod przyciskiem, poprawiając estetykę interfejsu.

#### Etykieta

Etykiety służą do wyświetlania tekstu lub obrazów w interfejsie.

```python
label = tk.Label(root, text="To jest etykieta", font=("Arial", 14))
label.pack(pady=20)
```

- Tworzymy etykietę z określonym tekstem i czcionką. Parametr `font` pozwala nam ustawić krój i rozmiar czcionki.
- Podobnie jak w przypadku przycisku, używamy metody `pack()` do dodania etykiety do okna z odpowiednimi odstępami.

### Układanie i kompozycja widżetów

Aby interfejs był czytelny i intuicyjny, ważne jest odpowiednie rozmieszczenie widżetów w oknie. Tkinter oferuje kilka metod układania, które pozwalają na precyzyjną kontrolę nad położeniem elementów.

#### Główne metody układania

I. **`pack()`:**

- Automatycznie układa widżety jeden za drugim w określonym kierunku (domyślnie pionowo).
- Parametry takie jak `side`, `fill`, `expand` pozwalają na dodatkową kontrolę.

**Przykład:**

```python
button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
```

II. **`grid()`:**

- Układa widżety w formie siatki (tabeli), gdzie możemy określić wiersze i kolumny.
- Pozwala na precyzyjne pozycjonowanie elementów.

**Przykład:**

```python
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
```

III. **`place()`:**

- Umożliwia dokładne pozycjonowanie widżetów za pomocą współrzędnych `x` i `y`.
- Daje największą kontrolę, ale wymaga ręcznego zarządzania położeniem.

**Przykład:**

```python
button.place(x=50, y=100)
```

#### Użycie ramek dla lepszej organizacji

Ramki (`Frame`) służą do grupowania widżetów, co ułatwia zarządzanie złożonymi układami.

**Przykład użycia ramek:**

```python
import tkinter as tk

root = tk.Tk()

# Tworzenie ramki
frame = tk.Frame(root, bg="lightgray", bd=5, relief="ridge")
frame.pack(pady=20, padx=20)

button1 = tk.Button(frame, text="Przycisk 1")
button2 = tk.Button(frame, text="Przycisk 2")

# Umieszczanie przycisków w siatce wewnątrz ramki
button1.grid(row=0, column=0, padx=10)
button2.grid(row=0, column=1, padx=10)

root.mainloop()
```

Ramka jest kontenerem dla innych widżetów. Parametry:

- `bg`: kolor tła ramki.
- `bd`: szerokość obramowania.
- `relief`: styl obramowania (np. `sunken`, `raised`, `groove`, `ridge`).

Używamy metody `grid()` wewnątrz ramki, aby precyzyjnie ułożyć przyciski.

**Zalety użycia ramek:**

- Pozwalają na podział interfejsu na logiczne sekcje.
- Możemy stosować różne metody układania w różnych ramkach.
- Ułatwiają zarządzanie złożonymi interfejsami.

**Wskazówki:**

- Unikaj mieszania metod `pack()` i `grid()` w obrębie tej samej ramki.
- Dla skomplikowanych układów warto zagnieżdżać ramki w innych ramkach.

### Obsługa zdarzeń

Interaktywność aplikacji zależy od jej zdolności do reagowania na zdarzenia generowane przez użytkownika.

#### Podstawowe zdarzenia

**Kliknięcia myszy:**

- `<Button-1>`: kliknięcie lewym przyciskiem myszy.
- `<Button-3>`: kliknięcie prawym przyciskiem myszy.
- `<Double-Button-1>`: podwójne kliknięcie lewym przyciskiem.

**Ruch myszy:**

- `<Enter>`: kursor wchodzi na widżet.
- `<Leave>`: kursor opuszcza widżet.
- `<Motion>`: ruch kursora nad widżetem.

**Klawiatura:**

- `<Key>`: naciśnięcie dowolnego klawisza.
- `<Return>`: naciśnięcie klawisza Enter.
- `<Escape>`: naciśnięcie klawisza Esc.

#### Metoda `bind()`

Aby powiązać zdarzenie z funkcją obsługującą, używamy metody `bind()`.

**Przykład:**

```python
from tkinter import Tk, Button

def on_mouse_enter(event):
print("Myszka najechała na przycisk")

def on_mouse_leave(event):
print("Myszka opuściła przycisk")

root = Tk()
button = Button(root, text="Najedź na mnie!")
button.bind("<Enter>", on_mouse_enter)
button.bind("<Leave>", on_mouse_leave)
button.pack()
root.mainloop()
```

Funkcje obsługujące zdarzenia przyjmują jeden argument — obiekt `event`, który zawiera informacje o zdarzeniu (np. pozycja kursora, stan klawiszy modyfikujących).

#### Łączenie wielu zdarzeń

Możemy powiązać wiele zdarzeń z jednym widżetem lub jedną funkcję obsługującą z wieloma widżetami.

**Przykład:**

```python
def on_key_press(event):
print(f"Naciśnięto klawisz: {event.char}")

root.bind("<Key>", on_key_press)
```

#### Uwaga o dekoratorze `@event_decorator`

Dekorator `@event_decorator` nie jest częścią standardowej biblioteki Tkinter. Standardowo zdarzenia obsługujemy za pomocą metody `bind()`. Jeśli chcemy używać dekoratorów do obsługi zdarzeń, musimy zaimplementować własne rozwiązanie lub skorzystać z dodatkowych bibliotek.

**Przykład własnego dekoratora:**

```python
def event_handler(event_name):
def decorator(func):
    def wrapper(event):
        return func(event)
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    wrapper.event_name = event_name
    return wrapper
return decorator

class MyApp:
def __init__(self, root):
    self.button = tk.Button(root, text="Kliknij mnie")
    self.button.pack()
    self.bind_events()

def bind_events(self):
    for attr in dir(self):
        func = getattr(self, attr)
        if callable(func) and hasattr(func, 'event_name'):
            self.button.bind(func.event_name, func)

@event_handler("<Button-1>")
def on_click(self, event):
    print("Przycisk został kliknięty")
```

- Tworzymy dekorator, który dodaje atrybut `event_name` do funkcji.
- W klasie `MyApp` przeglądamy wszystkie metody i jeśli mają atrybut `event_name`, wiążemy je ze zdarzeniami.

**Uwaga:** Takie rozwiązanie wymaga zaawansowanej znajomości Pythona i może nie być konieczne w prostych aplikacjach.

### Zakończenie pracy

Po skonfigurowaniu interfejsu i dodaniu wszystkich niezbędnych elementów, uruchamiamy pętlę główną aplikacji, która utrzymuje interfejs aktywnym i reagującym na zdarzenia.

```python
root.mainloop()
```

Możemy zamknąć aplikację, wywołując metodę `root.destroy()`, np. w odpowiedzi na zdarzenie.

```python
def close_app():
  root.destroy()

button_exit = tk.Button(root, text="Zamknij", command=close_app)
button_exit.pack()
```
