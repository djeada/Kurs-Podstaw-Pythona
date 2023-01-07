### Liczby losowe

Liczby losowe są często potrzebne w programach, gdyż umożliwiają symulację różnych zjawisk. W Pythonie do generowania liczb losowych można użyć modułu <code>random</code>. Zawiera on wiele przydatnych funkcji, takich jak <code>random.random()</code> czy <code>random.uniform(a,b)</code>, które pozwalają na wylosowanie liczby zmiennoprzecinkowej z odpowiedniego przedziału. Możliwe jest również losowanie liczb całkowitych za pomocą funkcji <code>random.randint(a,b)</code>.

- <code>random.random()</code> wylosuje liczbę zmiennoprzecinkową z przedziału od *0* do *1*.
- <code>random.uniform(a,b)</code> wylosuje liczbę zmiennoprzecinkową z przedziału od *a* do *b*.
- <code>random.randint(a,b)</code> wylosuje liczbę całkowitą z przedziału od *a* do *b*.

Rozkład prawdopodobieństwa opisuje, jakie wartości są bardziej prawdopodobne, a jakie mniej prawdopodobne w losowaniu. Najprostszym przykładem rozkładu prawdopodobieństwa jest rozkład jednostajny, gdzie prawdopodobieństwo wystąpienia dowolnej wartości w przedziale `[a,b]` jest stałe. Wartość gęstości prawdopodobieństwa poza tym przedziałem wynosi 0.

Innym rodzajem rozkładu jest rozkład Gaussa, gdzie wartości zbliżone do średniej mają znacznie większe prawdopodobieństwo wystąpienia niż te oddalone od średniej. Wartości tego rodzaju rozkładu są często wykorzystywane w symulacjach, gdyż przy wpływie wielu czynników rozkład prawdopodobieństwa jest zazwyczaj zbliżony do krzywej Gaussa, co opisuje centralne twierdzenie graniczne."

- `random.gauss(mu, sigma)` - losuje liczbę z rozkładu normalnego o średniej `mu` i odchyleniu standardowym `sigma`.
- `random.expovariate(lambd)` - losuje liczbę z rozkładu wykładniczego o parametrze `lambd`.
- `random.weibullvariate(alpha, beta)` - losuje liczbę z rozkładu Weibulla o parametrach `alpha` i `beta`.
- `random.vonmisesvariate(mu, kappa)` - losuje liczbę z rozkładu von Misesa o parametrach `mu` i `kappa`.

Przykład użycia:

```python
import random

# losowanie liczb z rozkladu normalnego o sredniej 0 i odchyleniu standardowym 1
samples = [random.gauss(0, 1) for _ in range(10)]
print(samples)

# losowanie liczb z rozkladu wykladniczego o parametrze 0.5
samples = [random.expovariate(0.5) for _ in range(10)]
print(samples)
```
