## Tkinter - Tworzenie interfejsów graficznych

Tkinter jest standardowym modułem Pythona służącym do tworzenia interfejsów graficznych użytkownika (GUI). Dzięki niemu możemy szybko i efektywnie tworzyć aplikacje okienkowe, które są interaktywne i przyjazne dla użytkownika. W poniższych sekcjach omówimy szczegółowo, jak zainicjalizować okno główne, dodawać do niego elementy, układać widżety oraz obsługiwać zdarzenia.

### Inicjalizacja okna głównego

Pierwszym krokiem w tworzeniu aplikacji graficznej w Pythonie z użyciem Tkinter jest zaimportowanie modułu i zainicjalizowanie głównego okna aplikacji.

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

**Przykład - Dodanie przycisku**

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

**Przykład - Dodanie etykiety**

Etykiety służą do wyświetlania tekstu lub obrazów.

```python
label = tk.Label(root, text="To jest etykieta", font=("Arial", 14))
label.pack(pady=20)
```

![Etykieta Tkinter](https://github.com/user-attachments/assets/0f8aaa1e-47fd-4db1-a819-62da05261e96)  

Wyjaśnienie:

- `tk.Label()` tworzy etykietę z wybranym tekstem. Parametr `font` pozwala ustawić krój i rozmiar czcionki.
- `pack()` umieszcza etykietę w oknie z odstępem (`pady`), co poprawia czytelność.

### Układanie i kompozycja widżetów w Tkinter

Tworzenie przejrzystego i estetycznego interfejsu w Tkinter opiera się na odpowiednim układaniu widżetów. Tkinter oferuje trzy główne metody rozmieszczania elementów w oknie: `pack()`, `grid()` oraz `place()`. Każda z tych metod służy innym celom i posiada unikalne parametry umożliwiające elastyczną kontrolę nad układem widżetów.

#### I. Metoda `pack()`

Metoda `pack()` automatycznie rozmieszcza widżety w interfejsie, układając je jeden za drugim zgodnie z ustaloną orientacją. Domyślnie widżety są rozmieszczane w pionie. Chociaż metoda ta jest łatwa w użyciu, oferuje ograniczoną kontrolę nad dokładnym pozycjonowaniem widżetów, co może być mniej wygodne w bardziej złożonych interfejsach.

Poniższy przykład pokazuje podstawowe użycie `pack()` do ułożenia dwóch przycisków po lewej i prawej stronie okna:

```python
import tkinter as tk

root = tk.Tk()
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")

button1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
button2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

root.mainloop()
```

![Układ przycisków po lewej i prawej stronie](https://github.com/user-attachments/assets/129d9ad4-9bf0-41b6-978f-6f7b145939d6)

W tym przykładzie oba przyciski są umieszczone po przeciwnych stronach (`LEFT` i `RIGHT`) oraz wypełniają całą przestrzeń pionową i poziomą dzięki parametrom `fill=tk.BOTH` oraz `expand=True`.

Parametry metody `pack()`:

| Parametr  | Opis                                                                                      | Przykład                                |
|-----------|-------------------------------------------------------------------------------------------|-----------------------------------------|
| `side`    | Określa, z której strony widżet będzie pakowany. Możliwe wartości to: `tk.TOP`, `tk.BOTTOM`, `tk.LEFT`, `tk.RIGHT`.  | `side=tk.LEFT`                          |
| `fill`    | Określa, czy widżet ma wypełnić przestrzeń w kierunku poziomym (`tk.X`), pionowym (`tk.Y`) lub obu (`tk.BOTH`). | `fill=tk.BOTH`                          |
| `expand`  | Jeśli ustawione na `True`, widżet rozszerzy się, aby wypełnić dostępną przestrzeń w ramach swojego kontenera.     | `expand=True`                           |
| `padx`    | Dodaje poziomy odstęp (padding) po obu stronach widżetu.                                    | `padx=10`                               |
| `pady`    | Dodaje pionowy odstęp (padding) nad i pod widżetem.                                        | `pady=5`                                |

**Przykład 1: Tworzenie listy przycisków w pionie z odstępami**

W tym przykładzie umieszczamy pięć przycisków jeden pod drugim, każdy z niewielkim odstępem (`pady=5`), aby wyglądały bardziej estetycznie.

```python
import tkinter as tk

root = tk.Tk()
for i in range(5):
    button = tk.Button(root, text=f"Button {i+1}")
    button.pack(fill=tk.X, pady=5)  # Pionowy odstęp między przyciskami

root.mainloop()
```

![Przyciski ułożone pionowo z odstępami](https://github.com/user-attachments/assets/05c35c58-5d55-4eab-a1f3-607d845196f1)

Dzięki ustawieniu `fill=tk.X`, przyciski wypełniają całą dostępną szerokość okna, co pozwala uzyskać bardziej zorganizowany wygląd.

**Przykład 2: Tworzenie prostego menu poziomego**

W tym przykładzie tworzymy prosty pasek menu umieszczony u góry okna. Każdy przycisk w menu jest ustawiony w jednej linii dzięki `side=tk.LEFT` oraz dodaniu poziomego odstępu (`padx=5`), aby oddzielić przyciski.

```python
import tkinter as tk

root = tk.Tk()
menu_bar = tk.Frame(root)
menu_bar.pack(side=tk.TOP, fill=tk.X)

btn1 = tk.Button(menu_bar, text="Home")
btn1.pack(side=tk.LEFT, padx=5)

btn2 = tk.Button(menu_bar, text="Settings")
btn2.pack(side=tk.LEFT, padx=5)

root.mainloop()
```

![Proste menu poziome](https://github.com/user-attachments/assets/a0d34ea7-f0d3-40fb-bfc9-268fbc3c4e1f)

W tym przypadku `fill=tk.X` w `menu_bar` sprawia, że pasek menu rozciąga się na całą szerokość okna, podczas gdy poszczególne przyciski `Home` i `Settings` są ułożone poziomo z niewielkim odstępem.

#### II. Metoda `grid()`

Metoda `grid()` umożliwia organizację widżetów w siatce, przypisując je do określonych wierszy (`row`) i kolumn (`column`). Dzięki temu jest idealna do tworzenia bardziej precyzyjnych układów, takich jak formularze, tabele, czy skomplikowane interfejsy, które wymagają dokładnego rozmieszczenia elementów.

Poniższy przykład pokazuje podstawowe użycie `grid()` do stworzenia prostego formularza z polami dla nazwy użytkownika i hasła:

```python
import tkinter as tk

root = tk.Tk()
label1 = tk.Label(root, text="Username")
entry1 = tk.Entry(root)
label2 = tk.Label(root, text="Password")
entry2 = tk.Entry(root)

label1.grid(row=0, column=0, sticky="w")
entry1.grid(row=0, column=1)
label2.grid(row=1, column=0, sticky="w")
entry2.grid(row=1, column=1)

root.mainloop()
```

![Formularz logowania w siatce](https://github.com/user-attachments/assets/d3a8a977-df65-4418-b66c-f30f2bfc5ebd)

W tym przykładzie etykiety są umieszczone w lewej kolumnie (`column=0`), a pola wejściowe w prawej (`column=1`). `sticky="w"` powoduje, że etykiety są wyrównane do lewej strony komórki.

Parametry metody `grid()`:

| Parametr     | Opis                                                                                               | Przykład                               |
|--------------|----------------------------------------------------------------------------------------------------|----------------------------------------|
| `row`        | Określa numer wiersza, w którym ma się znaleźć widżet.                                             | `row=0`                                |
| `column`     | Określa numer kolumny, w której ma się znaleźć widżet.                                             | `column=1`                             |
| `sticky`     | Ustawia, do której krawędzi komórki ma przylegać widżet (`n`, `s`, `e`, `w` lub ich kombinacja).   | `sticky="w"`                           |
| `padx`       | Dodaje poziomy odstęp (padding) po obu stronach widżetu w komórce.                                 | `padx=5`                               |
| `pady`       | Dodaje pionowy odstęp (padding) nad i pod widżetem w komórce.                                      | `pady=5`                               |
| `columnspan` | Określa liczbę kolumn, które widżet ma zajmować (przydatne dla elementów zajmujących więcej przestrzeni). | `columnspan=2`                        |
| `rowspan`    | Określa liczbę wierszy, które widżet ma zajmować.                                                 | `rowspan=2`                            |

**Przykład 1: Tworzenie prostego formularza**

Poniżej przedstawiono przykład tworzenia bardziej rozbudowanego formularza, gdzie etykiety i pola tekstowe są rozmieszczone w układzie tabelarycznym.

```python
labels = ["Name", "Email", "Age"]
for i, text in enumerate(labels):
    label = tk.Label(root, text=text)
    label.grid(row=i, column=0, sticky="w")
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
```

![Prosty formularz z polami dla imienia, emaila i wieku](https://github.com/user-attachments/assets/2b09ac65-d5f2-4d61-9a2f-5683bea71686)

Tutaj etykiety są wyrównane do lewej (`sticky="w"`), a każde pole tekstowe jest przypisane do kolumny po prawej stronie, co tworzy przejrzysty i uporządkowany wygląd formularza.

**Przykład 2: Rozciąganie elementu na dwie kolumny**

W przypadku, gdy widżet, taki jak etykieta statusu, ma zajmować więcej miejsca (np. całą szerokość okna), można użyć parametru `columnspan`, aby rozciągnąć go na kilka kolumn.

```python
status_label = tk.Label(root, text="Status: Ready", bg="lightgrey")
status_label.grid(row=3, column=0, columnspan=2, sticky="we")  # Rozciągnięcie na 2 kolumny
```

![Etykieta statusu rozciągnięta na dwie kolumny](https://github.com/user-attachments/assets/db27e15f-3533-451e-aef8-6d2a71cf1c9d)

Dzięki `columnspan=2`, etykieta statusu zajmuje obie kolumny, co pozwala jej się rozciągnąć na całą szerokość. `sticky="we"` sprawia, że widżet przylega do lewej i prawej strony, co dodatkowo poprawia estetykę.

#### III. Metoda `place()`

Metoda `place()` umożliwia precyzyjne pozycjonowanie widżetów za pomocą współrzędnych `x` i `y`, co pozwala na pełną kontrolę nad ich umiejscowieniem w oknie. Jest to przydatne, gdy chcemy rozmieścić widżety w dokładnie określonych miejscach lub tworzyć bardziej nietypowe układy. Wadą tej metody jest konieczność znajomości wymiarów okna oraz widżetów, co sprawia, że metoda `place()` jest mniej elastyczna od `pack()` czy `grid()`.

Poniższy przykład pokazuje, jak umieścić przycisk w określonej pozycji za pomocą `x=50` oraz `y=100`.

```python
import tkinter as tk

root = tk.Tk()
button = tk.Button(root, text="Click me")
button.place(x=50, y=100)

root.mainloop()
```

![Pozycjonowanie przycisku w oknie za pomocą współrzędnych](https://github.com/user-attachments/assets/ba99c93c-34be-447b-8e03-6b1dfacbbe53)

W tym przykładzie przycisk jest umieszczony w pozycji (50, 100) względem lewego górnego rogu okna.

Parametry metody `place()`:

| Parametr  | Opis                                                                                               | Przykład                   |
|-----------|----------------------------------------------------------------------------------------------------|----------------------------|
| `x`       | Pozycja widżetu na osi X w pikselach (od lewej krawędzi okna).                                     | `x=100`                    |
| `y`       | Pozycja widżetu na osi Y w pikselach (od górnej krawędzi okna).                                    | `y=50`                     |
| `relx`    | Pozycja widżetu na osi X jako część całkowitej szerokości (np. `relx=0.5` umieszcza na środku).   | `relx=0.5`                 |
| `rely`    | Pozycja widżetu na osi Y jako część całkowitej wysokości (np. `rely=0.5` umieszcza na środku).     | `rely=0.5`                 |
| `anchor`  | Punkt odniesienia, względem którego widżet jest pozycjonowany. Możliwe wartości: `n`, `s`, `e`, `w`, `center` itd. | `anchor="center"`         |
| `width`   | Szerokość widżetu w pikselach.                                                                     | `width=200`                |
| `height`  | Wysokość widżetu w pikselach.                                                                      | `height=50`                |

**Przykład 1: Pozycjonowanie elementu na środku okna**

Poniżej znajduje się przykład ustawienia przycisku w samym środku okna. Parametry `relx=0.5` i `rely=0.5` umieszczają przycisk na 50% szerokości i 50% wysokości okna, a `anchor="center"` sprawia, że środek przycisku jest odniesieniem tej pozycji.

```python
button = tk.Button(root, text="Center")
button.place(relx=0.5, rely=0.5, anchor="center")
```

![Pozycjonowanie przycisku na środku okna](https://github.com/user-attachments/assets/433cd17b-2078-4e20-9397-0712533fbdc2)

**Przykład 2: Tworzenie layoutu na podstawie współrzędnych**

W tym przykładzie rozmieszczamy kilka etykiet w oknie, każdą w różnych pozycjach zdefiniowanych przez `x` i `y`, co tworzy bardziej nieregularny układ.

```python
label1 = tk.Label(root, text="Label 1")
label1.place(x=10, y=10)

label2 = tk.Label(root, text="Label 2")
label2.place(x=10, y=50)

label3 = tk.Label(root, text="Label 3")
label3.place(x=100, y=100)
```

![Układ etykiet na różnych współrzędnych](https://github.com/user-attachments/assets/8beb3511-2678-403f-b870-5ac35d39c10c)

Dzięki zastosowaniu `x` i `y`, każda etykieta jest umieszczona w precyzyjnie określonej pozycji, tworząc unikalny układ na potrzeby bardziej skomplikowanych projektów interfejsu.

### Organizacja widżetów za pomocą ramek

Ramki (`Frame`) są kontenerami, które grupują widżety i pomagają organizować bardziej złożone układy.

**Przykład użycia ramek**

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

**Popularne Zdarzenia**

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

**Metoda `bind()`**

Aby powiązać zdarzenie z konkretną funkcją obsługującą, używamy metody `bind()`. Funkcje te przyjmują argument `event`, który zawiera szczegóły zdarzenia (takie jak pozycja kursora czy informacje o klawiszach modyfikujących).

**Przykład obsługi zdarzeń myszy**

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

**Przykład obsługi klawisza**

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

**Przykład — Łączenie zdarzeń na przycisku**

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

**Przykład własnego dekoratora `event_handler`**

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

**Przykład — Dodanie przycisku zamykającego aplikację**

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

**Alternatywne zamknięcie aplikacji**

Możemy także przypisać zamknięcie aplikacji do klawisza, na przykład `Escape`.

```python
root.bind("<Escape>", lambda event: root.destroy())
```
