
## Praca z plikami PDF
Istnieje kilka popularnych bibliotek do obsługi plików PDF. Jedną z najczęściej używanych jest biblioteka <code>PyPDF2</code>. Aby ją zainstalować, możemy użyć polecenia <code>pip install pypdf2</code>.

### Otwieranie pliku PDF

Aby otworzyć plik PDF, używamy funkcji `PdfFileReader` z modułu `PyPDF2`.

```python
from PyPDF2 import PdfFileReader

# otworz plik
with open('plik.pdf', 'rb') as plik:
    reader = PdfFileReader(plik)
```

### Wypisywanie informacji o pliku

Aby wyświetlić informacje o pliku, takie jak ilość stron, autor czy tytuł, możemy skorzystać z odpowiednich właściwości obiektu <code>PdfFileReader</code>:

```python
print(f"Ilość stron: {czytnik.getNumPages()}")
print(f"Autor: {czytnik.getDocumentInfo().author}")
print(f"Tytuł: {czytnik.getDocumentInfo().title}")
```

### Odczytywanie tekstu

Aby wyświetlić zawartość pliku PDF, możemy użyć metody `getPage()`. Metoda `getPage()` oczekuje obiektu `PageObject` reprezentującego daną stronę. Metoda `getNumPages()` zwraca liczbę stron w pliku.

Poniższy kod wyświetla zawartość wszystkich stron pliku PDF:

```python
# pobierz liczbe stron
liczba_stron = reader.getNumPages()

# dla kazdej strony
for strona in range(liczba_stron):
    # pobierz tekst strony
    tekst = reader.getPage(strona).extractText()
    # wyswietl tekst
    print(tekst)
```

### Modyfikowanie pliku PDF

Aby modyfikować plik PDF, możemy użyć obiektu `PdfFileWriter` z modułu `PyPDF2`. Możemy dodawać nowe strony do pliku lub usuwać istniejące strony.

Poniższy kod dodaje nową stronę z tekstem "Hello, World!" do pliku:

```python
# utworz obiekt PdfFileWriter
writer = PdfFileWriter()

# dodaj nowa strone z tekstem
writer.addPage(writer.newTextPage("Hello, World!"))

# otworz plik do zapisu
with open('nowy_plik.pdf', 'wb') as plik:
    # zapisz plik
    writer.write(plik)
```

### Łączenie plików PDF

Możemy użyć poniższego kodu, aby połączyć wszystkie pliki PDF z listy:

```python
import os
import glob
from PyPDF2 import PdfFileMerger

# utworzenie listy plikow
pdf_files = []
for filename in glob.glob('*.pdf'):
    pdf_files.append(filename)

# utworzenie obiektu merger
merger = PdfFileMerger()

# laczenie plikow
for pdf in pdf_files:
    merger.append(open(pdf, 'rb'))

# zapis nowego pliku
with open('sciezka/do/nowego_pliku.pdf', 'wb') as fout:
    merger.write(fout)
```
