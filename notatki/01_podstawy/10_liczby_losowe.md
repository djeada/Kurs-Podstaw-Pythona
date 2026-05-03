## Liczby losowe: Generowanie i Rozkłady Prawdopodobieństwa

Liczby losowe odgrywają kluczową rolę w wielu obszarach nauki, technologii i przemysłu, takich jak symulacje komputerowe, gry, analiza statystyczna, uczenie maszynowe, a także w badaniach fizycznych i matematycznych. W Pythonie za generowanie liczb losowych odpowiada moduł `random`, który zapewnia szeroki wachlarz funkcji do generowania liczb losowych z różnych rozkładów prawdopodobieństwa.

Aby lepiej zrozumieć koncepcję losowości w programowaniu, warto zaznaczyć, że funkcje w module `random` nie generują "prawdziwie" losowych liczb, a jedynie **pseudolosowe**. Oznacza to, że liczby te są determinowane algorytmicznie, jednak z perspektywy większości zastosowań praktycznych mogą być uznawane za losowe.

### Algorytm generowania liczb pseudolosowych
Większość funkcji w module `random` opiera się na algorytmach typu **Mersenne Twister**, który jest zaawansowanym i popularnym generatorem liczb pseudolosowych. Pseudolosowe liczby to liczby generowane w taki sposób, że wydają się być losowe, ale w rzeczywistości są determinowane przez tzw. **ziarno** (ang. *seed*), które inicjalizuje generator.

Możemy ustawić ziarno za pomocą funkcji `random.seed()`. Dzięki temu sekwencje generowanych liczb mogą być reprodukowalne, co jest ważne w naukowych eksperymentach i testowaniu kodu.

```python
import random
random.seed(42)  # Inicjalizowanie generatora pseudolosowego
print(random.random())  # Zawsze zwróci tę samą wartość np. 0.6394267984578837
```

### Podstawowe funkcje generujące liczby losowe

#### `random.random()`

- Zwraca losową liczbę zmiennoprzecinkową z zakresu `[0, 1)`. Oznacza to, że dolny kraniec (0) jest zawarty, ale górny (1) już nie.
- Ta funkcja bazuje na rozkładzie **jednostajnym** (ang. *uniform distribution*), gdzie każda liczba z zakresu `[0, 1)` ma jednakowe prawdopodobieństwo wystąpienia.

Matematycznie można to wyrazić jako:

$$
X \sim U(0,1) \quad \text{gdzie} \quad X \in [0, 1)
$$

```python
import random
print(random.random())  # Np. 0.37444887175646646
```

#### `random.uniform(a, b)`
Zwraca losową liczbę zmiennoprzecinkową z przedziału `[a, b]`. Rozkład jest jednostajny na zadanym przedziale, co oznacza, że każda wartość w tym przedziale ma równe prawdopodobieństwo bycia wylosowaną.

Matematyczna definicja:

$$
X \sim U(a, b) \quad \text{gdzie} \quad X \in [a, b]
$$

```python
print(random.uniform(1, 10))  # Np. 5.422116796485917
```

#### `random.randint(a, b)`
Zwraca losową liczbę całkowitą z przedziału `[a, b]`, gdzie zarówno `a`, jak i `b` są włącznie. Jest to odpowiednik rozkładu jednostajnego dyskretnego na zbiorze liczb całkowitych.

Matematyczna definicja:

$$
X \sim U(\{a, a+1, ..., b\}) \quad \text{gdzie} \quad X \in \{a, a+1, ..., b\}
$$

```python
print(random.randint(1, 10))  # Np. 7
```

### Generowanie liczb z różnych rozkładów prawdopodobieństwa

#### `random.gauss(mu, sigma)`
Generuje losową liczbę zgodnie z rozkładem **normalnym** (Gaussa) o średniej `mu` i odchyleniu standardowym `sigma`. Rozkład normalny ma kluczowe znaczenie w statystyce, ponieważ wiele zjawisk naturalnych podlega temu rozkładowi.

