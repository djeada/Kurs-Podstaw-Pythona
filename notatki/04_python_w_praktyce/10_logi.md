## Logowanie

Podczas tworzenia większych aplikacji niezbędne jest monitorowanie ich działania, zwłaszcza gdy są one uruchamiane przez długi czas. Logi pozwalają na zapisywanie i analizowanie działania programu, co jest niezwykle ważne przy diagnozowaniu problemów czy monitorowaniu postępów. Moduł `logging` w Pythonie oferuje rozbudowane narzędzia do tworzenia i zarządzania logami.

### Poziomy logów

Logi można kategoryzować na podstawie ich ważności. Oto dostępne poziomy logów w module `logging`:

| Poziom logu  | Wartość | Opis |
| ------------ | ------- | ---- |
| CRITICAL     | 50      | Błędy krytyczne, które mogą powodować przerwanie działania programu |
| ERROR        | 40      | Błędy, które nie zatrzymują działania programu, ale wymagają uwagi |
| WARNING      | 30      | Ostrzeżenia o potencjalnych problemach w przyszłości |
| INFO         | 20      | Ogólne informacje o działaniu programu |
| DEBUG        | 10      | Szczegółowe informacje, przydatne podczas debugowania |
| NOTSET       | 0       | Poziom domyślny dla loggerów |

### Logowanie do konsoli

W celu wypisania informacji na konsolę możemy skorzystać z funkcji takich jak `logging.info()`, `logging.warning()` itp.:

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Przykladowa wiadomosc INFO.")
logging.warning("Przykladowa wiadomosc WARNING.")
```

W tym przykładzie ustawiliśmy poziom logów na INFO, co oznacza, że widoczne będą komunikaty o poziomie INFO oraz wszystkie o wyższym priorytecie.

### Logowanie do pliku

Logowanie do pliku jest niezbędne w sytuacjach, gdy logi muszą być przechowywane i analizowane w przyszłości:

```python
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

fh = logging.FileHandler('plik.log')
fh.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)

logger.info("Przykladowa wiadomosc INFO.")  # Ten komunikat nie zostanie zapisany do pliku
logger.warning("Przykladowa wiadomosc WARNING.")
```

W powyższym kodzie, obiekt `logger` jest skonfigurowany do logowania komunikatów o poziomie INFO i wyższych. Dodatkowo dodaliśmy `FileHandler`, który zapisuje logi o poziomie WARNING i wyższych do pliku 'plik.log'. Użyliśmy również formatter do określenia formatu logów, dodając informacje o dacie i czasie.
