import re

'''
. dowolny znak
Przyklad: '.ala' Pasuja: fala, gala, mala, nala

[] znaki wymienione miedzy nawiasami
Przyklad: '[dm]am' Pasuja: mam, dam Niepasuja: sam, ram

[^ ] znaki nie wymienione miedzy nawiasami
Przyklad: '[^dm]am' Pasuja: sam, ram, gam, tam Niepasuja: dam, mam

* wszelkie mozliwe kombinacje znakow
Przyklad: 'k.*' Pasuja: kot, kocur, kalafior, katafrakci

'''

napis = 'James lubi jesc tunczyki jako jedzenie'

wyrazenie = re.compile('j[^ ]*')

#wzorzec i tekst musza byc takie same 
if re.match('.*lubi.*', napis):
    print('znaleziono za pomoca match')

#wzorzec wystepuje w tekscie
if re.search('[kwefjsb]u.i', napis):
    print('znaleziono za pomoca search')

#znajdujemy wszystkie wystapienia wyrazenia w tekscie
for i in re.findall(wyrazenie,napis):
    print(i)





