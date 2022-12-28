
### Debugowanie

Debuger jest bardzo przydatnym narzędziem, zwłaszcza przy pracy nad dużymi projektami. Dzięki niemu możemy zatrzymać program w dowolnym momencie, aby sprawdzić co się w nim dzieje. Możemy też prześledzić kolejne kroki programu, które zostały wykonane do momentu zatrzymania, co pozwala na szybkie i skuteczne znajdowanie błędów.

Dwa główne zastosowania debugera:
- Wyszukiwanie przyczyn bugów w kodzie.
- Analiza działania programu przez zaznajamiających się z nim programistów.

Jedną z mocnych stron debugera jest też to, że pozwala nam zajrzeć "pod maskę" programu i zobaczyć jakie zmienne są zdefiniowane i jakie są ich wartości. Dzięki temu możemy szybciej zrozumieć co dzieje się w kodzie i co jest przyczyną jakichś błędów.

Słabą stroną debugera jest to, że korzystanie z niego może być czasochłonne. Zatrzymywanie programu i przechodzenie przez kolejne kroki wymaga czasu i cierpliwości. Czasem może też być trudno zrozumieć co dzieje się w kodzie, jeśli jest on bardzo skomplikowany lub niezrozumiały.

Większość współczesnych środowisk programistycznych (IDE) ma wbudowany debuger. Debugger w IDE umożliwia ustawienie punktów breakpoint, dzięki którym program zatrzymuje się automatycznie w wybranym miejscu, co ułatwia debugowanie. IDE zazwyczaj posiada również dodatkowe funkcje, takie jak możliwość podglądu zmiennych czy historii wywołań funkcji, które ułatwiają debugowanie.

Jeśli nie korzystamy z IDE, możemy użyć modułu pdb, który jest wbudowanym w Pythonie debugerem. Moduł ten umożliwia kontrolowanie wykonywania kodu z linii poleceń, co pozwala na debugowanie skryptów bez konieczności ich uruchamiania w środowisku programistycznym. Możliwe jest również uruchamianie pdb z poziomu kodu Pythona za pomocą funkcji importowanej z modułu <code>pdb</code>: <code>pdb.set_trace()</code>. Po uruchomieniu tej funkcji program zatrzyma się i będziemy mogli kontrolować jego działanie z linii poleceń.

Linki:

* https://docs.python.org/3/library/pdb.html