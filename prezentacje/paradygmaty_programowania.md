Paradygmat ogólnie: przejście z jednego światopoglądu na inny (geocentryzm -> heliocentryzm). 

Paradygmat w programowaniu określa zbiór mechanizmów dostępnych w składni danego języka, przy pomocy których budujemy programy.

Klasyfikacja:

1. Imperatywne:
   Kod składa się z sekwencji instrukcji modyfikujących stan programu (bottom-up).
  - Proceduralny: kod składa się z funkcji bez klas.
  - Obiektowy: kod składają się z klas zbudowanych z pól (określających stan) oraz metod (modyfikujących stan).
2. Deklaratywne
  Kod składa się z instrukcji wskazujących na pożądany stan programu bez konieczności definiowania wszystkich kroków prowadzących do tego stanu (top-bottom).
  - Funkcyjny: składają się z funkcji wzorowanych na wyrażeniach matematycznych. 
  - Logiczny: kod składa się z zestawu zależności, a obliczenia są dowodem pewnego twierdzenia na podstawie tych zależności. 

Współczesne języki mieszają paradygmaty.

## Stan

* statefull vs stateless


## Zmienność danych

* mutability vs immutability

## Czystość 

Funkcja jest funkcją czystą jeśli nie modyfikuje danych, których nie jest właścicielem. 

Zalety:
* czytelność kodu
* optymalizacja kodu w czasie kompilacji
* brak zjawiska wyścigu w programowaniu współbieżnym
