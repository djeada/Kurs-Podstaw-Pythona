## Logowanie

W większych aplikacjach, zwłaszcza tych uruchamianych w środowiskach produkcyjnych lub działających przez długi czas, kluczowe znaczenie ma **logowanie**. Monitorowanie aplikacji za pomocą logów pozwala na analizę jej działania, identyfikację błędów, przewidywanie potencjalnych problemów oraz ocenę wydajności. Moduł `logging` w Pythonie zapewnia rozbudowane mechanizmy logowania, oferując precyzyjną kontrolę nad tym, jakie informacje są rejestrowane i gdzie są przechowywane.

### Dlaczego logowanie jest niezbędne?

Logi umożliwiają:

1. Możemy monitorować ważne etapy procesu, takie jak uruchamianie serwerów, połączenia z bazami danych, czy inne krytyczne operacje.
2. Dzięki logom możemy szybko zidentyfikować przyczynę błędu lub problemu wydajnościowego.
3. Logi mogą być używane do monitorowania operacji, takich jak zmiany w systemie, dostęp do wrażliwych danych, czy inne ważne zdarzenia, które mogą być potrzebne w przyszłości do celów audytu.
4. Zapisując informacje o nieudanych próbach logowania, zmianach uprawnień czy innych podejrzanych operacjach, logi mogą wspierać ochronę przed zagrożeniami.
5. Analiza logów umożliwia znalezienie wąskich gardeł w wydajności aplikacji oraz monitorowanie jej zasobów.

### Poziomy logów: Szczegółowość i priorytet

Pythonowy moduł `logging` wprowadza hierarchię poziomów logów, które pozwalają na różnicowanie istotności komunikatów. Każdy komunikat ma przypisany jeden z następujących poziomów:

| **Poziom logu** | **Wartość numeryczna** | **Opis** |
| --------------- | ---------------------- | -------- |
| **CRITICAL**    | 50                     | Błędy krytyczne, które mogą skutkować przerwaniem działania aplikacji |
| **ERROR**       | 40                     | Błędy istotne, które wymagają interwencji, ale aplikacja może kontynuować działanie |
| **WARNING**     | 30                     | Ostrzeżenia o potencjalnych problemach, które mogą wystąpić w przyszłości |
| **INFO**        | 20                     | Informacje o zwykłych operacjach aplikacji |
| **DEBUG**       | 10                     | Szczegółowe informacje, przydatne w trakcie debugowania i diagnozowania aplikacji |
| **NOTSET**      | 0                      | Brak ustawionego poziomu, logowanie nie zostanie wykonane |

Każdy komunikat logowania ma określony priorytet. Na przykład, ustawiając poziom logowania na `INFO`, będziemy zapisywać wszystkie logi na poziomie `INFO` i wyższe (tj. `INFO`, `WARNING`, `ERROR`, `CRITICAL`).

### Podstawowe logowanie do konsoli

Podstawowym i najczęściej używanym sposobem logowania jest wyświetlanie komunikatów na konsoli. Pythonowy moduł `logging` pozwala na szybkie skonfigurowanie logowania za pomocą funkcji `logging.basicConfig()`:

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Informacja o działaniu programu.")  # Ten komunikat zostanie wyświetlony
logging.warning("Ostrzeżenie o potencjalnym problemie.")
logging.error("Błąd, który wymaga uwagi.")
```

W powyższym przykładzie konfigurujemy system logowania z poziomem logowania ustawionym na `INFO`, co oznacza, że wszystkie komunikaty od poziomu `INFO` wzwyż zostaną wyświetlone na konsoli. Poziom logowania można zmieniać w zależności od potrzeb – na przykład, w środowisku produkcyjnym można ustawić poziom `ERROR` lub `WARNING`, aby unikać nadmiernej ilości logów, podczas gdy w trakcie programowania warto ustawić poziom `DEBUG`, aby uzyskać jak najwięcej informacji o stanie programu.

### Logowanie do pliku

Często zachodzi potrzeba zachowania logów w plikach, aby móc przeanalizować je później, zwłaszcza w przypadku aplikacji produkcyjnych. Moduł `logging` umożliwia łatwą konfigurację logowania do pliku, co jest niezbędne do długoterminowego monitorowania działania aplikacji.

#### Przykład logowania do pliku

```python
import logging

# Tworzenie loggera
logger = logging.getLogger('moj_logger')
logger.setLevel(logging.INFO)

