
## Asyncio

Asyncio to moduł umożliwiający programowanie asynchroniczne. Asynchroniczne programowanie polega na wykonywaniu wielu zadań jednocześnie, bez konieczności blokowania głównego wątku programu. Aby funkcja mogła zostać wykonana asynchronicznie, należy użyć słowa kluczowego async oraz await.

Przykład użycia asyncio:

```python
import asyncio

async def main():
    await asyncio.sleep(1)
    print("Hello, world!")

asyncio.run(main())
```

W tym przykładzie, funkcja `main` jest oznaczona jako `async`, co oznacza, że będzie wykonywana asynchronicznie. Funkcja `asyncio.sleep(1)` jest funkcją, która zatrzymuje wykonanie wątku na 1 sekundę. Słowo kluczowe `await` jest używane do oznaczenia miejsca, w którym wątek ma czekać na zakończenie wykonywania funkcji `asyncio.sleep(1)`.

Moduł `asyncio` umożliwia tworzenie wielu wątków jednocześnie, co pozwala na lepsze wykorzystanie zasobów komputera. Należy jednak pamiętać, że `asyncio` nie jest rozwiązaniem wszystkich problemów związanych z wielowątkowością. W niektórych przypadkach lepszym rozwiązaniem może być użycie biblioteki `threading` lub `multiprocessing`.
