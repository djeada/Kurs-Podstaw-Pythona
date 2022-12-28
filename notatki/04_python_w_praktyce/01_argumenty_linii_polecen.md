### Argumenty linii poleceń

Python obsługuje argumenty linii poleceń. Jeśli chcemy, by nasz skrypt był sterowany przez argumenty przekazywane podczas jego uruchomienia, mamy do dyspozycji kilka narzędzi, które ułatwią nam to zadanie.

Moduł biblioteki standardowej sys zawiera zmienną argv, która przechowuje nazwę programu oraz listę argumentów przekazanych z linii poleceń. Zakłada się, że argumenty są oddzielone spacjami.

Przykładowo, jeśli mamy skrypt o nazwie suma.py i chcemy, by po jego uruchomieniu skrypt wypisał sumę argumentów przekazanych z linii poleceń, możemy to zrobić w następujący sposób:

    import sys
    print(sum(sys.argv[1:]))
    
Dla następującej kombinacji liczb powinniśmy otrzymać następujący wynik:

    $ python suma.py 3 2 1
    6

Jeśli chcielibyśmy używać flag do nazywania dostępnych opcji, możemy nadal użyć sys.argv, ale będziemy musieli napisać parser do obsługi wszystkich możliwych kombinacji flag. Łatwiej skorzystać z gotowego narzędzia. Również w bibliotece standardowej mamy moduł *argparse*. Moduł ten daje nam opcję zdefiniowania możliwych do użycia argumentów.

Załóżmy, że chcemy by nasz skrypt przyjmował nazwę pliku jako argument, a następnie dopisywał na końcu pliku wiersz "nowy wiersz". Możemy to zrobić w następujący sposób:

    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser()
    parser.add_argument("plik", help="sciezka do pliku ktory chcesz zmodyfikowac")
    args = parser.parse_args()

    plik = Path(args.plik)
    nowy_wiersz = "nowy wiersz"
    plik.write_text(plik.read_text() + nowy_wiersz)

Jeśli teraz uruchomimy plik bez argumentu, to zostanie wyświetlony komunikat o błędzie:

    $ python3 script.py 
    usage: script.py [-h] plik
    script.py: error: the following arguments are required: plik

Mamy możliwość wyświetlenia pomocy dla naszego skryptu. Moduł *argparse* generuje pomoc automatycznie na podstawie argumentów, jakie ustawiliśmy.

    $ python3 script.py -h
    usage: script.py [-h] plik

    positional arguments:
      plik        sciezka do pliku ktory chcesz zmodyfikowac

    options:
      -h, --help  show this help message and exit

Jeśli chcemy by argument był opcjonalny to przy dodawaniu go musimy ustawić pole *required* na *False*.

    parser.add_argument("--argument", help="Opcjonalny argument", required=False)

Inne opcje to połączenie argumentu z flagą, nadanie wartości domyślnej oraz ustawienie oczekiwanego typu:

    parser.add_argument("-a", "--argument", help="Argument z wartością domyślną", type=int, default=10, required=False)