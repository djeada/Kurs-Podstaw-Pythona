from typing import List, Tuple
import random
import enum


class AlgorytmGeneracji(enum.Enum):
    DFS = enum.auto()
    PRIM = enum.auto()


class GeneratorLabiryntu:
    """
    Klasa sluzy do generacji labiryntu ASCII o podanych wymiarach.
    Sciany sa oznaczone znakiem '#', a wolne miejsca ' '.
    """

    def __init__(
        self, szerokosc, wysokosc, algorytm: AlgorytmGeneracji = AlgorytmGeneracji.DFS
    ):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.labirynt: List[List[str]] = [["#"] * szerokosc for _ in range(wysokosc)]
        self.poczatek: Tuple[int, int] = (1, 1)
        self.koniec: Tuple[int, int] = (szerokosc - 2, wysokosc - 2)
        if algorytm == AlgorytmGeneracji.DFS:
            self._dfs()
        elif algorytm == AlgorytmGeneracji.PRIM:
            self._prim()

    def _dfs(self):
        """
        Ten algorytm znany jest jako rekurencyjny backtracking. Podstawa jest
        DFS, ale w kazdej iteracji tasujemy liste sasiadow.
        """

        def dfs(komorka: Tuple[int, int]):
            self.labirynt[komorka[1]][komorka[0]] = " "
            if komorka == self.koniec:
                return True
            sasiedzi: List[Tuple[int, int]] = self._znajdz_sasiadow(komorka)
            random.shuffle(sasiedzi)
            for sasiad in sasiedzi:
                if self.labirynt[sasiad[1]][sasiad[0]] == "#":
                    if dfs(sasiad):
                        return True
            return False

        dfs(self.poczatek)

    def _prim(self):
        """
        Analogicznie do DFS, ale tym razem opieramy sie o algorytm Prima.
        Sortujemy liste sasiadow wg. odleglosci od poczatku. Wybieramy
        sasiada z najmniejsza odlegloscia. Odleglosci mnozymy przez
        losowa liczbe z przedzialu [1, 10].
        """

        def prim(komorka: Tuple[int, int]):
            self.labirynt[komorka[1]][komorka[0]] = " "
            if komorka == self.koniec:
                return True
            sasiedzi: List[Tuple[int, int]] = self._znajdz_sasiadow(komorka)
            sasiedzi.sort(key=lambda s: self._odleglosc(s, self.poczatek))
            for sasiad in sasiedzi:
                if self.labirynt[sasiad[1]][sasiad[0]] == "#":
                    if prim(sasiad):
                        return True
            return False

        prim(self.poczatek)

    def _odleglosc(self, a: Tuple[int, int], b: Tuple[int, int]) -> float:
        """
        Zwroc odleglosc miedzy dwoma punktami.
        """
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) * random.randint(1, 10)

    def _znajdz_sasiadow(
        self, aktualna_komorka: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        """
        Znajdz sasiadow danej komorki. Zwroc liste wspolrzednych sasiadow.
        """
        sasiedzi: List[Tuple[int, int]] = []
        x, y = aktualna_komorka
        if x > 1:
            sasiedzi.append((x - 1, y))
        if x < self.szerokosc - 2:
            sasiedzi.append((x + 1, y))
        if y > 1:
            sasiedzi.append((x, y - 1))
        if y < self.wysokosc - 2:
            sasiedzi.append((x, y + 1))
        return sasiedzi


if __name__ == "__main__":
    generator = GeneratorLabiryntu(40, 30, AlgorytmGeneracji.DFS)
    for wiersz in generator.labirynt:
        print("".join(wiersz))
