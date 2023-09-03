## Dokumentacja

Dokumentacja stanowi kluczowy komponent każdego projektu programistycznego, umożliwiając użytkownikom zrozumienie funkcjonalności, struktury oraz sposobu działania aplikacji. W Pythonie jednym z popularnych narzędzi służących do tworzenia profesjonalnej dokumentacji jest **SPHINX**. Pozwala on na generowanie dokumentacji w różnorodnych formatach, w tym HTML, LaTeX, epub czy plain text. Istnieje również możliwość konwersji dokumentacji z formatu LaTeX do PDF.

### Rozpoczęcie z Sphinx

Aby zainicjować szkielet dokumentacji, potrzebujesz uruchomić następującą komendę:

```bash
sphinx-quickstart
```

Po uruchomieniu tej komendy, SPHINX poprosi cię o podanie kilku szczegółów dotyczących twojego projektu. Na podstawie udzielonych odpowiedzi, narzędzie to wygeneruje odpowiednie pliki startowe i przygotuje je do uzupełnienia konkretną treścią.

Aby skompilować i wygenerować dokumentację opartą o istniejące pliki konfiguracyjne, wykorzystaj:

```bash
make html
```

Po pomyślnym wykonaniu tej komendy, jeśli wszystko przebiegnie bez błędów, SPHINX poinformuje cię o sukcesie. W przypadku wystąpienia problemów, zostaniesz poinformowany za pomocą komunikatów błędów.

## reStructuredText i jego zastosowanie w Sphinx

**reStructuredText** (rST) to elastyczny i rozbudowany język znaczników przeznaczony do tworzenia dokumentacji i prostych stron internetowych. W porównaniu z popularnym językiem markdown, rST oferuje znacznie bogatszy zestaw funkcji, co czyni go idealnym narzędziem do tworzenia rozbudowanej dokumentacji.

### Kluczowe cechy reStructuredText:

1. **Zaawansowane formatowanie**: rST oferuje funkcje, takie jak przypisy dolne, tabele, linki oraz definicje, które nie są tak łatwo dostępne w markdown.

2. **Rozszerzalność**: Dzięki wsparciu dla różnych pluginów, rST można łatwo dostosować do konkretnych potrzeb projektu. 

3. **Integracja z Sphinx**: rST jest głównym formatem używanym przez Sphinx, popularne narzędzie do generowania dokumentacji. Plik `index.rst` jest centralnym punktem dokumentacji w Sphinx, zawierającym główną strukturę oraz linki do innych części dokumentacji.

4. **Prostota linkowania**: W rST linkowanie do innych plików czy sekcji jest bardziej intuicyjne i przejrzyste, dzięki czemu utrzymanie spójności w rozbudowanych dokumentacjach staje się łatwiejsze.

5. **Automatyczna generacja HTML**: Sphinx, korzystając z plików rST, umożliwia generowanie dokumentacji w różnych formatach, w tym w HTML. Wystarczy użyć komendy `make html`, aby przekształcić pliki rST w elegancką stronę internetową.

Dla projektów o złożonej strukturze dokumentacji, reStructuredText w połączeniu z Sphinxem oferuje niezrównane możliwości. Dzięki zaawansowanym funkcjom i możliwościom dostosowania, tworzenie profesjonalnej i spójnej dokumentacji staje się prostsze i bardziej efektywne.

### Podstawowe formatowanie w reStructuredText

#### Nagłówki

Nagłówki są tworzone poprzez dodanie linii znaków pod tekstem.

```
Nagłówek 1
==========

Nagłówek 2
----------

Nagłówek 3
^^^^^^^^^^
```

#### Wyróżnienia tekstu

```
*Pochylenie*

**Pogrubienie**

``Poczwórny akcent dla kodu źródłowego``
```

#### Listy

```
- Element 1
- Element 2
    - Pod-element 2.1
    - Pod-element 2.2
- Element 3
```

#### Linki

```
`Link tekstowy <http://example.com>`_
```

#### Obrazy

```
.. image:: ścieżka/do/obrazu.jpg
   :alt: Tekst alternatywny
```

#### Tabele

```
+---------------+-------------+-------------+
| Nagłówek 1    | Nagłówek 2  | Nagłówek 3  |
+---------------+-------------+-------------+
| komórka 1.1   | komórka 1.2 | komórka 1.3 |
| komórka 2.1   | komórka 2.2 | komórka 2.3 |
+---------------+-------------+-------------+
```

#### Przypisy

```
Przykład tekstu z przypisem.[1]

.. [1] Tekst przypisu dolnego.
```

#### Dyrektywy

Dyrektywy służą do wstawiania różnych elementów, takich jak obrazy, tabele czy fragmenty kodu.

```
.. note:: To jest notatka.
```

```
.. warning:: To jest ostrzeżenie.
```

```
.. code-block:: python

    def funkcja():
        print("Przykład kodu")
