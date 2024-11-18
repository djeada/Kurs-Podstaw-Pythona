## Manipulacja i analiza plików PDF

Praca z plikami PDF w Pythonie jest możliwa dzięki kilku dostępnym bibliotekom. Jednym z najpopularniejszych narzędzi służących do tego celu jest **PyPDF2**.

### Wprowadzenie do PyPDF2

- **PyPDF2** to biblioteka w języku Python, która umożliwia manipulowanie plikami PDF, takimi jak odczytywanie zawartości, modyfikowanie, łączenie i dzielenie dokumentów.
- Biblioteka ta jest wolna od zależności od zewnętrznych narzędzi, co sprawia, że jest łatwa w instalacji i użyciu.
- Dzięki **PyPDF2** programiści mogą automatyzować procesy związane z dokumentami PDF, co jest szczególnie przydatne w aplikacjach biznesowych i naukowych.

### Instalacja biblioteki PyPDF2

Aby rozpocząć pracę z **PyPDF2**, najpierw należy ją zainstalować przy użyciu menedżera pakietów `pip`, co można zrobić za pomocą polecenia:

```bash
pip install PyPDF2
```

- Upewnij się, że używasz odpowiedniej wielkości liter w nazwie pakietu, ponieważ w nowszych wersjach nazwa pakietu to **PyPDF2**, a nie `pypdf2`.
- Po pomyślnej instalacji warto sprawdzić wersję zainstalowanej biblioteki, aby upewnić się, że korzystasz z najnowszej.

### Otwieranie i odczytywanie pliku PDF

Możemy łatwo otworzyć plik PDF w trybie **odczytu binarnego** (`'rb'`), który jest wymagany do prawidłowego przetwarzania plików PDF.

```python
from PyPDF2 import PdfFileReader

with open('plik.pdf', 'rb') as plik:
  czytnik = PdfFileReader(plik)
```

- Metoda `PdfFileReader` tworzy obiekt, który pozwala na interakcję z zawartością pliku PDF.
- **Tryb binarny** jest niezbędny, ponieważ pliki PDF zawierają dane binarne, które mogą być niepoprawnie odczytane w trybie tekstowym.

### Eksploracja informacji o pliku PDF

- Za pomocą obiektu `PdfFileReader` możemy uzyskać różne **metadane** dokumentu, takie jak liczba stron, autor czy tytuł.
- Aby uzyskać **liczbę stron**, używamy metody `getNumPages()`, która zwraca całkowitą liczbę stron w dokumencie.

```python
liczba_stron = czytnik.getNumPages()
print(f"Liczba stron: {liczba_stron}")
```

 Metoda `getDocumentInfo()` zwraca obiekt zawierający **informacje o dokumencie**, które można wyświetlić lub przetworzyć.

```python
informacje = czytnik.getDocumentInfo()
print(f"Autor: {informacje.author}")
print(f"Tytuł: {informacje.title}")
```

Metadane mogą być przydatne przy katalogowaniu dokumentów lub wyświetlaniu informacji w interfejsie użytkownika.

### Odczytywanie zawartości stron

Aby uzyskać dostęp do treści konkretnej strony, używamy metody `getPage(nr_strony)`, która zwraca obiekt reprezentujący daną stronę.

```python
strona = czytnik.getPage(0)  # Pobiera pierwszą stronę
```

Możemy następnie wyodrębnić tekst ze strony za pomocą metody `extractText()`.

```python
tekst = strona.extractText()
print(tekst)
```

- **Uwaga**: Metoda `extractText()` może nie zawsze działać poprawnie z nowszymi formatami PDF lub jeśli dokument zawiera niestandardowe czcionki czy układy.
- W przypadku problemów z ekstrakcją tekstu warto rozważyć użycie alternatywnych bibliotek, takich jak **PDFMiner**.

### Iterowanie przez wszystkie strony dokumentu

Jeśli chcemy przetworzyć cały dokument, możemy iterować przez wszystkie strony za pomocą pętli `for`.

```python
for nr_strony in range(liczba_stron):
  strona = czytnik.getPage(nr_strony)
  tekst = strona.extractText()
  print(f"Strona {nr_strony + 1}:")
  print(tekst)
```

- Iteracja pozwala na masowe przetwarzanie dokumentu, co jest przydatne w przypadku dużych plików.
- Możemy także zbierać tekst ze wszystkich stron do jednego ciągu znaków lub listy, aby łatwiej go analizować.

