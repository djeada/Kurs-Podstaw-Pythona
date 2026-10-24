# Inżynieria oprogramowania w Pythonie — quiz

Notatki: [Moduły i pakiety](../notatki/03_inzynieria_oprogramowania/01_moduly_i_pakiety.md), [Wersje Pythona](../notatki/03_inzynieria_oprogramowania/02_wersje_pythona.md), [PIP i PyPI](../notatki/03_inzynieria_oprogramowania/03_pip_i_pypi.md), [Środowisko wirtualne](../notatki/03_inzynieria_oprogramowania/04_srodowisko_wirtualne.md), [Dbanie o jakość kodu](../notatki/03_inzynieria_oprogramowania/05_dbanie_o_jakosc_kodu.md), [Debugowanie](../notatki/03_inzynieria_oprogramowania/06_debugowanie.md), [Testy jednostkowe](../notatki/03_inzynieria_oprogramowania/07_testy_jednostkowe.md), [Dokumentacja](../notatki/03_inzynieria_oprogramowania/08_dokumentacja.md), [PyInstaller](../notatki/03_inzynieria_oprogramowania/09_pliki_wykonywalne_i_pyinstaller.md), [Kod bajtowy](../notatki/03_inzynieria_oprogramowania/10_kod_bajtowy.md), [Testy (prezentacja)](../notatki/05_prezentacje/testy.md), [Git (prezentacja)](../notatki/05_prezentacje/git.md)

Sprawdź, czy rozumiesz moduły, narzędzia do zarządzania wersjami i pakietami, jakość kodu, debugowanie, testy, dokumentację, PyInstaller i kod bajtowy.

#### Q. Jaką wartość ma zmienna `__name__` wewnątrz pliku `misja.py`, gdy zostaje on zaimportowany instrukcją `import misja`?

* [ ] `"__main__"`
* [x] `"misja"`
* [ ] `"misja.py"`
* [ ] `None`

> **Wyjaśnienie:** Przy imporcie `__name__` zawiera nazwę modułu. Wartość `"__main__"` pojawia się tylko wtedy, gdy plik jest uruchamiany bezpośrednio, i na tym opiera się warunek `if __name__ == "__main__":`.

#### Q. Co wypisze ten program?

```python
import pathlib
import sys

pathlib.Path("licznik_mod.py").write_text('print("ładuję moduł")\n', encoding="utf-8")
sys.path.insert(0, ".")

import licznik_mod
import licznik_mod
print("koniec")
```

* [ ] Dwa razy `ładuję moduł`, a potem `koniec`
* [x] Raz `ładuję moduł`, a potem `koniec`
* [ ] Tylko `koniec`
* [ ] Zgłosi `ImportError` przy drugim imporcie

> **Wyjaśnienie:** Kod modułu wykonuje się przy pierwszym imporcie, a gotowy moduł trafia do `sys.modules`. Kolejny `import` tej samej nazwy tylko pobiera go z tej pamięci podręcznej i nie uruchamia kodu ponownie.

#### Q. Co określa lista `__all__` zdefiniowana w pliku `__init__.py` pakietu?

* [ ] Kolejność, w jakiej Python ładuje moduły pakietu
* [x] Nazwy importowane przez `from pakiet import *`
* [ ] Moduły, których nie da się zaimportować z zewnątrz
* [ ] Zależności, które `pip` instaluje razem z pakietem

> **Wyjaśnienie:** `__all__` dotyczy tylko importu z gwiazdką: wskazuje, które nazwy mają zostać wtedy zaimportowane. Inne moduły nadal można zaimportować jawnie, np. `from pakiet import modul`.

#### Q. Plik `kalkulator/arytmetyka.py` zawiera import `from .geometry import oblicz_pole`. Co się stanie po uruchomieniu go bezpośrednio poleceniem `python kalkulator/arytmetyka.py`?

