## Serializacja

Serializacja to proces konwersji obiektu na strumień bajtów, który może być następnie zapisany, przesłany lub przechowywany w inny sposób. Dzięki serializacji możliwe jest zapisywanie stanu obiektów i ich późniejsze odtwarzanie, co może być przydatne np. w grach, gdzie chcemy zapisać postępy gracza lub w aplikacjach, gdzie chcemy zapisywać dane użytkownika.

Moduł `pickle` służy do serializacji i deserializacji obiektów. Funkcja `dumps()` pozwala na zserializowanie obiektu do strumienia bajtów, który może być następnie zapisany do pliku lub przesłany do innego procesu. Funkcja `loads()` pozwala na odtworzenie obiektu ze strumienia bajtów.

Przykład użycia tych funkcji znajduje się poniżej. W kodzie tworzona jest klasa `Czlowiek` z polami `imie` i `numer`, a następnie serializowana i zapisywana do pliku. Następnie obiekt jest odtwarzany z pliku i wyświetlany na ekranie.

```python
import pickle

class Czlowiek:
  def __init__(self, imie, numer):
    self.imie = imie
    self.numer = numer

  def __repr__(self):
    return f'Imie: {self.imie}, numer: {self.numer}'

sciekza = 'przyklad.pickle'

with open(sciekza, 'wb') as plik:
  pickle.dump(Czlowiek('James', 10), plik)


with open(sciekza, 'rb') as plik:
  czlowiek = pickle.load(plik)
  print(czlowiek) #Imie: James, numer: 10
```
