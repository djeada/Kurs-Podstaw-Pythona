
### PIP i PyPI

PIP to narzędzie umożliwiające instalację pakietów Pythona dostępnych na stronie PyPI (Python Package Index).

Instalacja:

1. Pobierz skrypt <a href="https://bootstrap.pypa.io/get-pip.py">get-pip.py</a>.
1. Uruchom skrypt <code>python get-pip.py</code>.
1. Zweryfikuj poprawność instalcji wpisując w wierszu poleceń następujące komendy: <code>pip help</code>.

Aby zainstalować konkretny pakiet, użyj:

    pip install <nazwa_pakietu>
    
Aby wyświetlić szczegóły zainstalowanego pakietu, użyj:
    
    pip show <nazwa_pakietu>
    
Aby wyświetlić listę wszystkich aktualnie używanych pakietów, użyj:

    pip list
    
Aby zapisać w pliku *requirements.txt* listę wszystkich aktualnie używanych pakietów wraz z wersjami, użyj:

    pip freeze > requirements.txt
    
Aby odinstalować pakiet, użyj:

    pip uninstall <nazwa_pakietu>

Aby zaktualizować program PIP, użyj:
 
    pip install --upgrade pip

Linki:

* https://pypi.org/
