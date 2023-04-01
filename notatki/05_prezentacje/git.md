# Git

* Git to system kontroli wersji, który archiwizuje zmiany w kodzie i pozwala na łatwe zarządzanie różnymi wersjami projektu. 
* Został stworzony w 2005 roku przez Linusa Torvaldsa dla programistów pracujących nad jądrem systemu operacyjnego Linux. 
* Obecnie jest jednym z najpopularniejszych systemów kontroli wersji na świecie. 
* Git jest szybki, rozproszony, co oznacza, że może być używany przez wielu ludzi jednocześnie, a także jest chroniony przed błędami w repozytorium, co pozwala na bezpieczne przechowywanie zmian w kodzie.

# Instalacja

Aby zainstalować Git, należy pobrać instalator z oficjalnej strony https://git-scm.com/downloads i przejść przez proces instalacji. W systemie Linux dla wersji opartych na Debianie, można użyć polecenia:

```bash
sudo apt install git
```

# GitHub

* GitHub to platforma internetowa, która umożliwia bezpłatne hostowanie repozytoriów Git oraz oferuje bogaty interfejs graficzny do ich zarządzania. 
* Obecnie jest jednym z najpopularniejszych serwisów tego typu na świecie i korzystają z niego największe firmy i organizacje, takie jak Microsoft, Meta, NASA czy NSA. 
* GitHub jest szczególnie popularny wśród twórców projektów open-source, czyli projektów o otwartym kodzie źródłowym, dostępnych dla wszystkich do współpracy i modyfikacji.

Pytanie: Czy muszę korzystać z GitHuba, aby korzystać z Gita?

Odpowiedź: Nie, istnieją inne rozwiązania do hostowania repozytoriów Git, takie jak np. GitLab czy Bitbucket. Można również hostować repozytoria na własnym serwerze lub używać innych narzędzi do zarządzania kontrolą wersji, które nie są związane z GitHubem.

# Jak to działa?

* Do pracy z Gitem wykorzystywane są tak zwane repozytoria, czyli miejsca, w których przechowywana jest historia zmian w projekcie. 
* Każdy członek zespołu programistów, który uczestniczy w pracach nad projektem, posiada swoją kopię repozytorium, w której ma dostęp do pełnej historii zmian w projekcie. 
* Po wprowadzeniu swoich zmian do kodu, programista może je przesłać z powrotem na serwer i udostępnić je innym członkom zespołu, którzy mogą zaktualizować swoje kopie repozytorium. 
* Historia zmian jest gromadzona w obiektach Git, które są przechowywane w specjalnym ukrytym folderze o nazwie .git.

Istnieją trzy typy obiektów w Git:

* `blob` - obiekt przechowujący plik binarny.
* `drzewo` - obiekt przechowujący listę innych obiektów wraz z ich nazwami, haszami (unikalnymi identyfikatorami) i listą uprawnień.
* `commit` - obiekt przechowujący informacje o każdej zmianie w kodzie, w tym hash poprzedniego commita w historii zmian oraz krótką notatkę od autora zmian.

Przykłady komend, które pozwalają na manipulowanie obiektami i repozytorium to:

* `git cat-file -p <object name>` - wyświetla informacje o danym obiekcie.
* `git rev-list --objects --all` - wyświetla listę wszystkich obiektów w repozytorium.

# Tworzenie repozytorium

Aby utworzyć nowe repozytorium, zaleca się skorzystanie z serwisu GitHub lub innej platformy do hostowania repozytoriów Git. 

