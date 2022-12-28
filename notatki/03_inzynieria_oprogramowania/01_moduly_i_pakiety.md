
### Moduły i pakiety

Za każdym razem, gdy używamy instrukcji <code>import</code>, importujemy do skryptu zewnętrzny moduł. Każdy plik Pythona jest modułem, którego nazwa to nazwa pliku bez rozszerzenia .py. <a href="https://docs.python.org/3/library/index.html">Dokumentacja</a> zawiera pełną listę wbudowanych modułów biblioteki standardowej Pythona. Przykładowo, tak możemy zaimporotwać moduł `requests`:
 
    import requests
    print(type(requests)) # <class 'module'>

Pakiety to foldery z modułami, w których znajduje się plik `init.py`. Jest to plik specjalny, który jest potrzebny do odróżnienia pakietu od zwykłego folderu.

    .
    └── nazwa_paczki
        ├── __init__.py
        └── przykladowy_skrypt_a.py
        └── przykladowy_skrypt_b.py
        └── przykladowy_skrypt_c.py
    └── main.py
    
Możemy importować moduły na kilka sposobów:

* Zaimportowanie całego modułu:

      import nazwa_modulu

* Zaimportowanie całego modułu i nadanie mu aliasu:

      import nazwa_modulu as alias

* Zaimportowanie wybranych funkcji z modułu:

      from nazwa_modulu import fun_1, fun_2

* Zaimportowanie wybranych funkcji z modułu i nadanie im aliasów:

      from nazwa_modulu import fun_1 as f1, fun_2 as f2

* Zaimportowanie wszystkich funkcji z modułu:

      from nazwa_paczki.przykladowy_skrypt_a import *

      fun_a()
      fun_b()

Należy uważać z używaniem instrukcji <code>from modul import *</code>, ponieważ zaimportowane zostają wszystkie zmienne i funkcje z modułu, niezależnie od tego czy ich będziemy używać czy nie. Może to prowadzić do konfliktów nazw oraz utrudnić odczytanie kodu.

Uwaga: instrukcje, które nie są częścią definicji żadnej funkcji, zostaną automatycznie wykonane podczas importowania modułu!

Przykład:

    def fun_a():
        ...

    def fun_b():
         ...

    wyslij_rakiety()

Jeśli ten moduł zostanie zaimportowany w innym skrypcie, to funkcja `wyslij_rakiety()` zostanie wywołana podczas importowania modułu.
Aby temu zapobiec, należy umieścić wszystkie instrukcje, które mają być wykonywane poza definicjami funkcji, w ciele następującego warunku <code>if name == "main":</code> :

    def fun_a():
        ...

    def fun_b():
         ...

    if __name__ == "__main__":
      wyslij_rakiety()
