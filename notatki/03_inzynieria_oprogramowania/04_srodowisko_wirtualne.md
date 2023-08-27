## Środowisko wirtualne

Środowisko wirtualne to mechanizm, który pozwala na tworzenie odizolowanych przestrzeni dla różnych projektów Pythona. Zapewnia to, że każdy projekt może mieć własne zależności, niezależnie od innych projektów. Dzięki temu możemy unikać potencjalnych konfliktów związanych z różnymi wersjami bibliotek.

### Virtualenv

**virtualenv** to jedno z najpopularniejszych narzędzi do tworzenia środowisk wirtualnych w Pythonie. 

Aby zainstalować narzędzie **virtualenv** za pomocą menedżera pakietów **PIP**, wykonaj:

```bash
pip install virtualenv
```

Aby utworzyć nowe środowisko wirtualne o nazwie env w bieżącym folderze, wpisz:

```bash
virtualenv env
```

Jeśli posiadasz różne wersje Pythona zainstalowane w systemie, możesz określić, której wersji Pythona ma używać twoje środowisko wirtualne. Przykładowo, aby użyć interpretera Pythona zlokalizowanego w `/usr/bin/python3`:

```bash
virtualenv -p /usr/bin/python3 env
```

Aby aktywować środowisko wirtualne (w systemach bazujących na Unix):

```bash
source env/bin/activate
```

Dla systemów Windows:

```bash
env\Scripts\activate
```

Aby dezaktywować środowisko wirtualne:

```bash
deactivate
```

Możesz również zapisywać i przywracać zależności projektu. Aby zapisać zainstalowane pakiety do pliku `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Aby zainstalować pakiety z pliku `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Venv

Warto również wspomnieć o **venv**, narzędziu wbudowanym w Pythona od wersji 3.3, które służy do tworzenia środowisk wirtualnych. Jest mniej funkcjonalne niż **virtualenv**, ale nie wymaga dodatkowej instalacji.

Aby utworzyć środowisko wirtualne za pomocą `venv`:

```bash
python3 -m venv env
```

Aktywacja i dezaktywacja środowiska działa tak samo, jak w przypadku `virtualenv`.

### Linki

- [Oficjalna strona Virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Repozytorium Virtualenv na GitHubie](https://github.com/pypa/virtualenv)
- [Dokumentacja Venv w Pythonie](https://docs.python.org/3/library/venv.html)
- [Poradnik po środowiskach wirtualnych w Pythonie](https://realpython.com/python-virtual-environments-a-primer/)
