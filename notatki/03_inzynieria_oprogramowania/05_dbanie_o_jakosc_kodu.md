
### Dbanie o jakość kodu i lintowanie

Poprawny z punktu widzenia interpretera kod można napisać na wiele sposobów. Nawet jedna linia kodu może być zapisana na wiele sposobów. Jedną z przyczyn takiego stanu rzeczy są różnice w formatowaniu. Na przykład w kodzie do oddzielania instrukcji można użyć zarówno spacji, jak i tabów. Definicje funkcji można oddzielać jednym, dwoma lub trzema enterami. Linie kodu mogą być tak długie, że nie zmieszczą się na ekranie. Czy więc należy ograniczać ich długość? Jeśli tak, to ile znaków powinno być górną granicą? Dopóki z kodem pracujemy sami, wszystko wydaje się być w porządku, ale co jeśli ktoś inny będzie musiał czytać nasz kod? Co jeśli ktoś inny będzie musiał go modyfikować? Wtedy ważne staje się, by kod był czytelny i zrozumiały dla innych programistów. Z tych właśnie względów warto przestrzegać konwencji pisania kodu.

Narzędzia, takie jak <code>Pylint</code> i <code>Black</code> pomagają nam uniknąć typowych błędów i niepoprawności, które mogą pojawić się podczas pisania kodu. Narzędzia te sprawdzają, czy kod jest zgodny z zasadami zapisanymi w dokumentach <code>PEP8</code> i <code>PEP257</code>.

Aby użyć narzędzia <code>Pylint</code>, zainstaluj je za pomocą <code>PIP</code>:

    pip install pylint

Aby sprawdzić kod za pomocą <code>Pylint</code>, użyj polecenia:

    pylint <nazwa_pliku.py>

Aby użyć narzędzia <code>Black</code>, zainstaluj je za pomocą <code>PIP</code>:

    pip install black

Aby użyć <code>Black</code> do sformatowania kodu w pliku o nazwie <code>nazwa_pliku.py</code>, użyj polecenia:

    black nazwa_pliku.py

Black to narzędzie do automatycznej reformatowania kodu w celu dostosowania go do wytycznych PEP8. Nie pyta ono o zdanie programisty i zmienia formatowanie kodu bez możliwości konsultacji. Z tego względu Black jest narzędziem bardzo szybkim i prostym w użyciu. Jego główną wadą jest brak możliwości konfiguracji. Black nie pozwala na zmianę domyślnych ustawień ani na wyłączenie poszczególnych zasad formatowania.

Flake8 to narzędzie do sprawdzania jakości kodu. Oprócz formatowania kodu, Flake8 sprawdza także jego poprawność semantyczną oraz brak błędów składniowych. W porównaniu do Blacka, Flake8 oferuje większą ilość opcji konfiguracyjnych. Możliwe jest m.in. wyłączenie poszczególnych zasad sprawdzania lub zmiana ich domyślnych ustawień. Jedną z wad Flake8 jest to, że jest ono wolniejsze od Blacka, ponieważ sprawdza także inne aspekty kodu niż tylko jego formatowanie.

Pylint to narzędzie do sprawdzania jakości kodu podobne do Flake8. Oprócz sprawdzania formatowania kodu i braku błędów składniowych, Pylint sprawdza także nazewnictwo zmiennych i funkcji oraz brak docstringów (komentarzy opisujących kod).

|                            | black | pylint | flake8 | 
|----------------------------|--------|--------|-------|
| automatyczna korekcja            |   ✔️   |   ❌   |   ❌  | 
| wskazówki do stylu     |   👷‍♂️   |   ✔️   |   👷‍♂️  |
| wyszukiwanie bugów             |   ❌   |   ✔️   |   👷‍♂️  | 
| wskazywanie zbyt złożonego kodu      |   ❌   |   👷‍♂️   |   ❌  |
| dostępność pluginów    |   ❌   |   ❌   |   ✔️  | 

Linki:

* https://www.python.org/dev/peps/pep-0008/
* https://www.python.org/dev/peps/pep-0257/
* https://github.com/psf/black
* https://github.com/PyCQA/pylint
* https://github.com/PyCQA/flake8
* https://github.com/myint/autoflake