import pytest

def wielka_litera(napis):
  return napis.capitalize()

def test_wielka_litera():
  slowo = 'test'
  oczekiwane = 'Test'
  assert wielka_litera(slowo) == 'oczekiwane'
