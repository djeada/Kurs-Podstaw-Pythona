## Git

* System kontroli wersji (archiwizuje zmiany w kodzie).
* Stworzony przez Linusa Torvaldsa w 2005 dla programistów pracujących nad jądrem Linux.
* Obecnie dominuje na rynku.
* Szybki, rozproszony, chroniony przed błędami w repozytorium.

## Instalacja

* Pobierz instalator z oficjalnej strony https://git-scm.com/downloads. Następnie przejdź przez proces instalacji.
* W systemie Linux dla wersji opartych na Debianie:

      sudo apt install git

## GitHub

* GitHub.com daje bezpłatną możliwość hostingu repozytoriów oraz oferuje bogaty interfejs graficzny.
* Obecnie dominuje na rynku.
* Korzystają z niego największe firmy i organizacje: Microsoft, Meta, NASA, NSA.
* Ogromna ilość projektów open-source.

Pytanie: Czy muszę korzystać z GitHuba, aby korzystać z Gita?

Odpowiedź: Nie, istnieją inne rozwiązania.

## Jak to działa?

* Git pracuje z tak zwanymi repozytoriami, gdzie umieszczany jest kod źródłowy. 
* Każdy członek zespołu ma swoją kopię repozytorium, a w niej dostęp do pełnej historii zmian w projekcie.
* Po wprowadzeniu swoich zmian programista wysyła je do serwera, a inni członkowie zespołu aktualizują swoje kopie repozytorium.
* Historia zmian gromadzona jest w obiektach Gita, które zapisuje w ukrytym folderze *.git*.

Typy obiektów: 

1) blob - plik binarny.
2) drzewo - lista innych obiektów wraz z ich nazwą, hashem i listą uprawnień.
3) commit - każdy commit trzyma hash poprzedniego commita w historii zmian oraz krótką notkę od autora.

Komendy:

* `git cat-file -p <object name>` - wyświetl informacje o danym obiekcie.
* `git rev-list --objects --all` - wyświetl listę wszystkich obiektów.

## Tworzenie repozytorium

* Aby utworzyć nowe repozytorium, zaleca się skorzystanie z serwisu GitHub.

![GitHub](https://user-images.githubusercontent.com/37275728/189520870-2bedbded-7354-43b6-8d05-35421cff847e.png)

* Następnie lokalnie używamy komendy:

      git clone link_do_repozytorium

* Istnieje też opcja utworzenia repozytorium lokalnie, przy pomocy komendy:

      git init
    
## Proces pracy z Gitem

* Nanieś zmiany w plikach w swojej lokalnej wersji repozytorium.
* Dodaj zmienione pliki do składu plików oczekujących na zatwierdzenie (staging area).
* Zatwierdź pliki wraz z krótkim komentarzem opisującym wprowadzone zmiany (commit).

      cat "Hello" > example.txt
      git add example.txt
      git commit -m "przykladowa informacja"
      git log

## Zatwierdzanie zmian

* Git używa tak zwanych commitów do zatwierdzenia wprowadzonych zmian.
* Wyświetlając historię zmian w repozytorium widzimy wszystkie dotychczasowe commity (*git log*).
* Mamy opcję załadowania stanu repozytorium z czasu zatwierdzenia danego commita (*git checkout commit-id*).
* Każdy commit ma unikalny klucz generowany przez algorytm SHA-1.
* Ten klucz składa się z 40 znaków oraz liczb zapisanych w systemie szesnastkowym.

![commit](https://user-images.githubusercontent.com/37275728/189501913-7fa99b33-bbd9-4667-a3d3-70c9ad197f41.png)

## Rozgałęzianie i łączenie gałęzi

* Git oferuje opcję nieliniowej historii zmian.
* Domyślna gałąź zwie się *master* lub *main*.
* Zawsze możemy utworzyć nową gałąź. Jej punktem startowym będzie ostatnio zatwierdzony commit.
* Aby przełączyć się z jednej gałęzi na inną, używamy polecenia <code>checkout</code> oraz nazwy gałęzi (*git checkout nazwa_galezi*).

      git checkout -b nowa_galaz
      git branch
      git touch temp.md
      git commit -am "proba"
      git checkout master
      git merge nowa_galaz

## Konflikty

* Jeśli jednocześnie zostały wprowadzone zmiany w tej samej części pliku na dwóch gałęziach, to przy próbie ich połączenia wystąpi komunikat o konflikcie.
* Problematyczny plik zostanie zmodyfikowany i będzie zawierał sekcje wydzielone strzałkami: <<<< ... >>>>.

      <<<<<<< HEAD:temp.md
      wiadomosc a zmieniona w b
      =======
      wiadomosc a zmieniona w c
      >>>>>>> nowa_galaz:temp.md

• Znajdź te sekcje, usuń strzałki i wybierz odpowiednią wersję zmian.

## Interakcje z serwerem

* Komenda `push` służy do wysłania lokalnych zmian do serwera.
* Komenda `pull` polega do pobierania modyfikacji z serwera.

      git pull origin master
      cat "Hello" > example.txt
      git add example.txt
      git commit -m "przykladowa informacja"
      git push origin master

## Ważne komendy

| Komenda | Działanie |
| ------- | --------- |
| git clone url | pobierz repozytorium z serwera |
| git add  | dodaj zmienione pliki do składu plików oczekujących na zatwierdzenie |
| git commit | zatwierdź zmiany |
| git status | wyświetl informację o zmienionych plikach |
| git diff | pokaż zmiany naniesione od ostatniego commita |
| git push | wyślij lokalne zmiany do serwera |
| git pull | pobierz modyfikację z serwera |

## Ćwiczenia

### Ćwiczenie nr 1

1. Sklonuj lokalnie repozytorium z twojego konta na GitHub. 
2. Utwórz dowolny plik tekstowy w obrębie tego repozytorium.
3. Wyświetl historię zmian dla repozytorium.
4. Dodaj plik 
5. Wyświetl historię zmian dla repozytorium.

### Ćwiczenie nr 2

1. Dodaj zmiany w tym samym pliku, w lokalnej wersji repozytorium oraz na stronie GitHub.
2. Spróbuj wysłać lokalne zmiany do serwera. Otrzymasz komunikat o konflikcie.
3. Rozwiąż konflikt i wyślij zmiany do serwera.
4. Sprawdź, czy GitHub zaakceptował zmiany.
