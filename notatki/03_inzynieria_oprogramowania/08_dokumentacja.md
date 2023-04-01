
## Dokumentacja

Dokumentacja to ważny element każdego projektu, służący do opisania działania aplikacji oraz jej funkcjonalności. Narzędziem służącym do tworzenia dokumentacji w Pythonie jest SPHINX. Pozwala on na tworzenie dokumentacji w różnych formatach, takich jak HTML, LaTeX, epub, czy zwykły tekst. Możliwe jest również przekształcenie pliku w formacie LaTeX do PDF.

Aby zbudować szkielet dokumentacji, wystarczy uruchomić komendę:

```
quickstart
```

SPHINX zapyta cię o kilka szczegółów dotyczących projektu, na podstawie których wygeneruje odpowiednie pliki startowe i wypełni je treścią.

Aby utworzyć dokumentację z plików konfiguracyjnych, użyj komendy:

```
make html
```

Program poinformuje cię o pomyślnym utworzeniu dokumentacji, jeśli w trakcie procesu nie pojawią się żadne błędy. W przeciwnym razie proces tworzenia dokumentacji zostanie przerwany, a na konsoli zostaną wyświetlone komunikaty o błędach.

### reStructuredText

Plikiem startowym dokumentacji jest `index.rst`. Zapisany jest on w formacie `reStructuredText`, który jest rozszerzeniem języka markdown. Jego głównym atutem jest możliwość instalowania przydatnych pluginów. Linkowanie plików jest również uproszczone, co jest ważne w dokumentacji. Komenda `make html` generuje na podstawie plików z rozszerzeniem `.rst` odpowiadające im pliki html.

### Jak pisać dobrą dokumentację?

# Wskazówki dotyczące tworzenia dokumentacji

1. **Zacznij od tutoriali**
   - Pokaż użytkownikowi jak zainstalować oraz uruchomić twoją aplikację.
   - Przygotuj scenariusze użycia programu.
   - Zaprezentuj, do czego służy każdy z elementów graficznych.
   - Tutoriale to nie to samo co dokumentacja, ale dobrze przygotowane poradniki pozwolą ci zebrać wiele informacji, które później możesz przetworzyć na dokumentację.

2. **Korzystaj z narzędzi automatyzujących pracę**
   - Sphinx pozwala na tworzenie dokumentacji w różnych formatach.
   - Jeśli używasz języka Python, używaj `docstrings`, czyli umieszczaj dokumentacje kodu bezpośrednio w plikach źródłowych.

3. **Pamiętaj o aktualności dokumentacji**
   - Utrzymuj dokumentację w równowadze z aktualną wersją aplikacji.
   - W razie zmian w kodzie, pamiętaj o odpowiednim zaktualizowaniu dokumentacji.

4. **Staraj się być zrozumiały**
   - Unikaj skomplikowanych zwrotów i nieznanych szerzej pojęć.
   - Jeśli masz taką możliwość, dodaj przykłady użycia konkretnych funkcji.

5. **Dopracuj szczegóły**
   - Zadbaj o poprawność gramatyczną i ortograficzną.
   - Dodaj linki do dokumentacji zewnętrznych bibliotek, jeśli korzystasz z nich w swoim projekcie.

6. **Utrzymuj porządek**
   - Dokumentacja powinna być czytelna i przejrzysta.
   - Dziel informacje na krótkie rozdziały i sekcje.

7. **Zachęcaj do zgłaszania błędów i propozycji ulepszeń**
   - Jeśli użytkownicy znajdą błędy lub będą mieć propozycje ulepszeń, chętnie przyjmij ich uwagi.

### Automatyczne generowanie dokumentacji do API

Jeśli tworzysz aplikację z interfejsem API, warto zadbać o automatyczne generowanie dokumentacji, która będzie zawierała wszystkie dostępne endpointy, opis ich działania, a także informacje o przyjmowanych i zwracanych parametrach. W Pythonie jednym z popularnych narzędzi do tego celu jest <a href="https://www.sphinx-doc.org/en/master/">Sphinx</a>.

Aby skorzystać z tej funkcjonalności, należy zainstalować rozszerzenie <code>sphinx-apidoc</code> i uruchomić go z odpowiednimi opcjami. W folderze z dokumentacją należy wywołać polecenie:

    sphinx-apidoc -o docs/source/api/ <ścieżka do katalogu z kodem>

To polecenie utworzy plik <code>api.rst</code> z automatycznie wygenerowaną dokumentacją. Następnie należy dodać go do pliku <code>index.rst</code>, aby pojawił się w głównym menu dokumentacji.

```rst
.. toctree::
    :maxdepth: 2
    :caption: Spis treści:

    api
```

Po uruchomieniu polecenia <code>make html</code> będzie można zobaczyć wygenerowaną dokumentację na stronie internetowej.

### Linki

* https://developers.google.com/style
