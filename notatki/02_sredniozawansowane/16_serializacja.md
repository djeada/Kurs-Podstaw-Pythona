## Serializacja

Serializacja to proces przekształcania obiektu lub struktury danych w format, który można łatwo przechowywać lub przesyłać. Zserializowane dane można następnie przywrócić do ich oryginalnej postaci za pomocą procesu deserializacji. Serializacja jest szeroko stosowana w programowaniu do przesyłania danych między różnymi systemami, przechowywania ich w plikach, bazach danych, lub w celu tymczasowego przechowywania obiektów w pamięci.

```
+------------------+      Serializacja      +----------------+
| Obiekt Pythona   | ---------------------> | Bajty          |
+------------------+                        +----------------+
        Ʌ                                         |
        |                                         |
        | Deserializacja                          | Deserializacja
        |                                         |
        |                                         V
+------------------+      Serializacja      +-----------------+
| Bajty            | <--------------------- | Obiekt Pythona  |
+------------------+                        +-----------------+
```

### Zastosowania serializacji

- **Przechowywanie danych**: Zserializowane dane mogą być zapisane w plikach lub bazach danych, co pozwala na ich późniejsze odczytanie i przywrócenie do stanu pierwotnego.
- **Przesyłanie danych**: Serializacja umożliwia przesyłanie obiektów przez sieć, np. między różnymi komponentami aplikacji rozproszonych lub w komunikacji klient-serwer.
- **Klonowanie obiektów**: Proces serializacji i deserializacji może być użyty do głębokiego kopiowania obiektów, czyli tworzenia kopii obiektu wraz z wszystkimi zagnieżdżonymi obiektami.

### Przykład użycia `pickle`

W Pythonie istnieje wiele narzędzi do serializacji, ale jednym z najbardziej podstawowych jest moduł `pickle`. Moduł ten umożliwia konwersję dowolnego obiektu Pythona na strumień bajtów i odwrotnie. Poniżej znajduje się przykład, jak można serializować i deserializować obiekt klasy `Czlowiek`:

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

#### Ostrzeżenie dotyczące bezpieczeństwa

Chociaż `pickle` jest bardzo potężnym narzędziem, może być niebezpieczny. Nigdy nie należy deserializować danych otrzymanych od nieznanych lub niezaufanych źródeł, ponieważ może to prowadzić do wykonywania złośliwego kodu. W takich przypadkach lepiej korzystać z formatów danych takich jak JSON lub XML, które są bardziej ograniczone pod względem funkcjonalności, ale są bezpieczne.

Wyobraźmy sobie, że ktoś przesyła nam zserializowane dane, a my deserializujemy je za pomocą `pickle`:

```python
import pickle

# Otrzymane dane (mogą pochodzić z niezaufanego źródła)
data = b"cos zlośliwego"

# Deserializacja danych
obj = pickle.loads(data)
```

Jeśli dane zawierają złośliwy kod, jego wykonanie może prowadzić do poważnych konsekwencji, takich jak kradzież danych, uszkodzenie systemu, czy instalacja malware.

### Alternatywne narzędzia do serializacji

Choć `pickle` jest często używany, istnieją też inne popularne narzędzia do serializacji w Pythonie, takie jak `json` (dla formatu JSON) czy `xml.etree.ElementTree` (dla formatu XML). Wybór narzędzia zależy od potrzeb projektu i wymagań bezpieczeństwa.

#### Serializacja z użyciem `json`

Format JSON jest jednym z najpopularniejszych formatów do serializacji danych, szczególnie w kontekście komunikacji między aplikacjami webowymi.

```python
import json

class Czlowiek:
    def __init__(self, imie, numer):
        self.imie = imie
        self.numer = numer

    def to_dict(self):
        return {"imie": self.imie, "numer": self.numer}

    @classmethod
    def from_dict(cls, data):
        return cls(data['imie'], data['numer'])

# Serializacja
czlowiek = Czlowiek('James', 10)
json_str = json.dumps(czlowiek.to_dict())

# Deserializacja
data = json.loads(json_str)
czlowiek = Czlowiek.from_dict(data)
print(czlowiek)  # Wyjście: Imie: James, Numer: 10
```

#### Serializacja z użyciem `xml.etree.ElementTree`

XML jest innym popularnym formatem do serializacji danych, często używanym w kontekście wymiany danych między różnymi systemami.

```python
import xml.etree.ElementTree as ET

class Czlowiek:
    def __init__(self, imie, numer):
        self.imie = imie
        self.numer = numer

    def to_xml(self):
        czlowiek = ET.Element("Czlowiek")
        imie = ET.SubElement(czlowiek, "Imie")
        imie.text = self.imie
        numer = ET.SubElement(czlowiek, "Numer")
        numer.text = str(self.numer)
        return ET.tostring(czlowiek, encoding='unicode')

    @classmethod
    def from_xml(cls, data):
        element = ET.fromstring(data)
        imie = element.find("Imie").text
        numer = int(element.find("Numer").text)
        return cls(imie, numer)

# Serializacja
czlowiek = Czlowiek('James', 10)
xml_str = czlowiek.to_xml()

# Deserializacja
czlowiek = Czlowiek.from_xml(xml_str)
print(czlowiek)  # Wyjście: Imie: James, Numer: 10
```