### Modyfikowanie dokumentów PDF

Do modyfikacji dokumentów PDF używamy obiektu **PdfFileWriter**, który pozwala na tworzenie nowych dokumentów lub modyfikowanie istniejących.

```python
from PyPDF2 import PdfFileWriter

pisarz = PdfFileWriter()
```

Możemy dodawać strony do nowego dokumentu za pomocą metody `addPage()`.

```python
strona = czytnik.getPage(0)
pisarz.addPage(strona)
```

**PdfFileWriter** nie modyfikuje istniejącego dokumentu, ale tworzy nowy, co jest ważne dla zachowania integralności oryginalnych plików.

### Dodawanie nowej strony z tekstem

Aby dodać nową stronę z własnym tekstem, potrzebujemy dodatkowej biblioteki, takiej jak **ReportLab**, która umożliwia generowanie stron PDF.

```bash
pip install reportlab
```

Następnie tworzymy nową stronę za pomocą **canvas** z **ReportLab**.

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO

packet = BytesIO()
can = canvas.Canvas(packet, pagesize=A4)
can.drawString(100, 750, "Hello, World!")
can.save()
```

Po utworzeniu nowej strony, integrujemy ją z istniejącym dokumentem za pomocą **PyPDF2**.

```python
packet.seek(0)
nowy_pdf = PdfFileReader(packet)
pisarz.addPage(nowy_pdf.getPage(0))
```

Proces ten pozwala na tworzenie złożonych dokumentów z własnymi treściami i istniejącymi stronami.

### Zapisywanie zmodyfikowanego dokumentu

Aby zapisać nowy lub zmodyfikowany dokument, używamy metody `write()` obiektu **PdfFileWriter**.

```python
with open('nowy_plik.pdf', 'wb') as plik_wyjsciowy:
  pisarz.write(plik_wyjsciowy)
```

- **Tryb zapisu binarnego** (`'wb'`) jest konieczny, aby plik został zapisany poprawnie.
- Po zapisaniu warto otworzyć plik, aby upewnić się, że wszystkie zmiany zostały wprowadzone zgodnie z oczekiwaniami.

### Łączenie wielu plików PDF w jeden dokument

Do łączenia wielu plików PDF używamy klasy **PdfFileMerger** z biblioteki **PyPDF2**.

```python
from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()
```

Możemy dodawać pliki do obiektu `merger` za pomocą metody `append()`.

```python
pliki_do_polaczenia = ['plik1.pdf', 'plik2.pdf', 'plik3.pdf']
for plik_pdf in pliki_do_polaczenia:
  merger.append(plik_pdf)
```

Na koniec zapisujemy połączony dokument do nowego pliku.

```python
with open('polaczony_dokument.pdf', 'wb') as plik_wyjsciowy:
  merger.write(plik_wyjsciowy)
```

Łączenie plików jest szczególnie przydatne przy tworzeniu raportów zbiorczych lub kompilacji dokumentów.

### Dodatkowe funkcje PyPDF2

Możemy zabezpieczyć dokument hasłem za pomocą metody `encrypt()`.

```python
pisarz.encrypt(user_pwd='haslo_uzytkownika', owner_pwd='haslo_wlasciciela', use_128bit=True)
```

Możemy podzielić dokument na mniejsze części, wybierając konkretne strony do nowego dokumentu.

```python
# Dodajemy strony od 2 do 5
for nr_strony in range(1, 5):
  strona = czytnik.getPage(nr_strony)
  pisarz.addPage(strona)
```

Chociaż **PyPDF2** ma ograniczone wsparcie dla zakładek, możemy dodawać prosty **tekst** lub **adnotacje**.

```python
# Dodanie adnotacji na pierwszej stronie
page = reader.pages[0]  # Pobieramy pierwszą stronę

# Tworzymy adnotację (przykład prostego tekstu)
annotation = AnnotationBuilder.text(
    "To jest przykładowa adnotacja tekstowa!",
    rect=(100, 700, 300, 720),  # Współrzędne (x1, y1, x2, y2) prostokąta
    open=True  # Domyślnie otwarta adnotacja
)

# Dodajemy adnotację do strony
page.add_annotation(annotation)

# Dodajemy strony do nowego pliku PDF
for page in reader.pages:
    writer.add_page(page)
