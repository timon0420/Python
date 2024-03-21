txt = open('dane.txt', 'r')
wynik = open('wynik.txt', 'w')
lista1 = []
tekst = []
lista = txt.read()
def szyfrowanie(a):
    for i in range(len(lista)):
        k = ord(lista[i]) + a
        if k > 123:
            lista1.append(k-26)
        else:
            lista1.append(k)
        tekst.append(chr(lista1[i]))
        wynik.write(tekst[i])
def deszyfrowanie(a):
    for i in range(len(lista)):
        k = ord(lista[i]) - a
        if k < 97:
            lista1.append(k+26)
        else:
            lista1.append(k)
        tekst.append(chr(lista1[i]))
        wynik.write(tekst[i])

print('Szyfr Cezara')
print('1.szyfrowanie')
print('2.deszyfrowanie')
wybory = int(input('Co wybierasz: '))
klucz = int(input('Podaj klucz: '))

if wybory == 1:    
    szyfrowanie(klucz)
else:
    deszyfrowanie(klucz)