imiona = open('imiona.txt', 'r').read().strip('\n')
lista = imiona.split('\n')
k = list(filter(lambda x: x.endswith('a'), lista)) 
k_sort = reversed(sorted(dict(zip(k, [len(y) for y in k])).items(), key=lambda z: z[1]))
m = list(filter(lambda x: x.endswith('a') == False, lista))
m_sort = reversed(sorted(dict(zip(m, [len(y) for y in m])).items(), key=lambda z: z[1]))
woman = open('dziewczynki.txt', 'w')
man = open('chlopcy.txt', 'w')
for i in k_sort:
    woman.write(str(list(i)))
    woman.write('\n')
for i in m_sort:
    man.write(str(list(i)))
    man.write('\n')