* [ ] Import zadziała, bo `geometry.py` leży w tym samym katalogu
* [ ] Python automatycznie potraktuje katalog jako pakiet
* [x] Zostanie zgłoszony `ImportError`: brak pakietu nadrzędnego
* [ ] Kropka zostanie zignorowana i import stanie się absolutny

> **Wyjaśnienie:** Import względny wymaga, by moduł był częścią pakietu. Uruchomiony bezpośrednio plik ma `__name__ == "__main__"` i nie zna pakietu nadrzędnego, więc kropka nie ma do czego się odnieść.

#### Q. Co wypisze ten program?

```python
from math import factorial as fac

print(fac(4), "factorial" in dir(), "fac" in dir())
```

* [ ] `24 True True`
* [ ] `24 True False`
* [x] `24 False True`
* [ ] Zgłosi `NameError`

> **Wyjaśnienie:** `from ... import ... as` dodaje do przestrzeni nazw tylko alias `fac`. Ani nazwa `factorial`, ani sam moduł `math` nie są wtedy dostępne w bieżącym module.

#### Q. Dlaczego nie należy nazywać własnego skryptu `random.py`?

* [ ] Bo Python zabrania nazw plików pokrywających się z nazwami modułów standardowych
* [ ] Bo `pip` usunie taki plik przy aktualizacji
* [x] Bo `import random` może wczytać ten plik zamiast modułu standardowego
* [ ] Bo pliki o takiej nazwie nie są kompilowane do kodu bajtowego

> **Wyjaśnienie:** Katalog uruchamianego skryptu jest na początku ścieżki wyszukiwania modułów, więc lokalny `random.py` przesłania moduł z biblioteki standardowej. Pojawiają się wtedy błędy typu `AttributeError: module 'random' has no attribute ...`.

#### Q. Który mechanizm ma najwyższy priorytet, gdy `pyenv` wybiera wersję Pythona?

* [ ] Plik `.python-version` w katalogu projektu
* [x] Zmienna środowiskowa `PYENV_VERSION`
* [ ] Wersja ustawiona przez `pyenv global`
* [ ] Wersja Pythona zainstalowana w systemie

> **Wyjaśnienie:** `pyenv` sprawdza najpierw `PYENV_VERSION`, potem plik `.python-version` (tworzony przez `pyenv local`), a na końcu wersję globalną. Dzięki temu można chwilowo nadpisać wersję projektu w jednej sesji terminala.

#### Q. W jaki sposób `pyenv` sprawia, że polecenie `python` uruchamia wybraną wersję interpretera?

* [ ] Podmienia systemowy plik `/usr/bin/python`
* [ ] Zmienia wpisy w rejestrze systemu operacyjnego
* [ ] Kompiluje Pythona od nowa przy każdej zmianie wersji
* [x] Dodaje na początek `PATH` katalog z „shimami”

> **Wyjaśnienie:** Shimy to małe skrypty o nazwach `python`, `pip` itd., które przechwytują wywołanie i przekazują je do wersji wybranej przez konfigurację `pyenv`. Systemowa instalacja Pythona pozostaje nietknięta.

#### Q. Które wersje pakietu spełniają wpis `sqlalchemy>=2.0,<3.0` w pliku `requirements.txt`?

* [x] Wersje od 2.0 włącznie do 3.0 wyłącznie
* [ ] Wyłącznie wersje 2.0 i 3.0
* [ ] Każda wersja od 2.0 wzwyż, również wszystkie wydania 3.x
* [ ] Najnowsza wersja z gałęzi 3.x

> **Wyjaśnienie:** Przecinek łączy warunki, więc oba muszą być spełnione naraz. Taki zakres przyjmuje poprawki z serii 2.x, a blokuje wersję 3.0, która może zawierać niezgodne zmiany.

#### Q. Do czego służy polecenie `pip freeze > requirements.txt`?