Rozkład normalny można opisać wzorem:

$$
f(x; \mu, \sigma) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$

gdzie:
- `\mu` to średnia,
- `\sigma` to odchylenie standardowe.

```python
samples_gauss = [random.gauss(0, 1) for _ in range(10)]
print("Próbki z rozkładu normalnego:", samples_gauss)
```

#### `random.expovariate(lambd)`
Generuje liczby z **rozkładu wykładniczego** z parametrem `lambd`, gdzie `lambd` to odwrotność oczekiwanej wartości.

Rozkład wykładniczy opisuje czas między zdarzeniami w procesie Poissona i ma funkcję gęstości:

$$
f(x; \lambda) = \lambda e^{-\lambda x} \quad \text{dla} \quad x \geq 0
$$

gdzie `λ = 1 / E(X)`.

```python
samples_exp = [random.expovariate(0.5) for _ in range(10)]
print("Próbki z rozkładu wykładniczego:", samples_exp)
```

#### `random.weibullvariate(alpha, beta)`
Generuje liczby z **rozkładu Weibulla**, który jest używany w analizach niezawodności, np. do modelowania czasu życia urządzeń. Parametr `alpha` odpowiada za skalę, a `beta` za kształt rozkładu.

Funkcja gęstości rozkładu Weibulla jest opisana wzorem:

$$
f(x; \alpha, \beta) = \frac{\beta}{\alpha}\left(\frac{x}{\alpha}\right)^{\beta - 1}e^{-(x/\alpha)^\beta} \quad \text{dla} \quad x \geq 0
$$

```python
samples_weibull = [random.weibullvariate(1.5, 1) for _ in range(10)]
print("Próbki z rozkładu Weibulla:", samples_weibull)
```

#### `random.vonmisesvariate(mu, kappa)`
Zwraca liczby z **rozkładu von Misesa**, który jest odpowiednikiem rozkładu normalnego, ale na okręgu. Jest szeroko stosowany w badaniach kierunkowych, np. do analizy wektorów.

Funkcja gęstości ma postać:

$$
f(\theta; \mu, \kappa) = \frac{e^{\kappa \cos(\theta - \mu)}}{2\pi I_0(\kappa)} \quad \text{dla} \quad \theta \in [0, 2\pi]
$$

gdzie:

- `\mu` to wartość średnia (kierunkowa),
- `\kappa` to koncentracja wokół średniej.

```python
samples_vonmises = [random.vonmisesvariate(0, 1) for _ in range(10)]
print("Próbki z rozkładu von Misesa:", samples_vonmises)
```

### Praktyczne zastosowania funkcji losowych

#### `random.choice(seq)`
Zwraca losowy element z niepustej sekwencji, np. listy, krotki. Może być stosowana do losowego wyboru obiektu z grupy możliwych wartości.

```python
choices = ['jabłko', 'banan', 'pomarańcza']
print(random.choice(choices))  # Np. 'banan'
```

#### `random.shuffle(seq)`
Losowo przekształca sekwencję w miejscu, mieszając jej elementy. Przydatne do np. tasowania talii kart.

```python
deck = list(range(1, 53))  # Talia kart
random.shuffle(deck)
print(deck)  # Np. [23, 1, 17, ...]
```

#### `random.sample(population, k)`
Zwraca listę `k` unikalnych elementów wylosowanych z `population`. Używane do losowego wybierania próbek bez zamiany.

```python
population = list(range(100))
sample = random.sample(population, 10)
print(sample)  # Np. [82, 3, 72, 54, ...]
```

#### `random.choices(population, weights=None, k=1)`

Zwraca listę `k` elementów wylosowanych **ze zwracaniem** (element może się powtarzać). Opcjonalnie można podać wagi dla każdego elementu:

```python
import random

# Bez wag — równe prawdopodobieństwo
print(random.choices(["reszka", "orzeł"], k=5))
# Np. ['orzeł', 'reszka', 'orzeł', 'orzeł', 'reszka']

# Z wagami — orzeł 3x częściej niż reszka
print(random.choices(["orzeł", "reszka"], weights=[3, 1], k=10))
```