```

Możemy obrócić stronę o określony kąt za pomocą metody `rotateClockwise()`.

```python
strona = czytnik.getPage(0)
strona.rotateClockwise(90)
pisarz.addPage(strona)
```

### Obsługa wyjątków i błędów

Podczas pracy z plikami PDF mogą wystąpić różne błędy, dlatego ważne jest, aby implementować **obsługę wyjątków**.

```python
try:
  with open('plik.pdf', 'rb') as plik:
      czytnik = PdfFileReader(plik)
except FileNotFoundError:
  print("Plik nie został znaleziony.")
except Exception as e:
  print(f"Wystąpił błąd: {e}")
```

- Obsługa wyjątków zwiększa niezawodność aplikacji i pozwala na lepsze zarządzanie błędami.
- Warto również sprawdzać, czy plik PDF nie jest zaszyfrowany przed próbą jego odczytu.

### Alternatywne biblioteki do manipulacji plikami PDF

- **PDFMiner** jest biblioteką przeznaczoną do ekstrakcji tekstu z plików PDF, zapewniając skuteczność szczególnie w przypadku dokumentów zawierających różnorodne układy tekstu.
- **ReportLab** umożliwia tworzenie dokumentów PDF od podstaw, oferując zaawansowane możliwości związane z projektowaniem układów strony, dodawaniem grafiki oraz interaktywnych elementów.
- **pdfrw** pozwala na odczytywanie i modyfikowanie plików PDF bez potrzeby instalacji dodatkowych zależności, co czyni ją lekkim i prostym w użyciu narzędziem.
- **PyMuPDF**, znane również jako **Fitz**, oferuje szybkie i wydajne operacje na plikach PDF, w tym możliwość manipulacji obrazami, czcionkami oraz obiektami wektorowymi.
- **PyPDF2** jest często wybierane jako podstawowe narzędzie do pracy z plikami PDF ze względu na prostotę obsługi i szeroki zakres funkcjonalności, takich jak scalanie, dzielenie i szyfrowanie dokumentów.

### Praktyczne zastosowania manipulacji plikami PDF

- Generowanie raportów w formacie PDF pozwala na automatyczne tworzenie raportów na podstawie danych, co jest często wykorzystywane przez firmy do generowania raportów finansowych, które mogą być automatycznie tworzone i wysyłane do zainteresowanych stron.
- Przetwarzanie faktur umożliwia ekstrakcję danych z faktur w celu automatyzacji procesów księgowych, co pozwala na oszczędność czasu i redukcję błędów ludzkich przy wprowadzaniu danych.
- Łączenie dokumentów jest przydatne przy tworzeniu jednego dokumentu z wielu plików PDF, takich jak zestawy umów czy prezentacji, co ułatwia zarządzanie dokumentacją i jej dystrybucję.
- Dodawanie znaków wodnych do dokumentów pozwala na ich oznaczanie w celach bezpieczeństwa lub identyfikacji, co chroni przed nieautoryzowanym kopiowaniem i rozpowszechnianiem treści.
- Digitalizacja dokumentów umożliwia przetwarzanie zeskanowanych materiałów i konwersję ich do przeszukiwalnych plików PDF, co znacząco poprawia dostępność i organizację treści.

### Dobre praktyki

- Zarządzanie zasobami w pracy z plikami PDF jest bardziej efektywne, gdy używa się kontekstu `with` przy ich otwieraniu, ponieważ zapewnia to automatyczne zamknięcie plików, co zapobiega wyciekom pamięci i blokadom plików.
- Bezpieczeństwo jest kluczowe podczas pracy z plikami pochodzącymi z niezaufanych źródeł, dlatego warto upewnić się, że pliki nie zawierają złośliwego kodu lub nie są uszkodzone, aby uniknąć potencjalnych zagrożeń.
- Regularne aktualizacje biblioteki **PyPDF2** pozwalają na korzystanie z najnowszych funkcji i poprawek bezpieczeństwa, co jest istotne, ponieważ nowe wersje często zawierają ważne ulepszenia oraz naprawy błędów.
- Dokumentacja oficjalna oraz wsparcie społeczności mogą być cennym źródłem informacji, pomagając w rozwiązywaniu problemów oraz w nauce najlepszych praktyk dotyczących pracy z plikami PDF.
