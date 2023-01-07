
### Procesy
Procesy to niezależne od siebie instancje programów wykonywane w systemie operacyjnym. Procesy dzielą pamięć i zasoby systemu, takie jak pliki i gniazda sieciowe. W odróżnieniu od wątków, procesy są całkowicie niezależne od siebie i nie mogą udostępniać swoich zmiennych.

W Pythonie mamy moduł <code>multiprocessing</code>, który umożliwia tworzenie procesów. Możemy użyć go, aby uruchomić nasz kod w osobnym procesie.

```python
import multiprocessing
import time

def worker():
    print("Rozpoczynam prace")
    time.sleep(2)
    print("Koncze prace")

p = multiprocessing.Process(target=worker)
p.start()
```

W przeciwieństwie do wątków, procesy nie mogą być zatrzymywane. Jeśli chcemy zatrzymać proces, musimy go zakończyć. W tym celu możemy użyć metody <code>terminate()</code>.

```python
p.terminate()
```

Procesy są dobrym wyborem, gdy chcemy uruchamiać kod równolegle, ale nie potrzebujemy udostępniać zmiennych między procesami. Procesy są również dobrym wyborem, gdy chcemy uniknąć problemu GIL, który dotyczy wątków w Pythonie. Należy jednak pamiętać, że procesy są bardziej zasobożerne niż wątki i nie nadają się do wszystkich zastosowań.