* [ ] Blokuje możliwość aktualizacji pakietów w bieżącym środowisku wirtualnym
* [x] Zapisuje zainstalowane pakiety wraz z dokładnymi wersjami
* [ ] Instaluje pakiety wymienione w pliku `requirements.txt`
* [ ] Tworzy kopię zapasową środowiska wirtualnego

> **Wyjaśnienie:** `pip freeze` wypisuje zainstalowane pakiety w formacie `nazwa==wersja`, a `>` przekierowuje to do pliku. Środowisko odtwarza się potem poleceniem `pip install -r requirements.txt`.

#### Q. Jak dziś wyszukać pakiet w indeksie PyPI?

* [ ] Poleceniem `pip search nazwa` wpisanym w terminalu
* [ ] Poleceniem `pip list --all nazwa`
* [x] Przez wyszukiwarkę na stronie pypi.org
* [ ] Poleceniem `pip show --remote nazwa`

> **Wyjaśnienie:** PyPI wyłączył interfejs, z którego korzystało `pip search`, więc to polecenie kończy się dziś błędem. Pakietów szuka się na stronie pypi.org, a `pip show` opisuje tylko pakiety już zainstalowane.

#### Q. Jak aktywować środowisko wirtualne `env` utworzone przez `venv` w systemie Linux?

* [x] `source env/bin/activate`
* [ ] `env\Scripts\activate`
* [ ] `python -m venv activate env`
* [ ] `pip activate env`

> **Wyjaśnienie:** W systemach uniksowych skrypt aktywujący leży w `env/bin/` i trzeba go wczytać do bieżącej powłoki przez `source`. Ścieżka `env\Scripts\activate` dotyczy systemu Windows.

#### Q. Które polecenie utworzy środowisko wirtualne bez instalowania dodatkowych narzędzi?

* [ ] `virtualenv env`
* [x] `python3 -m venv env`
* [ ] `conda create --name env`
* [ ] `pipenv install`

> **Wyjaśnienie:** Moduł `venv` jest częścią biblioteki standardowej od Pythona 3.3 (w Debianie i Ubuntu trzeba jedynie mieć pakiet systemowy `python3-venv`). `virtualenv` i `pipenv` trzeba doinstalować przez `pip`, a `conda` wymaga instalacji Anacondy lub Minicondy.

#### Q. Czym `conda` różni się od `venv`?

* [ ] Działa tylko w systemie Windows
* [ ] Nie potrafi izolować zależności projektów
* [x] Instaluje też Pythona i biblioteki spoza ekosystemu Pythona
* [ ] Wymaga, by wszystkie projekty używały tej samej wersji Pythona

> **Wyjaśnienie:** `conda` zarządza zarówno środowiskami, jak i pakietami, także interpreterem Pythona i bibliotekami C/C++. `venv` izoluje tylko pakiety Pythona i korzysta z interpretera, którym go uruchomiono.

#### Q. Jaką domyślną maksymalną długość linii stosuje formater Black?

* [ ] 79 znaków
* [x] 88 znaków
* [ ] 100 znaków
* [ ] 120 znaków

> **Wyjaśnienie:** Black domyślnie łamie linie dłuższe niż 88 znaków, co jest celowym, niewielkim odstępstwem od 79 znaków zalecanych w PEP 8. Wartość można zmienić opcją `--line-length`.

#### Q. Które z narzędzi samo przepisuje kod do jednolitego stylu, zamiast tylko zgłaszać problemy?

* [ ] Pylint
* [ ] Flake8
* [ ] mypy
* [x] Black

> **Wyjaśnienie:** Black jest formaterem: zmienia pliki tak, by miały jednolity styl. Pylint i Flake8 to lintery, które raportują problemy, a mypy sprawdza zgodność typów.

#### Q. Kiedy `mypy` wykryje błąd w wywołaniu `oblicz_vat("100")`, jeśli parametr funkcji ma adnotację `kwota: float`?

* [ ] Dopiero gdy program w trakcie działania dojdzie do tego wywołania
* [x] Podczas analizy kodu, bez uruchamiania programu
* [ ] Przy kompilacji pliku do kodu bajtowego
* [ ] Wcale, bo `mypy` sprawdza tylko formatowanie

