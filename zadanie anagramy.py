with open('dane.txt', 'r') as f: txt = [x.rstrip() for x in f]
# def spr(lista):
#     lista.append([])
#     for i in range(len(lista)-1):
#         if lista[i] != lista[i+1]:
#             print(lista[i])
wynik = []
for i in txt:
    lst = []
    for slowo in txt:
        if sorted(slowo) == sorted(i):
            lst.append(slowo)
    if len(lst) >= 2:
       wynik.append(lst)
#spr(wynik)
wynik.append([])
for i in range(len(wynik)-1):
    if wynik[i] != wynik[i+1]:
        print(wynik[i])


