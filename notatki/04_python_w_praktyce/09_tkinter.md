## Tkinter - Tworzenie interfejsów graficznych

Tkinter jest standardowym modułem Pythona służącym do tworzenia interfejsów graficznych użytkownika (GUI). Dzięki niemu możemy szybko i efektywnie tworzyć aplikacje okienkowe, które są interaktywne i przyjazne dla użytkownika. W poniższych sekcjach omówimy szczegółowo, jak zainicjalizować okno główne, dodawać do niego elementy, układać widżety oraz obsługiwać zdarzenia.

### Inicjalizacja okna głównego

Pierwszym krokiem w tworzeniu aplikacji graficznej w Pythonie z użyciem Tkinter jest zaimportowanie modułu i zainicjalizowanie głównego okna aplikacji.

#### Kod inicjalizacyjny

```python
import tkinter as tk

root = tk.Tk()                # Tworzy główne okno aplikacji
root.title("Moja aplikacja")   # Ustawia tytuł okna na "Moja aplikacja"
root.geometry("300x200")       # Ustawia wymiary okna: szerokość = 300, wysokość = 200
root.mainloop()                # Uruchamia główną pętlę aplikacji
```

![Przykładowe okno Tkinter](https://github.com/user-attachments/assets/4e826e32-25ea-4372-89f3-963774fefab9)  

Wyjaśnienie krok po kroku:

1. `import tkinter as tk` — Importujemy moduł Tkinter z aliasem `tk`, co upraszcza odwoływanie się do elementów Tkintera.
2. `root = tk.Tk()` — Inicjalizujemy główne okno aplikacji, które jest kontenerem dla wszystkich widżetów.
3. `root.title("Moja aplikacja")` — Ustawiamy tytuł okna, który pojawi się na pasku tytułowym.
4. `root.geometry("300x200")` — Ustalamy rozmiar okna w formacie `"szerokośćxwysokość"`.
5. `root.mainloop()` — Rozpoczyna główną pętlę zdarzeń, dzięki czemu aplikacja pozostaje aktywna i może reagować na interakcje.

### Dodawanie elementów do okna

Po utworzeniu głównego okna możemy dołączać do niego różne elementy interfejsu, zwane widżetami. Tkinter oferuje bogaty zestaw widżetów, takich jak przyciski, etykiety, pola tekstowe itp.

#### Przykład - Dodanie przycisku

Przyciski umożliwiają użytkownikowi interakcję z aplikacją, wywołując określone funkcje po kliknięciu.

```python
def on_button_click():
    print("Kliknięto przycisk!")

button = tk.Button(root, text="Kliknij", command=on_button_click)
button.pack(pady=20)
```

![Przycisk Tkinter](https://github.com/user-attachments/assets/49334b58-bce4-4c6c-bf03-782b281ad6eb)  

Wyjaśnienie:

- `on_button_click` ta funkcja jest wywoływana po kliknięciu przycisku i wypisuje tekst w konsoli.
- `tk.Button()` tworzy przycisk. Parametr `text` ustawia tekst na przycisku, a `command` przypisuje funkcję obsługującą zdarzenie kliknięcia.
- Metoda `pack()` dodaje przycisk do okna i umieszcza go w jego środku. Parametr `pady` dodaje pionowe odstępy nad i pod przyciskiem.

#### Przykład - Dodanie etykiety

Etykiety służą do wyświetlania tekstu lub obrazów.

```python
label = tk.Label(root, text="To jest etykieta", font=("Arial", 14))
label.pack(pady=20)
```

![Etykieta Tkinter](https://github.com/user-attachments/assets/0f8aaa1e-47fd-4db1-a819-62da05261e96)  

Wyjaśnienie:

- `tk.Label()` tworzy etykietę z wybranym tekstem. Parametr `font` pozwala ustawić krój i rozmiar czcionki.
- `pack()` umieszcza etykietę w oknie z odstępem (`pady`), co poprawia czytelność.

### Układanie i kompozycja widżetów

Aby interfejs był czytelny i estetyczny, Tkinter oferuje kilka metod układania widżetów w oknie. Każda z nich ma inne zastosowanie.

I. `pack()` — Układa widżety jeden za drugim w zadanym kierunku, domyślnie pionowo.

```python
button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
```

II. `grid()` — Układa widżety w formie siatki, co umożliwia bardziej precyzyjne rozmieszczenie elementów poprzez przypisywanie ich do określonych wierszy i kolumn.

```python
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
```

III. `place()` — Umożliwia dokładne pozycjonowanie widżetów za pomocą współrzędnych `x` i `y`, co daje pełną kontrolę nad ich położeniem.

```python
button.place(x=50, y=100)
```

Każda z metod ma swoje specyficzne zastosowanie. `pack()` jest prosty i szybki, `grid()` pozwala na bardziej elastyczne pozycjonowanie, a `place()` daje pełną kontrolę nad położeniem elementów.

### Organizacja widżetów za pomocą ramek

Ramki (`Frame`) są kontenerami, które grupują widżety i pomagają organizować bardziej złożone układy.

#### Przykład użycia ramek

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

![Ramka Tkinter](https://github.com/user-attachments/assets/53e70045-7a45-46ba-867b-e550e27cbee8)  

Parametry ramki:

| Parametr  | Opis                                                                                   |
|-----------|----------------------------------------------------------------------------------------|
| **`bg`**  | Ustawia kolor tła ramki.                                                              |
| **`bd`**  | Określa szerokość obramowania ramki.                                                  |
| **`relief`** | Styl obramowania (np. `sunken`, `raised`, `groove`, `ridge`), co dodaje wizualne wyróżnienie. |

Zalety ramek:

- Ramki pozwalają podzielić interfejs na logiczne sekcje, co ułatwia zarządzanie układem.
- W różnych ramkach można stosować różne metody układania, np. `pack()` w jednej ramce, a `grid()` w innej.
- Ramki umożliwiają łatwiejsze utrzymanie estetyki w złożonych interfejsach.

Wskazówki:

- Unikaj używania `pack()` i `grid()` w obrębie tej samej ramki, co może prowadzić do błędów.
- Dla bardziej skomplikowanych interfejsów możesz zagnieżdżać ramki w innych ramkach, co daje większą elastyczność w zarządzaniu układem.

### Obsługa zdarzeń

Interaktywność aplikacji zależy od jej zdolności do reagowania na zdarzenia, takie jak kliknięcia myszy czy naciśnięcia klawiszy. Tkinter pozwala nam obsługiwać te zdarzenia za pomocą metody `bind()`.

#### Typowe zdarzenia

Poniżej kilka popularnych zdarzeń w Tkinter i ich opisy:

Kliknięcia myszy:

| Symbol                | Opis                                  |
|-----------------------|---------------------------------------|
| `<Button-1>`          | Kliknięcie lewym przyciskiem myszy.   |
| `<Button-3>`          | Kliknięcie prawym przyciskiem myszy.  |
| `<Double-Button-1>`   | Podwójne kliknięcie lewym przyciskiem.|

Ruch myszy:

| Symbol    | Opis                               |
|-----------|------------------------------------|
| `<Enter>` | Kursor wchodzi na obszar widżetu.  |
| `<Leave>` | Kursor opuszcza obszar widżetu.    |
| `<Motion>`| Ruch kursora nad widżetem.         |

Klawiatura:

| Symbol      | Opis                             |
|-------------|----------------------------------|
| `<Key>`     | Naciśnięcie dowolnego klawisza.  |
| `<Return>`  | Naciśnięcie klawisza Enter.      |
| `<Escape>`  | Naciśnięcie klawisza Esc.        |

### Metoda `bind()`

Aby powiązać zdarzenie z konkretną funkcją obsługującą, używamy metody `bind()`. Funkcje te przyjmują argument `event`, który zawiera szczegóły zdarzenia (takie jak pozycja kursora czy informacje o klawiszach modyfikujących).

#### Przykład obsługi zdarzeń myszy

Poniższy kod reaguje na to, czy kursor znajduje się nad przyciskiem, wypisując odpowiednie komunikaty.

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

Wyjaśnienie:

- `on_mouse_enter` to funkcja wywoływana, gdy kursor wchodzi na przycisk.
- `on_mouse_leave` to funkcja wywoływana, gdy kursor opuszcza przycisk.
- `bind("<Enter>", on_mouse_enter)` wiąże zdarzenie `<Enter>` z funkcją `on_mouse_enter`.
- `bind("<Leave>", on_mouse_leave)` wiąże zdarzenie `<Leave>` z funkcją `on_mouse_leave`.

### Obsługa zdarzeń klawiatury

Możemy reagować na naciśnięcie klawiszy, np. wyświetlając komunikat, gdy użytkownik naciśnie konkretny klawisz.

#### Przykład obsługi klawisza

```python
def on_key_press(event):
    print(f"Naciśnięto klawisz: {event.char}")

root = Tk()
root.bind("<Key>", on_key_press)
root.mainloop()
```

Wyjaśnienie:

- `bind("<Key>", on_key_press)` wiąże dowolne naciśnięcie klawisza z funkcją `on_key_press`.
- `event.char` zawiera znak reprezentujący naciśnięty klawisz.

### Łączenie wielu zdarzeń

Tkinter pozwala przypisać wiele różnych zdarzeń do tego samego widżetu lub jedną funkcję do obsługi zdarzeń na wielu widżetach.

#### Przykład — Łączenie zdarzeń na przycisku

Poniższy przykład przedstawia reakcję na różne kliknięcia przycisków myszy.

```python
def on_left_click(event):
    print("Lewy przycisk myszy")

def on_right_click(event):
    print("Prawy przycisk myszy")

button = Button(root, text="Kliknij mnie")
button.bind("<Button-1>", on_left_click)   # Kliknięcie lewym przyciskiem
button.bind("<Button-3>", on_right_click)  # Kliknięcie prawym przyciskiem
button.pack()
```

### Obsługa zdarzeń przy użyciu dekoratorów

Domyślnie Tkinter nie obsługuje dekoratorów dla zdarzeń, ale można napisać własny dekorator `event_handler`, który uprości wiązanie zdarzeń.

#### Przykład własnego dekoratora `event_handler`

```python
def event_handler(event_name):
    def decorator(func):
        def wrapper(event):
            return func(event)
        wrapper.event_name = event_name
        return wrapper
    return decorator

class MyApp:
    def __init__(self, root):
        self.button = Button(root, text="Kliknij mnie")
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

root = Tk()
app = MyApp(root)
root.mainloop()
```

Wyjaśnienie:

1. Dekorator `event_handler` dodaje atrybut `event_name` do funkcji, wskazując typ obsługiwanego zdarzenia.
2. Metoda `bind_events` przeszukuje metody klasy `MyApp` i przypisuje zdarzenia do tych, które mają atrybut `event_name`.
3. `@event_handler("<Button-1>")` powiązuje funkcję `on_click` z lewym przyciskiem myszy.

**Uwaga**: To rozwiązanie wymaga dobrej znajomości Pythona i stosowane jest w bardziej złożonych aplikacjach.

### Zamykanie aplikacji na zdarzenie

Zamknięcie aplikacji można obsłużyć za pomocą przycisku wywołującego metodę `root.destroy()` lub na przykład na zdarzenie klawiaturowe.

#### Przykład — Dodanie przycisku zamykającego aplikację

```python
import tkinter as tk

def close_app():
    root.destroy()

root = tk.Tk()
button_exit = tk.Button(root, text="Zamknij", command=close_app)
button_exit.pack()
root.mainloop()
```

![Przycisk zamykający aplikację](https://github.com/user-attachments/assets/793499d9-e5a7-480e-9fde-9b1672e1bef7)

Wyjaśnienie:

-  Funkcja `close_app()` wywołuje `root.destroy()`, co zamyka aplikację.
- `command=close_app` przypisuje funkcję zamykającą do przycisku.

#### Alternatywne zamknięcie aplikacji

Możemy także przypisać zamknięcie aplikacji do klawisza, na przykład `Escape`.

```python
root.bind("<Escape>", lambda event: root.destroy())
```