> **Wyjaśnienie:** `mypy` jest narzędziem analizy statycznej: czyta kod i adnotacje typów, nie wykonując programu. Sam interpreter adnotacji nie sprawdza, więc bez `mypy` błąd wyszedłby dopiero w czasie działania (o ile w ogóle).

#### Q. Jak według PEP 8 powinna być zapisana nazwa stałej?

* [ ] `maxRozmiar`
* [ ] `MaxRozmiar`
* [ ] `max_rozmiar`
* [x] `MAX_ROZMIAR`

> **Wyjaśnienie:** PEP 8 zaleca dla stałych wielkie litery z podkreśleniami. `snake_case` służy do zmiennych i funkcji, `PascalCase` do nazw klas, a `camelCase` nie jest konwencją Pythona.

#### Q. Co robi wbudowana funkcja `breakpoint()` (Python 3.7+)?

* [ ] Przerywa program i zapisuje stan do pliku
* [x] Zatrzymuje program i uruchamia debuger, domyślnie `pdb`
* [ ] Zgłasza wyjątek, który kończy działanie programu
* [ ] Wypisuje wartości wszystkich zmiennych lokalnych i kontynuuje działanie programu

> **Wyjaśnienie:** `breakpoint()` to wygodny odpowiednik `import pdb; pdb.set_trace()`. Program zatrzymuje się w tym miejscu, a w sesji debugera można podglądać i zmieniać zmienne oraz wykonywać kod krok po kroku.

#### Q. Czym w debugerze `pdb` różni się polecenie `n` (next) od `s` (step)?

* [x] `n` wykonuje linię bez wchodzenia do funkcji, `s` wchodzi do jej środka
* [ ] `n` przechodzi do następnego breakpointa, a `s` tylko do następnej linii kodu
* [ ] `n` cofa wykonanie o linię, `s` przesuwa je o linię
* [ ] Oba polecenia działają identycznie, różnią się tylko nazwą

> **Wyjaśnienie:** `next` traktuje wywołanie funkcji w bieżącej linii jako jeden krok, a `step` zatrzymuje się na pierwszej linii wywoływanej funkcji. Do następnego breakpointa przechodzi `c` (continue).

#### Q. Co się stanie z instrukcją `assert x > 0`, gdy uruchomisz program poleceniem `python -O skrypt.py`?

* [ ] Zgłosi `AssertionError` niezależnie od `x`
* [x] Zostanie pominięta
* [ ] Zamieni się w ostrzeżenie `warnings.warn`
* [ ] Spowoduje błąd składni

> **Wyjaśnienie:** Flaga `-O` usuwa instrukcje `assert` z kodu. Dlatego asercje służą do sprawdzania założeń podczas tworzenia programu, a warunki ważne dla bezpieczeństwa sprawdza się przez `if ...: raise`.

#### Q. Którego narzędzia użyjesz, aby sprawdzić, w których funkcjach program spędza najwięcej czasu?

* [ ] `timeit`
* [ ] `pdb`
* [x] `cProfile`
* [ ] `traceback`

> **Wyjaśnienie:** `cProfile` mierzy liczbę wywołań i czas każdej funkcji w całym programie. `timeit` dokładnie mierzy czas pojedynczego fragmentu kodu, ale nie pokazuje rozkładu czasu na funkcje.

#### Q. Jaka jest właściwa kolejność kroków w cyklu TDD?

* [ ] Kod → test → refaktoryzacja
* [x] Test (czerwony) → minimalny kod → refaktoryzacja
* [ ] Refaktoryzacja → test → kod
* [ ] Kod → refaktoryzacja → test, który od razu przechodzi

> **Wyjaśnienie:** W TDD najpierw powstaje test opisujący nowe zachowanie i nie przechodzi on (czerwony). Potem dopisuje się minimalny kod, by test przeszedł (zielony), a na końcu porządkuje się kod, pilnując, by testy dalej przechodziły.

