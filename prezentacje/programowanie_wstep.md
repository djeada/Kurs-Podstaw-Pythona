## Czym jest program?

    kod => hardware => wyjscie
              ||
           wejscie

## Kompilator i impretator

Komputer rozumie kod binarny.

    kod => interpretajca/komiplacja => inny kod
    
Przykład: kod w języku programowania jak Java, C# na kod maszynowy.

Kompilator nie musi tłumaczyć bezpośrednio na kod maszynowy. Może mieć języki pośrednie.

F#.NET -> komiplator F#.NET -> CIL (.exe/.dll) -> komilator JIT (just-in-time) -> kod maszynowy
C#.NET -> komiplator C#.NET -> CIL (.exe/.dll) -> komilator JIT (just-in-time) -> kod maszynowy

Kompilator wyrzuca program wykonywalne.

Interpreter nie tylko tłumaczy, ale od razu wykonuje. Wiersz po wierszu.

## Syntaktyka (reguly) i semantyka (znaczenie)

Nazywam się Adam. -> Syntaktyka ok, semantyka ok

Nazywam się James. -> Syntaktyka ok, semantyka nie.

Semantyka czy program robi to chcemy żeby robił.

## Typowanie

* Typowanie statyczne – nadawanie typów zmiennym w czasie kompilacji programu
* Typowanie dynamiczne to przypisywanie typów do wartości przechowywanych w zmiennych w trakcie działania programu
