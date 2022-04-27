import dataclasses

def dataclass_ze_slownika(typ_klasy, slownik):
  try:
    typy_pol = {pole.name : pole.type for pole in dataclasses.fileds(typ_klasy)}
    return typ_klasy(**{klucz: dataclass_ze_slownika(typy_pol[klucz], slownik[klucz]) for klucz in slownik})
  except:
    return slownik
