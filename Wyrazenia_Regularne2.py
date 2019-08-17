import re

#+48-999-999-999

#\d to jest dowolna cyfra
#\D to jest dowolny znak nie bedacy cyfra

wzorNumeru = re.compile(r'[+]\d{2,3}-\d{3}-\d{3}-\d{3}')

znaleziono = wzorNumeru.search('To jest moj numer telefonu +48-999-999-999')
znaleziono2 = wzorNumeru.search('To jest moj numer telefonu +32-919-943-009')
znaleziono3 = wzorNumeru.search('To jest moj numer telefonu +352-939-559-999')

print(znaleziono.group())
print(znaleziono2.group())
print(znaleziono3.group())

numerWzor = re.compile(r'([+]\d\d)-(\d\d\d-\d\d\d-\d\d\d)')
znajdz = numerWzor.search(sentence)
print(znajdz.group(1))
print(znajdz.group(2))


#moze nie musi byc 
numerWzor = re.compile(r'([+]\d\d)?-\d\d\d-\d\d\d-\d\d\d')
