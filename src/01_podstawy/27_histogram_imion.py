# histogram napisow
# Przykład: a, b, a -> a: 2, b: 1


def histogram_imion(lista_imion):
    histogram = {}
    for imie in lista_imion:
        if imie in histogram:
            histogram[imie] += 1
        else:
            histogram[imie] = 1

    return histogram


def wyswietl_histogram(histogram):
    for imie, liczba in histogram.items():
        print(f"{imie}: {liczba}")


if __name__ == "__main__":
    imiona = ["Ala", "Ola", "Ela", "Ala", "Ola", "Ela", "Ala", "Ola", "Ela"]
    histogram = histogram_imion(imiona)
    wyswietl_histogram(histogram)
