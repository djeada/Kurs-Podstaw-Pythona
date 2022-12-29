"""
Otrzymujesz tekst.

1. Znajdz wszystkie wiersze zaczynajace sie od cyfry.
2. Podmien wszystkie slowa konczace sie wielka litera na '***'.
"""

import re


def wiersze_z_cyfra(tekst):
    return re.findall("^\d.*", tekst, re.MULTILINE)


def podmien_slowa(tekst):
    return re.sub("\w+[A-Z]", "***", tekst)


if __name__ == "__main__":
    tekst = """
Za czasow krola Artura, w AnglII panowala epoka rycerstwa. 
W kraju tym istniala elita wojownikow, ktorzy nosili zbroje i sluzyli krolowi w imieniu chwaly i honoru. 
Najslynniejszym z nich byl sir Lancelot, najodwazniejszy i najszlachetniejszy rycerz w calym krolestwie.

Sir Lancelot byl zawsze gotow stanac w obronie slabszych i walczyc z potworami, ktore nekaly krolestwo. 
Jego miecz byl niezwyciezony, a on sam nie znal strachu. 
Wielu szlachetnych rycerzy chcialo zostac jego uczniem, aby nauczyc sie jego tajnikow walki.

Pewnego dnia krol Artur oglosil turniej rycerskI, na ktorym mieli walczyc najlepsi rycerze Anglii. 
6. Sir Lancelot byl oczywiscie jednym z uczestnikow i szybko stal sie faworytEM do zwyciestwa. 
Walczyl dzielnie i odwaznie, a kiedy turniej dobiegl konca, zostal ogloszony zwyciezca. 
Wszyscy rycerze oklaskiwali go i chwalili za jego umiejetnosci, a krol Artur wreczyl mu nagrode 
- srebrna tarcze i klejnoty wartosci tysiaca groszy.

Sir Lancelot byl dumny z tego zaszczytu i zawsze pamietal o swoich obowiazkach wobec krolestwa. 
7. Dzieki jego odwadze i szlachetnosCI, Anglia byla bezpiecznym i spokojnym krajem, w ktorym kazdy mogl zyc w pokoju i dostatku.
"""

    wiersze = wiersze_z_cyfra(tekst)
    print("Wiersze zaczynajace sie od cyfry:")
    for wiersz in wiersze:
        print(wiersz)

    print("\nTekst po podmianie slow konczacych sie wielka litera:")
    print(podmien_slowa(tekst))