![GitHub](https://user-images.githubusercontent.com/37275728/189520870-2bedbded-7354-43b6-8d05-35421cff847e.png)

* Aby sklonować istniejące repozytorium na swój komputer, należy użyć komendy:

```bash
git clone link_do_repozytorium
```

* Istnieje też opcja utworzenia repozytorium lokalnie, przy pomocy komendy:

```bash
git init
```

# Proces pracy z Gitem

Git umożliwia wprowadzanie zmian w plikach w lokalnej wersji repozytorium, dodawanie tych zmienionych plików do składu plików oczekujących na zatwierdzenie (zwanego "staging area") oraz zatwierdzanie tych zmian za pomocą commitów. Proces pracy z Gitem można przedstawić w następujący sposób:

1. Wprowadź zmiany w plikach w swojej lokalnej kopii repozytorium.
1. Dodaj zmienione pliki do składu plików oczekujących na zatwierdzenie za pomocą komendy `git add`.
1. Zatwierdź pliki i opisz wprowadzone zmiany za pomocą commita za pomocą komendy `git commit -m "komentarz"`. 
1. Możesz teraz wyświetlić historię commitów za pomocą komendy `git log`.

Przykład:

```bash
cat "Hello" > example.txt
git add example.txt
git commit -m "przykladowa informacja"
git log
```

# Zatwierdzanie zmian

* Git wykorzystuje commity do zatwierdzenia wprowadzonych zmian w kodzie. 
* Dzięki komendzie `git log` można wyświetlić historię commitów w repozytorium. 
* Jeśli chcesz przejrzeć stan repozytorium z określonego momentu w przeszłości, możesz użyć komendy `git checkout commit-id`, gdzie `commit-id` to unikalny klucz commita generowany przez algorytm SHA-1 (składający się z 40 znaków i liczb zapisanych w systemie szesnastkowym).

![commit](https://user-images.githubusercontent.com/37275728/189501913-7fa99b33-bbd9-4667-a3d3-70c9ad197f41.png)

# Rozgałęzianie i łączenie gałęzi
Git umożliwia tworzenie nowych gałęzi, które są oddzielnymi ścieżkami rozwoju projektu. Domyślna gałąź to najczęściej gałąź `master` lub `main`. Gałęzie służą do odizolowania różnych funkcjonalności lub zmian od głównej linii kodu, co pozwala na pracę nad nimi bez ryzyka ich wpływu na inne elementy projektu.

* Aby utworzyć nową gałąź, można użyć komendy `git checkout -b nazwa_galezi`, gdzie `nazwa_galezi` to nazwa nowej gałęzi. 
* Aby przełączyć się z jednej gałęzi na inną, można użyć komendy `git checkout nazwa_galezi`. 
* Aby wyświetlić dostępne gałęzie, można użyć komendy `git branch`.
* Aby połączyć zmiany z dwóch różnych gałęzi, można użyć komendy `git merge nazwa_galezi`, gdzie `nazwa_galezi` to nazwa gałęzi, z której chcemy pobrać zmiany. W ten sposób zmiany z gałęzi `nazwa_galezi` zostaną połączone z aktualnie aktywną gałęzią.

Przykład:

```bash
git checkout -b nowa_galaz
git branch
git touch temp.md
git commit -am "proba"
git checkout master
git merge nowa_galaz
```

# Konflikty

Konflikty w Git występują, gdy dwa różne gałęzie zostały zmodyfikowane w taki sposób, że te same linie kodu zostały zmienione na obu gałęziach. W takiej sytuacji Git nie jest w stanie samodzielnie połączyć tych zmian, dlatego konieczne jest ręczne rozwiązanie konfliktu.

Jeśli próba połączenia gałęzi zakończy się konfliktem, plik zawierający konflikt zostanie zmodyfikowany i będzie zawierał sekcje wydzielone strzałkami `<<<<<<<`, `=======`, `>>>>>>>`. Te sekcje oznaczają, gdzie zaczyna się i kończy konflikt, oraz które zmiany pochodzą z jakiej gałęzi. Aby rozwiązać konflikt, należy usunąć strzałki i wybrać odpowiednią wersję zmian, która ma zostać zachowana.

```bash
<<<<<<< HEAD:temp.md
wiadomosc a zmieniona w b
=======
wiadomosc a zmieniona w c
>>>>>>> nowa_galaz:temp.md
```

• Znajdź te sekcje, usuń strzałki i wybierz odpowiednią wersję zmian.

# Interakcje z serwerem

* Aby przesłać zmiany z lokalnego repozytorium na serwer, można użyć komendy `git push`. 
* Aby pobrać zmiany z serwera, można użyć komendy `git pull`. 
* W obu przypadkach należy podać nazwę serwera oraz nazwę gałęzi, z której lub do której mają zostać przesłane/pobrane zmiany.

```bash
git pull origin master
cat "Hello" > example.txt
git add example.txt
git commit -m "przykladowa informacja"
git push origin master
```

# Ważne komendy

| Komenda | Działanie |
| ------- | --------- |
| git clone url | pobierz repozytorium z serwera |
| git add  | dodaj zmienione pliki do składu plików oczekujących na zatwierdzenie |
| git commit | zatwierdź zmiany |
| git status | wyświetl informację o zmienionych plikach |
| git diff | pokaż zmiany naniesione od ostatniego commita |
| git push | wyślij lokalne zmiany do serwera |
| git pull | pobierz modyfikację z serwera |

# Ćwiczenia

## Ćwiczenie nr 1

1. Sklonuj lokalnie repozytorium z twojego konta na GitHub za pomocą komendy `git clone link_do_repozytorium`.
1. Utwórz nowy plik tekstowy w obrębie tego repozytorium, np. za pomocą polecenia `touch nazwa_pliku.txt`.
1. Wyświetl historię zmian dla repozytorium za pomocą komendy `git log`.
1. Dodaj plik do składu plików oczekujących na zatwierdzenie za pomocą polecenia `git add nazwa_pliku.txt`.
1. Wyświetl ponownie historię zmian dla repozytorium za pomocą komendy `git log`.
    
## Ćwiczenie nr 2

1. Dodaj zmiany w tym samym pliku, zarówno w lokalnej wersji repozytorium, jak i na stronie GitHub.
1. Spróbuj wysłać lokalne zmiany do serwera za pomocą polecenia `git push origin nazwa_galezi`. Otrzymasz komunikat o konflikcie.
1. Rozwiąż konflikt poprzez usunięcie strzałek i wybranie odpowiedniej wersji zmian w pliku.
1. Zatwierdź zmiany za pomocą komendy `git commit -am "opis zmian"`.
1. Wyślij zmiany do serwera za pomocą polecenia `git push origin nazwa_galezi`.
1. Sprawdź, czy GitHub zaakceptował zmiany poprzez sprawdzenie historii zmian na stronie projektu.
