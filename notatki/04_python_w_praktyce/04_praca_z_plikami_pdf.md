## Manipulacja i analiza plików PDF

Praca z plikami PDF w Pythonie jest możliwa dzięki kilku dostępnym bibliotekom. Jednym z najpopularniejszych narzędzi służących do tego celu jest `PyPDF2`.

### Instalacja biblioteki PyPDF2

Aby rozpocząć pracę z `PyPDF2`, najpierw trzeba ją zainstalować. Można to zrobić przy pomocy menedżera pakietów `pip`:

```bash
pip install pypdf2
```

### Otwieranie pliku PDF

Korzystając z `PyPDF2`, możemy łatwo otworzyć i przeczytać plik PDF:

```python
from PyPDF2 import PdfFileReader

# Otwieranie pliku PDF
with open('plik.pdf', 'rb') as plik:
    czytnik = PdfFileReader(plik)
```

'rb' w funkcji open oznacza tryb "odczyt binarny", który jest wymagany do czytania plików PDF.

### Eksploracja informacji o pliku

Dzięki `PyPDF2` możemy także uzyskać różne informacje o pliku PDF, takie jak:

- Liczba stron.
- Autor.
- Tytuł.

```python
print(f"Ilość stron: {czytnik.getNumPages()}")
informacje = czytnik.getDocumentInfo()
print(f"Autor: {informacje.author}")
print(f"Tytuł: {informacje.title}")
```

### Eksploracja zawartości pliku PDF

Aby uzyskać dostęp do treści strony w pliku PDF, możemy skorzystać z metody `getPage()`, która zwraca obiekt `PageObject` reprezentujący daną stronę. Natomiast metoda `getNumPages()` informuje nas o liczbie stron w dokumencie.

Poniższy fragment kodu prezentuje, jak wyświetlić zawartość wszystkich stron pliku PDF:

```python
liczba_stron = czytnik.getNumPages()

for nr_strony in range(liczba_stron):
    strona = czytnik.getPage(nr_strony)
    tekst = strona.extractText()
    print(tekst)
```

### Modyfikowanie dokumentów PDF

Jeśli chcemy dokonać modyfikacji w pliku PDF, możemy skorzystać z obiektu `PdfFileWriter` dostępnego w module `PyPDF2`. Umożliwia on dodawanie nowych stron, usuwanie istniejących czy wprowadzanie innych zmian.

Przykład poniżej przedstawia, jak dodać nową stronę z tekstem "Hello, World!" do dokumentu:

```python
from PyPDF2 import PdfFileWriter

writer = PdfFileWriter()

# Utworzenie nowej strony jest bardziej złożone niż w przykładzie
# Potrzebujemy modułu reportlab do generowania treści strony
from reportlab.pdfgen import canvas
from io import BytesIO

packet = BytesIO()
can = canvas.Canvas(packet, pagesize=A4)
can.drawString(100, 750, "Hello, World!")
can.save()

packet.seek(0)
new_pdf = PdfFileReader(packet)
writer.addPage(new_pdf.getPage(0))

with open('nowy_plik.pdf', 'wb') as plik:
    writer.write(plik)
```

### Łączenie wielu plików PDF w jeden

Jeśli chcemy połączyć wiele plików PDF w jeden dokument, możemy użyć `PdfFileMerger`. Poniżej znajduje się fragment kodu, który demonstruje, jak to zrobić:

```python
from PyPDF2 import PdfFileMerger
import glob

pliki_pdf = glob.glob('*.pdf')
merger = PdfFileMerger()

for pdf in pliki_pdf:
    with open(pdf, 'rb') as plik:
        merger.append(plik)

with open('polaczony_dokument.pdf', 'wb') as wyjsciowy_plik:
    merger.write(wyjsciowy_plik)
```

Zwróć uwagę, że przy otwieraniu plików używamy kontekstu with, aby zapewnić prawidłowe zarządzanie zasobami i zamknięcie plików po ich użyciu.