#### Q. Co ten program wypisze na standardowe wyjście (pomijając raport `unittest` na `stderr`)?

```python
import unittest

class T(unittest.TestCase):
    def setUp(self):
        print("setUp", end=" ")

    def tearDown(self):
        print("tearDown", end=" ")

    def test_a(self):
        print("a", end=" ")

    def test_b(self):
        print("b", end=" ")

unittest.main(argv=["x"], exit=False, verbosity=0)
```

* [ ] `setUp a b tearDown`
* [x] `setUp a tearDown setUp b tearDown`
* [ ] `a b`
* [ ] `setUp setUp a b tearDown tearDown`

> **Wyjaśnienie:** `setUp` i `tearDown` wykonują się przed i po każdym teście osobno, dzięki czemu każdy test dostaje świeże środowisko. Do jednorazowego przygotowania całej klasy służy `setUpClass`.

#### Q. Którą z tych funkcji w pliku `test_mat.py` pytest domyślnie uruchomi jako test?

* [x] `test_dodaj`
* [ ] `dodaj_test`
* [ ] `sprawdz_dodawanie`
* [ ] `wynik_testu`

> **Wyjaśnienie:** Domyślnie pytest zbiera z plików `test_*.py` funkcje, których nazwa zaczyna się od `test`. Funkcje z `test` w środku lub na końcu nazwy nie są uruchamiane.

#### Q. Co wypisze ten program?

```python
import unittest

class T(unittest.TestCase):
    def test_x(self):
        with self.assertRaises(ValueError):
            int("abc")
        print("po bloku", end=" ")

wynik = unittest.main(argv=["x"], exit=False, verbosity=0)
print(wynik.result.wasSuccessful())
```

* [ ] Zgłosi nieobsłużony `ValueError`
* [ ] `False`
* [x] `po bloku True`
* [ ] `po bloku False`

> **Wyjaśnienie:** Blok `assertRaises` oczekuje wyjątku `ValueError`; gdy go dostanie, przechwytuje go i test idzie dalej. Test nie przeszedłby, gdyby `int("abc")` nie zgłosiło wyjątku.

#### Q. Co wypisze ten program?

```python
from unittest.mock import MagicMock

m = MagicMock(return_value=42)
print(m(1, 2), m.call_count)
m.assert_called_with(1, 2)
print("ok")
```

* [ ] `None 1`, a potem `ok`
* [x] `42 1`, a potem `ok`
* [ ] `42 0`, a potem `AssertionError`
* [ ] `MagicMock 1`, a potem `ok`

> **Wyjaśnienie:** Obiekt `MagicMock` z ustawionym `return_value` przy każdym wywołaniu zwraca tę wartość i zapamiętuje argumenty. `assert_called_with` sprawdza ostatnie wywołanie i milczy, gdy argumenty się zgadzają.

#### Q. Który rodzaj testów powinien stanowić największą część zestawu według proporcji z książki „Software Engineering at Google”?

* [ ] Testy end-to-end
* [ ] Testy integracyjne
* [ ] Testy akceptacyjne
* [x] Testy jednostkowe

> **Wyjaśnienie:** Zalecane proporcje to około 70–80% testów jednostkowych, 15–20% integracyjnych i 5–10% end-to-end. Testy jednostkowe są najszybsze i najprecyzyjniej wskazują miejsce błędu.

#### Q. Co można powiedzieć o kodzie, którego testy dają 100% pokrycia linii?

* [x] Każda linia była wykonana, ale błędy nadal są możliwe
* [ ] Kod nie zawiera żadnych błędów
* [ ] Każda możliwa kombinacja danych wejściowych została sprawdzona
* [ ] Testy na pewno sprawdzają poprawność wyników

