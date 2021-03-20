# wycinanie i podciagi
napis = "James lubi jezdzic na rowerze"
print(napis)
print(napis[1])
print(napis[0:5])
print(napis[8:12])
print(napis[10:150])

# laczenie napisow
imie = "Adam"
imie2 = "James"
imie3 = imie + " " + imie2
print(imie3)
print(imie2 + " " + imie)
print(imie3 + "cos")

# za pomoca slowa kluczowego in mozemy sprawdzic czy dany znak znajduje w naszym napisie
print("n" in imie)
print("a" in imie)
print("dam" in imie)

if "James" in napis:
    print("znaleziony")
else:
    print("nie znaleziony")

# find() znajduje pierwsze wystapienie znaku badz ciagu znakow w napisie
print(napis.find("l"))

# przyklad zamien napis na lubie tunczyka
napis = "Bardze nie lubie tunczyka"
pocz = int(napis.find("n"))
kon = int(napis.find("e", pocz, len(napis)))
print(napis)
napis = napis[0:pocz] + napis[kon + 2 : len(napis)]
print(napis)
