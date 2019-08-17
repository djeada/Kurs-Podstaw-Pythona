import re

sentence = 'Moj numer telefonu to +48-999-999-999'

numerWzor = re.compile(r'[+]\d\d-\d\d\d-\d\d\d-\d\d\d')

znajdz = numerWzor.search(sentence)

#co zostalo znalzione

print(znajdz)
print(znajdz.group())


numerWzor = re.compile(r'([+]\d\d)-(\d\d\d-\d\d\d-\d\d\d)')
znajdz = numerWzor.search(sentence)
print(znajdz.group(1))
print(znajdz.group(2))


#moze nie musi byc 
numerWzor = re.compile(r'([+]\d\d)?-\d\d\d-\d\d\d-\d\d\d')


