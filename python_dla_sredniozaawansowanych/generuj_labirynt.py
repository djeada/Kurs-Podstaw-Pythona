from typing import List, Tuple
import random
import enum

class AlgorytmGeneracji(enum.Enum):
    DFS = enum.auto()
    PRIM = enum.auto()

class GeneratorLabiryntu:
    '''
    Klasa służy do generacji labiryntu ASCII o podanych wymiarach.
    Ściany są oznaczone znakiem '#', a wolne miejsca ' '.
    '''

    def __init__(self, szerokosc, wysokosc, algorytm: AlgorytmGeneracji = AlgorytmGeneracji.DFS):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.labirynt: List[List[str]] = [['#'] * szerokosc for _ in range(wysokosc)]
        self.poczatek: Tuple[int, int] = (1, 1)
        self.koniec: Tuple[int, int] = (szerokosc - 2, wysokosc - 2)
        if algorytm == AlgorytmGeneracji.DFS:
            self._dfs()
        elif algorytm == AlgorytmGeneracji.PRIM:
            self._prim()

    def _dfs(self):
        '''
        Ten algorytm znany jest jako rekurencyjny backtracking. Podstawą jest 
        DFS, ale w każdej iteracji tasujemy listę sąsiadów.
        '''

        stos: List[Tuple[int, int]] = [self.poczatek]
        while stos:
            aktualna_komorka: Tuple[int, int] = stos.pop()
            self.labirynt[aktualna_komorka[1]][aktualna_komorka[0]] = ' '
            if aktualna_komorka == self.koniec:
                break
            sasiedzi: List[Tuple[int, int]] = self._get_sasiedzi(aktualna_komorka)
            for sasiad in sasiedzi:
                if self.labirynt[sasiad[1]][sasiad[0]] == '#':
                    stos.append(sasiad)

        self.labirynt[self.poczatek[1]][self.poczatek[0]] = ' '

    def _prim(self):
        '''
        Analogicznie do DFS, ale tym razem opieramy się o algorytm Prima.
        Sortujemy listę sąsiadów wg. odległości od początku. Wybieramy
        sąsiada z najmniejszą odległością. Odległości mnożymy przez
        losową liczbę z przedziału [1, 10].
        '''
        sterta: List[Tuple[int, int]] = [(0, self.poczatek)]
        while sterta:
            aktualna_odl, aktualna_komorka = sterta.pop()
            self.labirynt[aktualna_komorka[1]][aktualna_komorka[0]] = ' '
            if aktualna_komorka == self.koniec:
                break
            sasiedzi: List[Tuple[int, int]] = self._get_sasiedzi(aktualna_komorka)
            for sasiad in sasiedzi:
                if self.labirynt[sasiad[1]][sasiad[0]] == '#':
                    odleglosc = 1 if sasiad[0] == aktualna_komorka[0] or sasiad[1] == aktualna_komorka[1] else 1.2
                    odleglosc *= random.random()*10
                    sterta.append((aktualna_odl + odleglosc, sasiad))
                    sterta.sort(key=lambda x: x[0])

    def _get_sasiedzi(self, aktualna_komorka: Tuple[int, int]) -> List[Tuple[int, int]]:
        '''
        Znajdz sasiadow danej komorki. Zwroc liste wspolrzednych sasiadow.
        '''
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

generator = GeneratorLabiryntu(30, 30)