```

### Jak pisać dobrą dokumentację?

Pisanie efektywnej dokumentacji to proces, który może sprawić, że Twoja aplikacja stanie się bardziej użyteczna i przystępna. Poniżej znajdują się wskazówki, które pomogą Ci tworzyć jasną, zrozumiałą i przyjazną dla użytkownika dokumentację:

#### Zacznij od tutoriali
- Wprowadź użytkownika krok po kroku przez proces instalacji i uruchomienia aplikacji.
- Demonstruj podstawowe scenariusze użytkowania Twojego oprogramowania.
- Wyjaśnij funkcjonalność poszczególnych elementów interfejsu.
- Mimo że tutoriale różnią się od klasycznej dokumentacji, stanowią doskonały punkt wyjścia, z którego można czerpać informacje.

#### Automatyzuj proces tworzenia dokumentacji
- Narzędzia takie jak Sphinx ułatwiają tworzenie jednolitej i konsekwentnej dokumentacji w różnych formatach.
- Przy programowaniu w Pythonie wykorzystuj `docstrings` do tworzenia wewnętrznej dokumentacji kodu.

#### Dokumentacja musi być na bieżąco aktualizowana
- Upewnij się, że treść dokumentacji odzwierciedla aktualny stan aplikacji.
- Każda zmiana w kodzie powinna być odzwierciedlona w dokumentacji.

#### Używaj jasnego i zrozumiałego języka
- Unikaj technicznych terminów, chyba że są one niezbędne. Jeśli tak, staraj się je wyjaśnić.
- Ilustruj skomplikowane koncepcje przykładami praktycznymi.

#### Zwracaj uwagę na detale
- Dbaj o poprawność językową oraz stylistyczną.
- Jeżeli Twoja aplikacja bazuje na zewnętrznych bibliotekach, dołącz linki do ich dokumentacji.

#### Zachowuj strukturę i organizację
- Informacje powinny być prezentowane w logiczny sposób, uporządkowane w odpowiednie sekcje i podsekcje.
- Wykorzystuj nagłówki, listy i wyróżnienia, aby uczynić tekst bardziej czytelnym.

#### Bądź otwarty na feedback
   - Zachęcaj użytkowników do zgłaszania błędów w dokumentacji czy proponowania ulepszeń.
   - Pamiętaj, że Twoi użytkownicy są najlepszym źródłem informacji o tym, jak ulepszyć dokumentację.

### Automatyczne generowanie dokumentacji dla API

Współczesne aplikacje często korzystają z interfejsów API, które pozwalają na komunikację między różnymi usługami. Aby ułatwić korzystanie z takiego API, kluczowe jest dostarczenie dokładnej, ale i czytelnej dokumentacji. Automatyczne generowanie dokumentacji może znacząco przyspieszyć ten proces, jednocześnie zapewniając, że jest ona zawsze aktualna.

W Pythonie możemy wykorzystać narzędzie **Sphinx** do generowania dokumentacji, a w kontekście API, jego rozszerzenie `sphinx-apidoc` jest szczególnie przydatne.

#### Krok po kroku:

1. **Instalacja sphinx-apidoc**:
    Jeśli jeszcze nie masz zainstalowanego `sphinx-apidoc`, możesz to zrobić za pomocą pip:

    ```bash
    pip install sphinx
    ```

2. **Generowanie dokumentacji dla API**:
    Przejdź do folderu, w którym znajduje się Twoja dokumentacja, a następnie użyj poniższego polecenia:

    ```bash
    sphinx-apidoc -o docs/source/api/ <ścieżka do katalogu z kodem>
    ```

    To polecenie generuje plik `api.rst`, który zawiera automatycznie wygenerowane informacje na temat Twojego API.

3. **Dodanie wygenerowanej dokumentacji do głównej zawartości**:
    Teraz musisz dodać nowo utworzony plik `api.rst` do głównego pliku `index.rst`, aby był on dostępny w głównym menu dokumentacji:

    ```rst
    .. toctree::
        :maxdepth: 2
        :caption: Spis treści:

        api
    ```

4. **Generowanie strony internetowej z dokumentacją**:
    Po dodaniu pliku `api.rst` do `index.rst`, wystarczy uruchomić polecenie:

    ```bash
    make html
    ```

    Dzięki temu uzyskasz stronę internetową zawierającą nowo wygenerowaną dokumentację.

### Linki

* [Style Guide for Developers](https://developers.google.com/style)
* [Sphinx Official Documentation](https://www.sphinx-doc.org/en/master/)