### Praktyczne przykłady zastosowań

#### Symulacja rzutu kością

```python
import random

def rzut_koscia(sciany=6):
    return random.randint(1, sciany)

def rzuc_wielokrotnie(ile, sciany=6):
    return [rzut_koscia(sciany) for _ in range(ile)]

print(rzuc_wielokrotnie(5))           # Np. [3, 1, 6, 2, 5]
print(rzuc_wielokrotnie(3, sciany=20)) # Rzut k20
```

#### Tasowanie talii kart

```python
import random

kolory = ["♠", "♥", "♦", "♣"]
wartosci = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
talia = [f"{w}{k}" for k in kolory for w in wartosci]

random.shuffle(talia)
print("Pierwszych 5 kart:", talia[:5])
reka = random.sample(talia, 5)
print("Losowa ręka:", reka)
```

#### Generator haseł

```python
import random
import string

def generuj_haslo(dlugosc=12, cyfry=True, znaki_specjalne=True):
    znaki = string.ascii_letters
    if cyfry:
        znaki += string.digits
    if znaki_specjalne:
        znaki += "!@#$%^&*"
    return "".join(random.choices(znaki, k=dlugosc))

print(generuj_haslo())          # Np. 'aB3!kL9#mNzQ'
print(generuj_haslo(8, False, False))  # Tylko litery, 8 znaków
```

#### Symulacja loteryjki

```python
import random

def losowanie_lotto(ile=6, zakres=49):
    return sorted(random.sample(range(1, zakres + 1), ile))

print(losowanie_lotto())          # Np. [3, 12, 25, 33, 41, 47]
print(losowanie_lotto(5, 90))     # 5 z 90
```

### Moduł `secrets` — kryptograficznie bezpieczne losowanie

Moduł `random` **nie jest bezpieczny kryptograficznie** — generowane przez niego sekwencje można przewidzieć. Do zadań bezpieczeństwa (np. tokeny sesji, kody weryfikacyjne) należy używać modułu `secrets`:

```python
import secrets

# Bezpieczny token szesnastkowy
token = secrets.token_hex(32)    # 64 znaki hex
print(token)  # Np. 'a3f9...c7e2'

# Token URL-safe (base64)
url_token = secrets.token_urlsafe(16)  # ~22 znaki
print(url_token)  # Np. 'X9kJ7mQzP...'

# Bezpieczna losowa liczba całkowita
print(secrets.randbelow(100))    # losowa z [0, 99]

# Bezpieczny wybór z kolekcji
print(secrets.choice(["tak", "nie", "może"]))

# Bezpieczny PIN 6-cyfrowy
import string
pin = "".join(secrets.choice(string.digits) for _ in range(6))
print(pin)  # Np. '847302'
```

| Cecha                | `random`                       | `secrets`                         |
|----------------------|--------------------------------|-----------------------------------|
| Cel                  | Symulacje, gry, testy          | Kryptografia, bezpieczeństwo      |
| Przewidywalność      | Tak (deterministyczny z seedem) | Nie                              |
| Szybkość             | Szybszy                        | Wolniejszy                        |
| Seed                 | Tak (`random.seed()`)          | Nie                               |
| Zalecany do haseł    | **Nie**                        | **Tak**                           |

### Reprodukowalność — `random.seed()`

W testach i symulacjach naukowych często potrzebujemy tej samej sekwencji losowej przy każdym uruchomieniu. Służy do tego `seed`:

```python
import random

random.seed(42)
print([random.randint(1, 10) for _ in range(5)])  # [1, 10, 2, 5, 10]

random.seed(42)  # reset z tym samym seedem
print([random.randint(1, 10) for _ in range(5)])  # [1, 10, 2, 5, 10]  — identyczne!
```

Bez ustawienia seedu Python automatycznie używa aktualnego czasu systemowego, co daje różne wyniki przy każdym uruchomieniu.
