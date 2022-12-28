
### Logi

Większość programów, które tworzyliśmy w obrębie tego kursu, była jednorazowo uruchamiana i od razu zamykana. W prawdziwym świecie programy mogą działać godzinami, dniami lub nawet całymi latami. W takim przypadku wypadałoby poza samym efektem działania programu co jakiś czas otrzymać od programu informacje o tym, co aktualnie robi, wraz z ewentualnymi komunikatami o błędach. Takie informacje, zwane logami, są często zapisywane do osobnego pliku.

Moduł `logging` zawiera wiele przydatnych funkcjonalności do tworzenia logów.

Mamy dostępnych kilka poziomów logów:

| poziom | wartość |
| ------ | ------- | 
| CRITICAL | 50 | 
| ERROR | 40 | 
| WARNING | 30 | 
| INFO | 20 | 
| DEBUG | 10 | 
| NOTSET | 0 | 

Rzućmy okiem na prosty przykład, gdzie wypisujemy na konsoli komunikat "Przykładowa wiadomość":

    import logging

    logging.basicConfig(level=logging.INFO)
    logging.info("Przykladowa wiadomosc.")

W powyższym przykładzie, linia `logging.basicConfig(level=logging.INFO)` ustawia poziom logów na `INFO`. Poziomy logów określają ważność logów. W przypadku będą wyświetlane logi o poziomie `INFO` i wszystkie powyżej niego (np. `WARNING`, `ERROR`, `CRITICAL`). Linia `logging.info("Przykladowa wiadomosc.")` wyświetla komunikat "Przykladowa wiadomosc." na konsoli. W tym przypadku poziom logu jest ustawiony na `INFO`. Jeśli poziom logów ustawiony przez `logging.basicConfig()` jest równy lub wyższy niż poziom logu wyświetlanego przez `logging.info()`, komunikat zostanie wyświetlony. W przeciwnym razie komunikat nie zostanie wyświetlony.

Aby zapisać logi do pliku potrzebujemy obiektu do obsługi plików (FileHandler):

    import logging

    logger = logging.getLogger()

    fh = logging.FileHandler('plik.log')
    fh.setLevel(logging.WARNING)
    logger.addHandler(fh)

    logger.warning("Przykladowa wiadomosc.")

W powyższym przykładzie tworzymy najpierw obiekt `logger` służący do zarządzania logami, a następnie obiekt `fh` służący do zapisywania logów do pliku. Nazwa pliku podana jest jako argument 'plik.log'. Linia `fh.setLevel(logging.WARNING)` ustawia poziom logów dla obiektu `fh` na `WARNING`. Poziomy logów określają ważność logów. W przypadku ustawienia poziomu na `WARNING`, będą zapisywane logi o poziomie `WARNING` i wszystkie powyżej niego. Linia `logger.addHandler(fh)` dodaje obiekt `fh` do obiektu `logger`. W ten sposób logi wygenerowane przez `logger` będą zapisywane do pliku przez obiekt `fh`. Linia `logger.warning("Przykladowa wiadomosc.")` zapisuje komunikat "Przykladowa wiadomość" do pliku o nazwie 'plik.log'. 