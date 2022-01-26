import re

# +48-999-999-999

# \d to jest dowolna cyfra
# \D to jest dowolny znak nie badacy cyfra

wzorNumeru = re.compile(r"[+]\d{1,4}-\d{3}-\d{3}-\d{3}")
znaleziono = wzorNumeru.search("Moj numer to +48-999-999-999")
znaleziono2 = wzorNumeru.search("Moj numer to +352-919-459-933")
znaleziono3 = wzorNumeru.search("Moj numer to +7-943-865-000")

print(znaleziono.group())
print(znaleziono2.group())
print(znaleziono3.group())

wzorNumeru = re.compile(r"([+]\d{1,4})-(\d{3}-\d{3}-\d{3})")
znaleziono = wzorNumeru.search("Moj numer to +48-999-999-999")
print(znaleziono.group(1))
print(znaleziono.group(2))


wzorNumeru = re.compile(r"([+]\d{1,4}-)?\d{3}-\d{3}-\d{3}")
znaleziono = wzorNumeru.search("Moj numer to 888-999-999")
znaleziono2 = wzorNumeru.search("Moj numer to +99-999-999-999")

print(znaleziono.group())
print(znaleziono2.group())
