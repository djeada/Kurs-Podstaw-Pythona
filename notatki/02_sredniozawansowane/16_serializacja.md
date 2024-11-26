## Serializacja

Serializacja to proces przekształcania obiektów lub struktur danych w format, który można łatwo przechowywać, przesyłać i odtwarzać. Dzięki serializacji możemy zapisać stan obiektu w pliku, przesłać go przez sieć lub przechowywać w bazie danych, a następnie w dowolnym momencie przywrócić go do pierwotnej postaci poprzez deserializację. Jest to kluczowy mechanizm w programowaniu, który umożliwia efektywną wymianę danych między różnymi systemami i komponentami.

```
+--------------------+       Serializacja        +-----------------+
|    Obiekt Pythona  | ------------------------> |     Bajty        |
+--------------------+                           +-----------------+
        ^                                                  |
        |                                                  |
        |                 Deserializacja                   |
        |                                                  |
        |                                                  v
+--------------------+       Deserializacja       +-----------------+
|       Bajty        | <------------------------  |   Obiekt Pythona |
+--------------------+                           +-----------------+
```

### Zastosowania serializacji

Serializacja znajduje zastosowanie w wielu obszarach programowania:

- **Przechowywanie stanu obiektów**: Umożliwia zapisanie aktualnego stanu obiektów do pliku lub bazy danych, co pozwala na późniejsze odtworzenie ich w identycznym stanie. Jest to szczególnie przydatne w aplikacjach wymagających zachowania sesji użytkownika czy danych pomiędzy uruchomieniami programu.
- **Przesyłanie danych między systemami**: Dzięki serializacji możemy przesyłać złożone struktury danych przez sieć, np. między klientem a serwerem, nawet jeśli są napisane w różnych językach programowania.
- **Głębokie kopiowanie obiektów**: Proces serializacji i deserializacji pozwala na utworzenie głębokiej kopii obiektu, w którym wszystkie zagnieżdżone obiekty są również kopiowane.
- **Zachowanie kompatybilności danych**: Podczas migracji danych między różnymi wersjami aplikacji czy systemów, serializacja umożliwia zachowanie integralności i struktury danych.
- **Optymalizacja przechowywania**: Serializacja binarna może zmniejszyć rozmiar danych, co jest istotne w systemach o ograniczonej przestrzeni dyskowej lub przepustowości sieci.
- **Bezpieczeństwo danych**: Umożliwia szyfrowanie zserializowanych danych przed ich przesłaniem lub zapisaniem, co zwiększa poziom bezpieczeństwa aplikacji.
- **Interoperacyjność między językami**: Pozwala na wymianę danych między aplikacjami napisanymi w różnych językach programowania poprzez użycie uniwersalnych formatów, takich jak JSON czy XML.

### Serializacja z użyciem modułu `pickle`

W Pythonie jednym z podstawowych narzędzi do serializacji jest moduł `pickle`. Pozwala on na konwersję niemal dowolnych obiektów Pythona do ciągu bajtów i odwrotnie. Poniżej przedstawiono przykład, jak można zserializować i deserializować obiekt klasy `Czlowiek`:

```python
import pickle

class Czlowiek:
    def __init__(self, imie, numer):
        self.imie = imie
        self.numer = numer

    def __repr__(self):
        return f'Imię: {self.imie}, Numer: {self.numer}'

# Ścieżka do pliku, w którym zapiszemy dane
sciezka = 'przyklad.pickle'

# Serializacja obiektu
with open(sciezka, 'wb') as plik:
    obiekt = Czlowiek('James', 10)
    pickle.dump(obiekt, plik)

# Deserializacja obiektu
with open(sciezka, 'rb') as plik:
    obiekt = pickle.load(plik)
    print(obiekt)
```

Po uruchomieniu tego kodu, otrzymamy wynik:

```
Imię: James, Numer: 10
```

#### Ostrzeżenie dotyczące bezpieczeństwa

Korzystając z modułu `pickle`, należy zachować ostrożność. Deserializacja danych z niezaufanych źródeł może być niebezpieczna, ponieważ może prowadzić do wykonania złośliwego kodu. Dlatego zaleca się używanie `pickle` tylko z danymi pochodzącymi z zaufanych źródeł. W sytuacjach wymagających większego bezpieczeństwa warto rozważyć użycie innych formatów, takich jak JSON czy XML.

### Serializacja z użyciem modułu `json`

Format JSON (JavaScript Object Notation) jest jednym z najpopularniejszych formatów do wymiany danych między aplikacjami, zwłaszcza w kontekście aplikacji webowych. Python oferuje moduł `json`, który pozwala na serializację i deserializację obiektów do formatu JSON.

```python
import json

class Czlowiek:
    def __init__(self, imie, numer):
        self.imie = imie
        self.numer = numer

    def to_dict(self):
        return {'imie': self.imie, 'numer': self.numer}

    @classmethod
    def from_dict(cls, dane):
        return cls(dane['imie'], dane['numer'])

# Serializacja obiektu do JSON
obiekt = Czlowiek('James', 10)
json_str = json.dumps(obiekt.to_dict())
print(json_str)
```