> **Wyjaśnienie:** Pokrycie mówi tylko, które linie zostały uruchomione, a nie czy asercje sprawdzają właściwe rzeczy. Zielone testy z pełnym pokryciem mogą przeoczyć dane brzegowe, duże zbiory czy błędy konfiguracji.

#### Q. Do czego służy polecenie `sphinx-apidoc`?

* [ ] Do automatycznego publikowania gotowej dokumentacji na Read the Docs
* [x] Do generowania plików `.rst` dla modułów na podstawie kodu
* [ ] Do sprawdzania poprawności docstringów
* [ ] Do konwersji dokumentacji z Markdown do HTML

> **Wyjaśnienie:** `sphinx-apidoc` przechodzi po pakiecie i tworzy pliki `.rst` z dyrektywami `autodoc`, które przy budowaniu pobierają treść z docstringów. Gotowy HTML powstaje potem poleceniem `make html`.

#### Q. Jak w reStructuredText tworzy się nagłówek?

* [x] Linią znaków, np. `=` lub `-`, pod tekstem nagłówka
* [ ] Znakiem `#` na początku linii, dokładnie tak samo jak w Markdown
* [ ] Otoczeniem tekstu podwójnymi gwiazdkami `**`
* [ ] Dyrektywą `.. header::` przed tekstem

> **Wyjaśnienie:** W rST poziom nagłówka wynika z kolejności, w jakiej style podkreśleń pojawiają się w dokumencie; zwykle `=` oznacza najwyższy poziom, a `-` niższy. Podwójne gwiazdki dają tylko pogrubienie.

#### Q. Które rozszerzenie Sphinksa pozwala używać docstringów w stylu Google i NumPy?

* [ ] `sphinx.ext.autodoc`
* [ ] `sphinx.ext.viewcode`
* [x] `sphinx.ext.napoleon`
* [ ] `sphinx.ext.doctest`

> **Wyjaśnienie:** `napoleon` przekształca docstringi w stylu Google lub NumPy do postaci zrozumiałej dla Sphinksa. `autodoc` samo pobiera docstringi, ale oczekuje składni reST z polami `:param:`.

#### Q. Do czego służy `sys._MEIPASS` w aplikacji spakowanej PyInstallerem?

* [ ] Przechowuje hasło do rozpakowania aplikacji
* [ ] Zawiera numer wersji PyInstallera użytej do zbudowania aplikacji
* [x] Wskazuje katalog, w którym leżą dołączone zasoby
* [ ] Wskazuje katalog z kodem źródłowym `.py`

> **Wyjaśnienie:** W spakowanej aplikacji zasoby dodane przez `--add-data` znajdują się w katalogu wskazywanym przez `sys._MEIPASS` (w trybie `--onefile` jest to folder tymczasowy). Poza PyInstallerem atrybut nie istnieje, stąd funkcja `resource_path` z `try/except`.

#### Q. Czy PyInstaller uruchomiony w Linuksie może wygenerować plik `.exe` dla systemu Windows?

* [ ] Tak, wystarczy opcja `--onefile`
* [ ] Tak, jeśli w opcji `--icon` podamy plik ikony w formacie `.ico`
* [x] Nie, plik wykonywalny trzeba zbudować w docelowym systemie
* [ ] Tak, ale tylko dla aplikacji bez interfejsu graficznego

> **Wyjaśnienie:** PyInstaller dołącza interpreter i biblioteki systemu, w którym działa, więc tworzy plik wykonywalny tylko dla tej platformy. Wersję dla Windows buduje się w Windows, np. na maszynie wirtualnej lub w CI.

#### Q. Co zawiera katalog `__pycache__` tworzony obok modułów?

* [ ] Kopie zapasowe plików źródłowych tworzone przy każdej edycji
* [x] Pliki `.pyc` ze skompilowanym kodem bajtowym modułów
* [ ] Pobrane pakiety z PyPI
* [ ] Wyniki ostatniego uruchomienia testów

