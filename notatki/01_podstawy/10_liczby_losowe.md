## Liczby losowe w Pythonie

W wielu aplikacjach, zwłaszcza w symulacjach i grach, potrzebujemy generować liczby losowe. Python oferuje moduł `random`, który dostarcza różnorodne funkcje do generowania liczb losowych i wykonania innych operacji losowych.

### Funkcje podstawowe:

- `random.random()`: Zwraca liczbę zmiennoprzecinkową z zakresu `[0, 1)`.
- `random.uniform(a, b)`: Zwraca liczbę zmiennoprzecinkową z zakresu `[a, b]` lub `[b, a]` w zależności od wartości `a` i `b`.
- `random.randint(a, b)`: Zwraca losową liczbę całkowitą z zakresu `[a, b]`, włącznie z obiema wartościami końcowymi.

### Funkcje dla zaawansowanych rozkładów prawdopodobieństwa:

- `random.gauss(mu, sigma)`: Generuje liczbę według rozkładu normalnego (Gaussa) o średniej `mu` i odchyleniu standardowym `sigma`.
- `random.expovariate(lambd)`: Zwraca liczbę z rozkładu wykładniczego, gdzie `lambd` jest równy 1 dzielone przez średnią żądaną wartość.
- `random.weibullvariate(alpha, beta)`: Zwraca liczbę z rozkładu Weibulla o określonych parametrach.
- `random.vonmisesvariate(mu, kappa)`: Zwraca liczbę z rozkładu von Misesa, który jest stosowany głównie w badaniach w zakresie kierunków.

### Przykład użycia:

```python
import random

# Generowanie liczb z rozkładu normalnego o średniej 0 i odchyleniu standardowym 1
samples_gauss = [random.gauss(0, 1) for _ in range(10)]
print("Próbki z rozkładu normalnego:", samples_gauss)

# Generowanie liczb z rozkładu wykładniczego o parametrze 0.5
samples_exp = [random.expovariate(0.5) for _ in range(10)]
print("Próbki z rozkładu wykładniczego:", samples_exp)
```

Generowanie liczb losowych jest podstawą wielu algorytmów i symulacji, dlatego ważne jest zrozumienie dostępnych w Pythonie funkcji i ich zastosowania w różnych scenariuszach.
