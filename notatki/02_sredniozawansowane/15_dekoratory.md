
### Dekoratory
Przy pomocy dekoratorów możemy rozszerzać funkcjonalność istniejących funkcji bez ich modyfikowania. Możemy też używać ich jako dodatkowego sposobu na zabezpieczenie funkcji przed nieprawidłowym wykorzystaniem lub po prostu jako mechanizmu ułatwiającego debugowanie.

Aby zachować informacje o funkcji dekorowanej, możemy użyć dekoratora <code>functools.wraps()</code>:

    import functools

    def dekoruj(funkcja):
      @functools.wraps(funkcja)
      def funkcja_wew():
        print('przetwarzam dane')
        funkcja()
      return funkcja_wew

Dzięki temu wszystkie informacje o funkcji <code>foo</code>, takie jak jej nazwa czy dokumentacja, zostaną zachowane po dekoracji.

Możemy też przekazywać argumenty do dekoratora i funkcji dekorowanej:

    def dekoruj(funkcja):
      def funkcja_wew(*args, **kwargs):
