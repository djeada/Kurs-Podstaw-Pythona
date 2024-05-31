## Instalacja Pythona w systemie Windows

Aby rozpocząć programowanie w Pythonie, konieczne jest przygotowanie odpowiedniego środowiska pracy. Dla większości użytkowników oznacza to pobranie i zainstalowanie odpowiedniej wersji interpretera Pythona. Poniżej znajduje się szczegółowy przewodnik dotyczący instalacji Pythona w systemie Windows.

### Kroki instalacyjne

#### Przejście na stronę Pythona

1. Otwórz przeglądarkę internetową i wejdź na stronę [Python](https://www.python.org/downloads/) z linkami do pobrania plików.

![python_website](https://github.com/djeada/Kurs-Podstaw-Pythona/assets/37275728/615dc6d2-6ce3-469a-9528-3441283cd829)

#### Pobieranie odpowiedniej wersji

2. W sekcji "Python Releases for Windows", znajdź najnowszą stabilną wersję Pythona dedykowaną dla systemu Windows. Kliknij w odpowiedni link, aby rozpocząć pobieranie instalatora.

![python_windows](https://github.com/djeada/Kurs-Podstaw-Pythona/assets/37275728/13939d60-cef4-4f35-81f9-48c2a0ec9a37)

#### Uruchomienie instalatora

3. Po zakończeniu pobierania, lokalizuj plik instalacyjny (zwykle w folderze "Pobrane") i uruchom go, klikając dwukrotnie.

#### Konfiguracja instalacji

4. Po uruchomieniu instalatora pojawi się okno konfiguracji instalacji Pythona. Zwróć uwagę na opcję "Add Python to PATH". Zalecamy zaznaczenie tej opcji, ponieważ umożliwia ona uruchamianie Pythona z dowolnego miejsca w wierszu poleceń bez konieczności podawania pełnej ścieżki do interpretera.

#### Wybór typu instalacji

5. Masz dwie opcje: "Install Now" (zainstaluj teraz) lub "Customize installation" (dostosuj instalację). Wybierz "Customize installation" jeśli chcesz dostosować szczegóły instalacji, takie jak lokalizacja instalacji, dodatkowe opcje itp. W przeciwnym razie kliknij "Install Now", aby użyć domyślnych ustawień.

#### Postępowanie zgodnie z instrukcjami

6. Kontynuuj proces instalacji, postępując zgodnie z instrukcjami wyświetlanymi przez instalator. Instalator może poprosić o potwierdzenie uprawnień administratora - zaakceptuj te prośby, aby kontynuować.

#### Zakończenie instalacji

7. Po zakończeniu instalacji pojawi się okno z potwierdzeniem. Możesz zamknąć instalator. 

#### Sprawdzenie poprawności instalacji

8. Aby upewnić się, że instalacja przebiegła prawidłowo, otwórz wiersz poleceń (np. `cmd` lub `PowerShell`). Wpisz komendę `python --version` i naciśnij Enter. Jeśli instalacja została przeprowadzona prawidłowo, powinieneś zobaczyć informację o zainstalowanej wersji Pythona.

```shell
python --version
```

Prawidłowy wynik powinien wyglądać mniej więcej tak:

```shell
Python 3.9.2
```

#### Instalacja dodatkowych narzędzi

9. Python jest często używany wraz z dodatkowymi narzędziami i bibliotekami. Najważniejszym narzędziem jest `pip`, menedżer pakietów dla Pythona, który jest zwykle instalowany automatycznie razem z Pythonem. Możesz sprawdzić jego wersję za pomocą polecenia:

```shell
pip --version
```

#### Instalacja środowiska IDE

10. Aby ułatwić sobie pracę z Pythonem, warto zainstalować środowisko programistyczne (IDE). Popularne IDE dla Pythona to:

- **[PyCharm](https://www.jetbrains.com/pycharm/)**: Zaawansowane środowisko IDE stworzone przez JetBrains, oferujące wiele funkcji wspomagających programowanie w Pythonie, takich jak podświetlanie składni, inteligentne podpowiedzi, refaktoryzacja kodu, debugowanie i integracja z systemami kontroli wersji.

- **[Visual Studio Code](https://code.visualstudio.com/)**: Lekki, ale potężny edytor kodu od Microsoftu. Dzięki wtyczkom można rozszerzyć jego funkcjonalność, aby wspierał Python, oferując podświetlanie składni, automatyczne uzupełnianie, debugowanie, zintegrowany terminal i wiele innych narzędzi przydatnych dla programistów.

- **[Sublime Text](https://www.sublimetext.com/)**: Szybki i wydajny edytor tekstu, który można dostosować do pracy z Pythonem za pomocą różnych pakietów i wtyczek. Umożliwia podświetlanie składni, automatyczne uzupełnianie kodu i wiele innych funkcji.

- **[Atom](https://atom.io/)**: Edytor tekstu typu open source, stworzony przez GitHub. Atom jest bardzo konfigurowalny i wspiera Python dzięki wtyczkom, oferując funkcje takie jak podświetlanie składni, automatyczne uzupełnianie kodu, integracja z Git i wiele innych.

Każde z tych IDE oferuje różnorodne funkcje, takie jak podświetlanie składni, autouzupełnianie kodu, debugowanie i wiele innych, które mogą znacznie ułatwić programowanie w Pythonie. Wybór odpowiedniego narzędzia zależy od Twoich preferencji oraz specyficznych potrzeb projektów, nad którymi pracujesz.
