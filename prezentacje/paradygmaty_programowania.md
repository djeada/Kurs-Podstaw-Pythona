Paradygmat ogólnie: przejście z jednego światopoglądu na inny (geocentryzm -> heliocentryzm). 

Paradygmat w programowaniu określa zbiór mechanizmów dostępnych w składni danego języka, przy pomocy których budujemy programy.

Klasyfikacja:

1. Imperatywne:
   Kod składa się z sekwencji instrukcji modyfikujących stan programu (bottom-up).
  - Proceduralny: istnieje możliwość pogrupowania kodu w funkcje.
  - Obiektowy: istnieje możliwość pogrupowania kodu w klasy zbudowane z pól (określających stan) oraz metod (modyfikujących stan).
2. Deklaratywne
  Kod składa się z instrukcji wskazujących na pożądany stan programu bez konieczności definiowania wszystkich kroków prowadzących do tego stanu (top-bottom).
  - Funkcyjny: składają się z funkcji wzorowanych na wyrażeniach matematycznych. 
  - Logiczny: kod składa się z zestawu zależności, a obliczenia są dowodem pewnego twierdzenia na podstawie tych zależności. 

Współczesne języki mieszają paradygmaty.

## Stan

* stateful vs stateless


## Zmienność danych

* mutability vs immutability

## Czystość 

Funkcja jest funkcją czystą jeśli nie modyfikuje danych, których nie jest właścicielem. 

Zalety:
* czytelność kodu
* optymalizacja kodu w czasie kompilacji
* brak zjawiska wyścigu w programowaniu współbieżnym

## Literatura

* https://web.mit.edu/6.005/www/fa15/classes/09-immutability/
