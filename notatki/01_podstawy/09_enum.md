### Enum

Enum (od słowa enumerate - numerować) to specjalny typ danych, który pozwala na tworzenie stałych symbolicznych nazw dla wartości. W przeciwieństwie do zwykłych stałych, wartości Enumów są obiektami, a nie prostymi wartościami. Enum jest szczególnie przydatny, gdy chcemy przypisać nazwy symboliczne do wartości liczbowych.

Wewnątrz definicji klasy Enum tworzymy atrybuty klasy, które będą reprezentować nasze stałe symboliczne. Wartości atrybutów są automatycznie przypisane do kolejnych liczb całkowitych, począwszy od 1. Możemy również przypisać im jawnie określoną wartość.

Przykład definicji Enum dla kolorów:

```python
class Kolor(enum.Enum):
    ZIELONY = enum.auto()
    CZERWONY = enum.auto()
    NIEBIESKI = enum.auto()

kolor_a = Kolor.ZIELONY
kolor_b = Kolor.CZERWONY

print(kolor_a.name) # ZIELONY
print(kolor_a.value) # 1

print(kolor_b.name) # CZERWONY
print(kolor_b.value) # 2
```