# Tworzenie handlera do logowania do pliku
file_handler = logging.FileHandler('aplikacja.log')
file_handler.setLevel(logging.WARNING)

# Formatowanie logów
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Dodawanie handlera do loggera
logger.addHandler(file_handler)

# Przykłady logowania
logger.info("To jest poziom INFO.")  # Nie zostanie zapisany do pliku, bo poziom file_handler to WARNING
logger.warning("To jest poziom WARNING.")  # Zostanie zapisany do pliku
logger.error("To jest poziom ERROR.")  # Zostanie zapisany do pliku
```

Omówienie kodu:

1. Tworzymy obiekt `logger`, który zarządza wszystkimi operacjami logowania. `getLogger()` przyjmuje opcjonalną nazwę, która pozwala na tworzenie wielu loggerów, niezależnych od siebie.
2. Używamy obiektu `FileHandler`, aby wysłać logi do pliku `aplikacja.log`. Możemy tworzyć różne handlery do wysyłania logów do różnych miejsc (np. pliki, konsola, systemy zewnętrzne).
3. Za pomocą obiektu `Formatter` definiujemy format wiadomości logów, który w tym przypadku zawiera datę, poziom logowania i sam komunikat.
4. Logi na poziomie `INFO` nie zostaną zapisane do pliku, ponieważ poziom handlera to `WARNING`. Zapisane zostaną tylko komunikaty o poziomie `WARNING` i wyższym (`ERROR`, `CRITICAL`).

### Zaawansowane konfiguracje logowania

Pythonowy moduł `logging` oferuje zaawansowane mechanizmy konfiguracji, w tym możliwość używania wielu handlerów, logowania w różnych formatach oraz używania różnych poziomów logowania dla różnych komponentów aplikacji.

#### Logowanie do konsoli i pliku jednocześnie

Możemy skonfigurować logger w taki sposób, aby logi były wyświetlane zarówno na konsoli, jak i zapisywane do pliku.

```python
import logging

# Tworzenie loggera
logger = logging.getLogger('dual_logger')
logger.setLevel(logging.DEBUG)

# Handler do konsoli
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Handler do pliku
file_handler = logging.FileHandler('aplikacja_debug.log')
file_handler.setLevel(logging.ERROR)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Dodawanie handlerów do loggera
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Logowanie
logger.debug("To jest poziom DEBUG.")  # Zostanie wyświetlony na konsoli
logger.error("To jest poziom ERROR.")  # Zostanie zapisany do pliku i wyświetlony na konsoli
```

#### Używanie różnych loggerów w jednej aplikacji

W większych aplikacjach zaleca się stosowanie wielu loggerów dla różnych modułów lub komponentów. Każdy logger może być niezależnie konfigurowany, co pozwala na precyzyjne kontrolowanie logowania.

```python
import logging

# Logger dla modułu A
logger_A = logging.getLogger('modul_A')
logger_A.setLevel(logging.DEBUG)
handler_A = logging.FileHandler('modul_A.log')
logger_A.addHandler(handler_A)

# Logger dla modułu B
logger_B = logging.getLogger('modul_B')
logger_B.setLevel(logging.WARNING)
handler_B = logging.FileHandler('modul_B.log')
logger_B.addHandler(handler_B)

# Przykłady logowania
logger_A.debug("Log z modułu A - DEBUG")
logger_B.warning("Log z modułu B - WARNING")
```

#### Rzeczywisty przypadek logowania rotacyjnego

W aplikacjach działających przez długi czas pliki logów mogą szybko rosnąć, dlatego Python oferuje mechanizm rotacyjnego logowania za pomocą `RotatingFileHandler`. Ten handler automatycznie tworzy nowe pliki logów po przekroczeniu określonej wielkości.

```python
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('rotacyjny_logger')
logger.setLevel(logging.INFO)

# Handler rotacyjny
rotating_handler = RotatingFileHandler('rotacyjny_log.log', maxBytes=1024, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
rotating_handler.setFormatter(formatter)

logger.addHandler(rotating_handler)

# Generowanie logów
for i in range(100):
    logger.info(f"Log numer {i}")
```

Działanie rotacyjnego handlera:

1. **maxBytes** to maksymalny rozmiar pojedynczego pliku logu w bajtach (tutaj 1024 bajty).
2. **backupCount** to liczba zapasowych plików, które zostaną zachowane (tutaj 3 pliki).
3. Po przekroczeniu rozmiaru pliku nowy log jest zapisywany w nowym pliku, a najstarszy plik jest usuwany.