Wynik:

```
{"imie": "James", "numer": 10}
```

Aby zdeserializować dane z formatu JSON:

```python
# Deserializacja obiektu z JSON
dane = json.loads(json_str)
obiekt = Czlowiek.from_dict(dane)
print(obiekt)
```

Wynik:

```
Imię: James, Numer: 10
```

### Serializacja z użyciem modułu `xml.etree.ElementTree`

Format XML (eXtensible Markup Language) jest kolejnym popularnym formatem do przechowywania i wymiany danych. W Pythonie możemy użyć modułu `xml.etree.ElementTree` do pracy z danymi XML.

```python
import xml.etree.ElementTree as ET

class Czlowiek:
    def __init__(self, imie, numer):
        self.imie = imie
        self.numer = numer

    def to_xml(self):
        czlowiek = ET.Element('Czlowiek')
        imie_elem = ET.SubElement(czlowiek, 'Imie')
        imie_elem.text = self.imie
        numer_elem = ET.SubElement(czlowiek, 'Numer')
        numer_elem.text = str(self.numer)
        return ET.tostring(czlowiek, encoding='unicode')

    @classmethod
    def from_xml(cls, xml_data):
        root = ET.fromstring(xml_data)
        imie = root.find('Imie').text
        numer = int(root.find('Numer').text)
        return cls(imie, numer)

# Serializacja obiektu do XML
obiekt = Czlowiek('James', 10)
xml_str = obiekt.to_xml()
print(xml_str)
```

Wynik:

```xml
<Czlowiek><Imie>James</Imie><Numer>10</Numer></Czlowiek>
```

Deserializacja z XML:

```python
# Deserializacja obiektu z XML
obiekt = Czlowiek.from_xml(xml_str)
print(obiekt)
```

Wynik:

```
Imię: James, Numer: 10
```

### Diagram ilustrujący proces serializacji

Aby lepiej zrozumieć proces serializacji i deserializacji, spójrzmy na poniższy diagram:

```
+-----------------------+
|     Obiekt Pythona    |
+-----------+-----------+
            |
            |  Serializacja
            v
+-----------------------+
|     Format danych     |
|   (JSON, XML, bajty)  |
+-----------+-----------+
            |
            |  Deserializacja
            v
+-----------------------+
|     Obiekt Pythona    |
+-----------------------+
```

Proces ten polega na przekształceniu obiektu Pythona w format danych, który można łatwo przechowywać lub przesyłać, a następnie przywróceniu go do pierwotnej postaci.

### Praktyczne zastosowanie serializacji

Wyobraźmy sobie aplikację, w której użytkownik tworzy złożone obiekty, takie jak profile użytkowników, konfiguracje czy stany gry. Chcemy umożliwić zapisanie tych obiektów do pliku, aby można było je później wczytać lub przesłać innym użytkownikom.

#### Zapis stanu gry do pliku JSON

```python
import json

class Postac:
    def __init__(self, imie, poziom, ekwipunek):
        self.imie = imie
        self.poziom = poziom
        self.ekwipunek = ekwipunek

    def to_dict(self):
        return {
            'imie': self.imie,
            'poziom': self.poziom,
            'ekwipunek': self.ekwipunek
        }

    @classmethod
    def from_dict(cls, dane):
        return cls(dane['imie'], dane['poziom'], dane['ekwipunek'])

# Tworzenie obiektu postaci
postac = Postac('Aragorn', 20, ['Miecz', 'Tarcza', 'Pierścień'])

# Serializacja do JSON i zapis do pliku
with open('postac.json', 'w') as plik:
    json.dump(postac.to_dict(), plik)

# Deserializacja z pliku JSON
with open('postac.json', 'r') as plik:
    dane = json.load(plik)
    postac_wczytana = Postac.from_dict(dane)

print(f"Imię: {postac_wczytana.imie}, Poziom: {postac_wczytana.poziom}, Ekwipunek: {postac_wczytana.ekwipunek}")
```

Wynik:

```
Imię: Aragorn, Poziom: 20, Ekwipunek: ['Miecz', 'Tarcza', 'Pierścień']
```

#### Przesyłanie danych między aplikacjami

Jeśli chcemy przesłać dane między różnymi aplikacjami lub usługami sieciowymi, możemy użyć formatu JSON lub XML, który jest uniwersalny i obsługiwany przez wiele języków programowania.

### Uwagi dotyczące bezpieczeństwa

Podczas korzystania z serializacji, szczególnie z modułem `pickle`, należy być świadomym potencjalnych zagrożeń. Deserializacja danych z nieznanych źródeł może prowadzić do wykonania złośliwego kodu. Zawsze upewnij się, że dane pochodzą z zaufanego źródła lub używaj bezpieczniejszych metod serializacji, takich jak JSON, które nie wykonują kodu podczas deserializacji.
