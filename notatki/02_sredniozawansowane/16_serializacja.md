## Serializacja

Serializacja to proces konwersji obiektu (lub struktury danych) na postać, która może być łatwo zapisana, przesyłana lub przechowywana. Głównym celem jest przechowywanie stanu obiektu lub przesyłanie go pomiędzy różnymi systemami lub aplikacjami.

W Pythonie istnieje wiele narzędzi do serializacji, ale jednym z najbardziej podstawowych jest moduł `pickle`. Moduł ten umożliwia konwersję dowolnego obiektu Pythona na strumień bajtów i odwrotnie.

### Przykład użycia `pickle`

Poniżej znajduje się przykład, jak można serializować i deserializować obiekt klasy `Czlowiek`:

```python
import pickle

class Czlowiek:
    def __init__(self, imie, numer):
        self.imie = imie
        self.numer = numer

    def __repr__(self):
        return f'Imie: {self.imie}, Numer: {self.numer}'

sciezka = 'przyklad.pickle'

# Serializacja
with open(sciezka, 'wb') as plik:
    pickle.dump(Czlowiek('James', 10), plik)

# Deserializacja
with open(sciezka, 'rb') as plik:
    czlowiek = pickle.load(plik)
    print(czlowiek)  # Wyjście: Imie: James, Numer: 10
```

### Ostrzeżenie dotyczące bezpieczeństwa

Chociaż pickle jest bardzo potężnym narzędziem, może być niebezpieczny. Nigdy nie należy deserializować danych otrzymanych od nieznanych lub niezaufanych źródeł, ponieważ może to prowadzić do wykonywania złośliwego kodu. W takich przypadkach lepiej korzystać z formatów danych takich jak JSON lub XML, które są bardziej ograniczone pod względem funkcjonalności, ale są bezpieczne.

### Alternatywne narzędzia do serializacji

Choć pickle jest często używany, istnieją też inne popularne narzędzia do serializacji w Pythonie, takie jak `json` (dla formatu JSON) czy `xml.etree.ElementTree` (dla formatu XML). Wybór narzędzia zależy od potrzeb projektu i wymagań bezpieczeństwa.
