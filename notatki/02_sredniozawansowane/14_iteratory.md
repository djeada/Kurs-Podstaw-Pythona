
### Iteratory

Pętla `for` jest narzędziem, które umożliwia przejście przez kolejne elementy sekwencji, takiej jak lista, ciąg znaków lub tuple. Możemy użyć pętli `for` w następujący sposób:

    for elem in lista:
       print(elem)

Wbudowane kolekcje, takie jak listy, ciągi znaków i tuple, posiadają metodę `__iter__()`, która zwraca iterator dla danej kolekcji. Iterator to obiekt, który umożliwia przejście przez elementy kolekcji po kolei. Możemy wywołać funkcję `next()` z przekazanym jako argument iterator, aby pobrać kolejny element kolekcji. Jeśli iterator nie ma już więcej elementów do zwrócenia, zostanie rzucony wyjątek `StopIteration`.

    lista = [1, 2, 3]
    iterator = iter(lista)
    print(next(iterator)) # wyswietli 1
    print(next(iterator)) # wyswietli 2
    print(next(iterator)) # wyswietli 3
    print(next(iterator)) # zostanie wyrzucony wyjatek

Ten mechanizm jest używany wewnętrznie przez pętlę `for`. Iteratory pozwalają na implementację własnych zasad przechodzenia przez kolekcję. Możemy stworzyć własną klasę iterowalną, implementując metodę `__iter__()` i używając słowa kluczowego `yield` w celu zwracania elementów kolekcji po kolei.

    class ObiektIterowalny:

      def __init__(self):
        self.lista_a = [3, 2, 1]
        self.lista_b = [-1, -2, -3]

      def __iter__(self):
        licznik = 0
        while licznik < len(self.lista_a) and len(self.lista_b):
          yield self.lista_a[licznik], self.lista_b[licznik]
          licznik+=1

    obiekt = ObiektIterowalny()

    for elem in obiekt:
      print(elem)
      
Dzięki temu, że nasz obiekt jest iterowalny, możemy używać go w pętli `for` w taki sam sposób, jak wbudowane kolekcje.