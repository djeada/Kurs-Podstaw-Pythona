import shutil
from pathlib import Path
import unittest


class PrzykladTestu(unittest.TestCase):
    def setUp(self):
        # utworz tymczasowy folder
        self.folder_testowy = Path("temp_dir")
        self.folder_testowy.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        # usun folder testowy z cala zawartoscia
        shutil.rmtree(self.folder_testowy)

    def przykladowy_test(self):
        plik = Path("plik.txt")
        plik.touch()
        tresc = "Lezy Jerzy na wiezy.\n"
        plik.write_text(tresc)
        # sprawdz czy wczytana tresc z pliku pokrywa sie z oryginalna trescia
        self.assertEqual(plik.read_text(), tresc)


if __name__ == "__main__":
    unittest.main()
