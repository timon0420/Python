import random

# zad 1
miasta = ['Andrychów',
'Augustów',
'Aleksandrów Łódzki',
'Barlinek',
'Białystok',
'Bielsko-Biała',
'Cedynia',
'Chełm',
'Chojna',
'Choszczno',
'Cieszyn',
'Częstochowa',
'Drawsko Pomorskie',
'Darłowo',
'Dąbrowa Górnicza',
'Elbląg',
'Ełk',
'Frombork',
'Gdynia',
'Gdańsk',
'Gorzów Wielkopolski',
'Goleniów',
'Gniezno',
'Hel',
'Inowrocław',
'Ińsko',
'Iława',
'Jarocin',
'Jelenia Góra',
'Jaworzno',
'Kalisz',
'Kołobrzeg',
'Koszalin',
'Lębork',
'Lipiany',
'Lublin',
'Łódź',
'Łobez',
'Malbork',
'Międzyzdroje',
'Myślibórz',
'Nowogard',
'Nysa',
'Nowy Sącz',
'Opole',
'Ostrołęka',
'Olsztyn',
'Piła',
'Police',
'Poznań',
'Rzeszów',
'Radom',
'Rabka',
'Sandomierz',
'Siedlce',
'Szczecin',
'Tarnobrzeg',
'Toruń',
'Turek',
'Ustroń',
'Ustka',
'Ustrzyki Dolne',
'Wadowice',
'Warszawa',
'Wrocław',
'Zielona Góra',
'Złocieniec',
'Złotoryja']
temperatura = [random.randint(-10,6) for x in range(20)]
lista = [random.sample(miasta, 20)]
print(sorted(dict(zip((random.sample(miasta, 20)), [random.randint(-10,6) for x in range(20)])).items(), key=lambda x: x[1]) [::-1] )

# zad 2
lista = sum(set([int(x/2) for x in range(1,100)]))
print(lista)
zmienna = int(input('Podaj liczbę: '))
print([x+1 for x in range(sum(set([int(x/2) for x in range(1,zmienna)]))) if (sum(set([int(x/2) for x in range(1,zmienna)])))%(x+1) == 0] [::-1])

# zad 3
def generator(liczba):
    i = 0
    while i<=liczba:
        yield i 
        i += 1
x = list(filter(lambda x: x%1 == 0, list(generator(int(input('Podaj liczbę: '))))))
cos = [k+1 for i in list(filter(lambda x: x%1 == 0, list(generator(int(input('Podaj liczbę: ')))))) for k in range(i) if i%(k+1) == 0 ]
print(cos)
print('suma: ', sum(cos))
cos1 = [i+1 for i in range(int(sum(cos)/2)) if sum(cos)%(i+1) == 0 ]
print(cos1)