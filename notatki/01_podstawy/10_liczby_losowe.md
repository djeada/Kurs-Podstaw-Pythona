## Liczby losowe

W wielu aplikacjach, zwłaszcza w symulacjach, grach oraz analizach statystycznych, potrzebujemy generować liczby losowe. Python oferuje moduł `random`, który dostarcza różnorodne funkcje do generowania liczb losowych oraz wykonywania innych operacji losowych. Dzięki temu modułowi możemy łatwo implementować różne algorytmy oparte na przypadkowości.

### Podstawowe funkcje

#### `random.random()`
- Zwraca liczbę zmiennoprzecinkową z zakresu `[0, 1)`.
- Jest to podstawowa funkcja generująca losową liczbę zmiennoprzecinkową.

```python
import random
print(random.random())  # Np. 0.37444887175646646
```

#### `random.uniform(a, b)`
- Zwraca losową liczbę zmiennoprzecinkową z zakresu `[a, b]` lub `[b, a]` w zależności od wartości `a` i `b`.
- Używana do generowania losowych liczb zmiennoprzecinkowych w określonym zakresie.

```python
print(random.uniform(1, 10))  # Np. 5.422116796485917
```

#### `random.randint(a, b)`
- Zwraca losową liczbę całkowitą z zakresu `[a, b]`, włącznie z obiema wartościami końcowymi.
- Przydatna do generowania losowych liczb całkowitych.

```python
print(random.randint(1, 10))  # Np. 7
```

### Funkcje dla zaawansowanych rozkładów prawdopodobieństwa

#### `random.gauss(mu, sigma)`
- Generuje liczbę według rozkładu normalnego (Gaussa) o średniej `mu` i odchyleniu standardowym `sigma`.
- Stosowany w analizach statystycznych, symulacjach Monte Carlo i wielu innych dziedzinach.

```python
samples_gauss = [random.gauss(0, 1) for _ in range(10)]
print("Próbki z rozkładu normalnego:", samples_gauss)
```

#### `random.expovariate(lambd)`
- Zwraca liczbę z rozkładu wykładniczego, gdzie `lambd` jest równy 1 dzielone przez średnią żądaną wartość.
- Używany w modelowaniu czasów między zdarzeniami w procesach Poissona.

```python
samples_exp = [random.expovariate(0.5) for _ in range(10)]
print("Próbki z rozkładu wykładniczego:", samples_exp)
```

#### `random.weibullvariate(alpha, beta)`
- Zwraca liczbę z rozkładu Weibulla o określonych parametrach.
- Stosowany w analizie niezawodności oraz w modelowaniu rozkładów czasów życia.

```python
samples_weibull = [random.weibullvariate(1.5, 1) for _ in range(10)]
print("Próbki z rozkładu Weibulla:", samples_weibull)
```

#### `random.vonmisesvariate(mu, kappa)`
- Zwraca liczbę z rozkładu von Misesa, który jest stosowany głównie w badaniach w zakresie kierunków.
- Używany w analizie danych cyklicznych, takich jak kierunki wiatrów, fazy księżyca itp.

```python
samples_vonmises = [random.vonmisesvariate(0, 1) for _ in range(10)]
print("Próbki z rozkładu von Misesa:", samples_vonmises)
```

### Przykłady użycia

#### Generowanie liczb z rozkładu normalnego o średniej 0 i odchyleniu standardowym 1

```python
import random
samples_gauss = [random.gauss(0, 1) for _ in range(10)]
print("Próbki z rozkładu normalnego:", samples_gauss)
```

#### Generowanie liczb z rozkładu wykładniczego o parametrze 0.5

```python
samples_exp = [random.expovariate(0.5) for _ in range(10)]
print("Próbki z rozkładu wykładniczego:", samples_exp)
```

### Inne przydatne funkcje

#### `random.choice(seq)`
- Zwraca losowy element z niepustej sekwencji.
- Używany do losowego wybierania elementu z listy, krotki lub innej sekwencji.

```python
choices = ['jabłko', 'banan', 'pomarańcza']
print(random.choice(choices))  # Np. 'banan'
```

#### `random.shuffle(seq)`
- Przekształca sekwencję w miejscu, losowo mieszając jej elementy.
- Przydatny do losowego mieszania elementów listy.

```python
deck = list(range(1, 53))  # Talia kart
random.shuffle(deck)
print(deck)  # Np. [23, 1, 17, ...]
```

#### `random.sample(population, k)`
- Zwraca listę k unikalnych elementów wylosowanych z populacji.
- Używany do losowego wybierania próbek bez zamiany.

```python
population = list(range(100))
sample = random.sample(population, 10)
print(sample)  # Np. [82, 3, 72, 54, ...]
```
