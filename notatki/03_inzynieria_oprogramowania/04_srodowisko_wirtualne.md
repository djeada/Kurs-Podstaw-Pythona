## Środowisko wirtualne

Środowisko wirtualne to mechanizm, który pozwala na tworzenie odizolowanych przestrzeni dla różnych projektów Pythona. Zapewnia to, że każdy projekt może mieć własne zależności, niezależnie od innych projektów. Dzięki temu możemy unikać potencjalnych konfliktów związanych z różnymi wersjami bibliotek.

### Zalety używania środowisk wirtualnych

1. **Izolacja zależności:** Każde środowisko wirtualne ma własne niezależne biblioteki i wersje Pythona, co oznacza, że aktualizacje lub zmiany w jednym projekcie nie wpłyną na inny. To szczególnie przydatne w dużych zespołach, gdzie różne projekty mogą wymagać różnych wersji tej samej biblioteki.

2. **Uproszczenie zarządzania zależnościami:** Zarządzanie zależnościami staje się łatwiejsze, ponieważ wszystkie biblioteki wymagane przez projekt są instalowane w izolacji od globalnego środowiska. To ułatwia także wdrożenia, ponieważ lista zależności jest jasno zdefiniowana i łatwa do zreplikowania w innym środowisku.

3. **Konsystencja środowiska:** Środowiska wirtualne gwarantują, że aplikacje będą działać tak samo na różnych maszynach deweloperskich, jak i serwerach produkcyjnych, co minimalizuje "działa u mnie" syndrom błędów.

4. **Łatwość w konfiguracji:** Ustawienie nowego środowiska wirtualnego jest proste i może być szybko skonfigurowane z minimalnym nakładem pracy, co jest idealne dla nowych członków zespołu lub podczas rozpoczynania nowych projektów.

5. **Bezpieczeństwo:** Izolacja zależności minimalizuje ryzyko związane z nieautoryzowanym dostępem do systemów przez zależności, ponieważ każdy projekt może ograniczać się do minimalnie wymaganych uprawnień.

6. **Eksperymentowanie i testowanie:** Środowiska wirtualne umożliwiają bezpieczne eksperymentowanie z nowymi pakietami i wersjami bez ryzyka zakłócenia działania stabilnych aplikacji. Dzięki temu można testować nowe wersje bibliotek bez wpływu na istniejące projekty.

7. **Zarządzanie wersją Pythona:** Wiele projektów może wymagać różnych wersji Pythona. Środowiska wirtualne pozwalają na łatwe przełączanie między wersjami Pythona, co jest niezbędne w środowiskach, gdzie trwająca konserwacja kodu wymaga pracy na wielu wersjach języka.

### Popularne narzędzia do zarządzania środowiskami wirtualnymi

- **venv:** Narzędzie wbudowane w Python 3, które pozwala na tworzenie izolowanych środowisk.
- **virtualenv:** Starsze narzędzie, dostępne dla starszych wersji Pythona, oferujące większą elastyczność niż `venv`.
- **conda:** Menadżer pakietów i środowisk, popularny w społecznościach naukowych i danych, obsługujący zarówno Pythona, jak i inne języki.

Korzystanie ze środowisk wirtualnych to dzisiaj standard w profesjonalnym programowaniu w Pythonie, kluczowy dla zachowania zdrowego i zarządzalnego środowiska deweloperskiego.

#### Virtualenv

**virtualenv** to jedno z najpopularniejszych narzędzi do tworzenia środowisk wirtualnych w Pythonie. Umożliwia ono tworzenie izolowanych środowisk Pythona, co jest niezmiernie ważne przy zarządzaniu zależnościami projektów oraz unikaniu konfliktów między nimi.

I. Instalacja virtualenv

Aby zainstalować narzędzie **virtualenv** za pomocą menedżera pakietów **PIP**, wykonaj:

    ```bash
    pip install virtualenv
    ```

II. Tworzenie nowego środowiska wirtualnego

Aby utworzyć nowe środowisko wirtualne o nazwie `env` w bieżącym folderze, wpisz:

    ```bash
    virtualenv env
    ```

Jeśli posiadasz różne wersje Pythona zainstalowane w systemie, możesz określić, której wersji Pythona ma używać twoje środowisko wirtualne. Przykładowo, aby użyć interpretera Pythona zlokalizowanego w `/usr/bin/python3`:

    ```bash
    virtualenv -p /usr/bin/python3 env
    ```

III. Aktywacja środowiska wirtualnego

Aby aktywować środowisko wirtualne (w systemach bazujących na Unix):

    ```bash
    source env/bin/activate
    ```

Dla systemów Windows:

    ```bash
    env\Scripts\activate
    ```

IV. Dezaktywacja środowiska wirtualnego

Aby dezaktywować środowisko wirtualne:

    ```bash
    deactivate
    ```

V. Zarządzanie zależnościami

Możesz również zapisywać i przywracać zależności projektu. Aby zapisać zainstalowane pakiety do pliku `requirements.txt`:

    ```bash
    pip freeze > requirements.txt
    ```

Aby zainstalować pakiety z pliku `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### Venv

Warto również wspomnieć o **venv**, narzędziu wbudowanym w Pythona od wersji 3.3, które służy do tworzenia środowisk wirtualnych. Jest mniej funkcjonalne niż **virtualenv**, ale nie wymaga dodatkowej instalacji i jest wystarczające dla większości zastosowań deweloperskich.

I. Tworzenie środowiska wirtualnego za pomocą venv

Aby utworzyć środowisko wirtualne za pomocą `venv`:

    ```bash
    python3 -m venv env
    ```
  
II. Inne operacje

Aktywacja i dezaktywacja środowiska działają tak samo, jak w przypadku `virtualenv`.


## Porównanie różnych środowisk wirtualnych

| Środowisko wirtualne | Cechy charakterystyczne                          | Zalety                                            | Wady                                          |
|----------------------|--------------------------------------------------|---------------------------------------------------|-----------------------------------------------|
| virtualenv          | Bardziej elastyczne niż `venv`, wspiera starsze wersje Pythona | Wysoka kompatybilność wsteczna, może tworzyć środowiska dla dowolnej wersji Pythona | Może być redundantne na nowszych wersjach Pythona z `venv` |
| venv                 | Standardowe narzędzie w Pythonie do izolacji pakietów | Proste w użyciu, zintegrowane z Pythonem           | Brak zaawansowanego zarządzania zależnościami, nie zarządza Pythonem |
| conda                | Zarządza pakietami oraz środowiskami, obsługuje wiele języków | Zarządza zarówno pakietami jak i wersjami Pythona, działa na wielu platformach | Może być wolniejsze, niektóre pakiety mogą być nieaktualne |
| pipenv               | Automatycznie tworzy i zarządza wirtualnymi środowiskami, dodaje obsługę Pipfile i Pipfile.lock | Łatwe zarządzanie zależnościami, automatyzacja środowiska | Mniej popularne niż inne narzędzia, wolniejsze niż czysty pip |

### Linki

- [Oficjalna strona Virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Repozytorium Virtualenv na GitHubie](https://github.com/pypa/virtualenv)
- [Dokumentacja Venv w Pythonie](https://docs.python.org/3/library/venv.html)
- [Poradnik po środowiskach wirtualnych w Pythonie](https://realpython.com/python-virtual-environments-a-primer/)