> **Wyjaśnienie:** Python zapisuje tam kod bajtowy zaimportowanych modułów, np. `modul.cpython-312.pyc`, i używa go ponownie, dopóki źródło się nie zmieni. Przyspiesza to wczytywanie, a nie samo wykonanie, i katalog dodaje się do `.gitignore`.

#### Q. Co wypisze ten program w Pythonie 3.12?

```python
import dis

def f(a, b):
    return a + b

print([i.opname for i in dis.get_instructions(f)])
```

* [ ] `['LOAD_FAST', 'LOAD_FAST', 'BINARY_ADD', 'RETURN_VALUE']`
* [x] `['RESUME', 'LOAD_FAST', 'LOAD_FAST', 'BINARY_OP', 'RETURN_VALUE']`
* [ ] `['RESUME', 'LOAD_GLOBAL', 'LOAD_GLOBAL', 'BINARY_OP', 'RETURN_VALUE']`
* [ ] `['RESUME', 'LOAD_CONST', 'LOAD_CONST', 'CALL', 'RETURN_VALUE']`

> **Wyjaśnienie:** Od Pythona 3.11 dwuargumentowe operatory arytmetyczne i bitowe (`+`, `-`, `*` itd.) używają jednej instrukcji `BINARY_OP`, a funkcje zaczynają się od `RESUME`; starsze `BINARY_ADD` już nie istnieje. Argumenty funkcji są zmiennymi lokalnymi, więc ładuje je `LOAD_FAST`.

#### Q. Co wypisze ten program?

```python
def przyklad(a, b, c=10):
    x = a + b
    return x * c

code = przyklad.__code__
print(code.co_argcount, code.co_varnames)
```

* [ ] `2 ('a', 'b')`
* [ ] `3 ('a', 'b', 'c')`
* [x] `3 ('a', 'b', 'c', 'x')`
* [ ] `4 ('a', 'b', 'c', 'x')`

> **Wyjaśnienie:** `co_argcount` liczy parametry pozycyjne, także te z wartością domyślną. `co_varnames` zawiera wszystkie zmienne lokalne: najpierw parametry, potem zmienne utworzone w ciele funkcji.

#### Q. Co wypisze ten program?

```python
import inspect

def f(a, b=2, *args, c, **kw):
    pass

print(inspect.signature(f))
```

* [x] `(a, b=2, *args, c, **kw)`
* [ ] `(a, b, args, c, kw)`
* [ ] `f(a, b=2, *args, c, **kw)`
* [ ] `<Signature of f>`

> **Wyjaśnienie:** `inspect.signature` zwraca obiekt `Signature`, którego tekstowa postać odtwarza listę parametrów razem z wartościami domyślnymi i gwiazdkami, ale bez nazwy funkcji.

#### Q. Co wypisze ten program?

```python
import inspect

try:
    inspect.getsource(len)
except Exception as e:
    print(type(e).__name__)
```

* [ ] `OSError`
* [x] `TypeError`
* [ ] `NameError`
* [ ] `FileNotFoundError`

> **Wyjaśnienie:** `len` jest funkcją wbudowaną napisaną w C, a nie funkcją zdefiniowaną w Pythonie, więc `getsource` odrzuca ją jako zły typ obiektu. `OSError` pojawia się, gdy obiekt jest poprawnego typu, ale nie da się znaleźć jego pliku źródłowego.

#### Q. Co oznaczają w pliku znaczniki `<<<<<<<`, `=======` i `>>>>>>>` po wykonaniu `git merge`?

* [ ] Linie, które Git usunął podczas scalania
* [ ] Fragmenty dodane przez najnowszy commit
* [x] Konflikt: obie gałęzie zmieniły ten sam fragment
* [ ] Miejsca, w których trzeba dodać komentarz do commita

> **Wyjaśnienie:** Git nie umie sam połączyć zmian w tych samych liniach, więc wstawia obie wersje: bieżącej gałęzi (`HEAD`) i scalanej. Trzeba wybrać właściwą treść, usunąć znaczniki, a potem wykonać `git add` i commit.
