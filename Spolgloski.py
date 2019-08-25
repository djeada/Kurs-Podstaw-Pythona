spolgloski = "aeiou"

def zlicz_spolgoski_iter(napis):
    wynik = 0
    for x in napis:
        if x.isalpha() and x.lower() not in spolgloski:
            wynik += 1
    return wynik

def zlicz_spolgoski_iter(napis):
    if len(napis) == 0:
        return 0
    
    if napis[0].isalpha() and napis[0].lower() not in spolgloski:
        return 1 + zlicz_spolgoski_iter(napis[1:])
    else:
        return zlicz_spolgoski_iter(napis[1:])
