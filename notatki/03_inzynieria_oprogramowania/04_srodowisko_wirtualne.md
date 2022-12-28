
### Środowisko wirtualne

Środowisko wirtualne to odizolowane od reszty systemu wersje bibliotek i pakietów Pythona. Instalując daną wersję pakietu w środowisku wirtualnym jest ona dostępna tylko w nim. Gdy usuwamy środowisko wirtualne wraz z nim znika również wszystko to co zostało zainstalowane w jęgo obrębie.

Popularnym narzędziem do tworzenia środowisk wirtualnych jest <code>virtualenv</code>. Narzędzie to tworzy specjalny folder o dowolnej nazwie (np. `env/`) oraz modyfikuje zmienną środowiskową PATH dodając do niej refernecje do podfolderu `bin` znajdującego się w utworzonym folderze (np. `env/bin/`). Wszystkie pakiety i biblioteki instalowane w środowisku wirtualnym wędrują do tego folderu.

Aby zainstalować narzędzie <code>virtualenv</code> przy pomocy menadźera pakietów <code>PIP</code>, użyj:

    pip install virtualenv

Aby utworzyć środowisko wirtualne o nazwie *env* w aktualnym folderze, użyj:

    virtualenv env
    
Jeśli w systemie masz zainstalowane różne wersje Pythona, to możesz powiedzieć środowisku wirtualnemu, z której wersji ma korzystać.
Przykładowo, jeśli mam interpreter Pythona w folderze */usr/bin/python3* i chce, żeby z niego korzystało moje środowisko wirtualne, to używam następującej komendy:

    virtualenv -p /usr/bin/python3 env

Aby wejść do środowiska wirtualnego, użyj:

    source env/bin/activate
    
Aby wyjść ze środowiska wirtualnego, użyj:

    deactivate
    
Aby zapisać do pliku *requirements.txt* wszystkie aktualnie zainstalowane biblioteki wraz z ich wersjami, użyj:

    pip freeze > requirements.txt

Aby zainstalować biblioteki wymienione w pliku *requirements.txt*, użyj:

    pip install -r requirements.txt
    
Linki:

* https://github.com/pypa/virtualenv