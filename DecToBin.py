liczba = 100
lst = []
while liczba > 0:
    if liczba%2 == 0:
        lst.append(0)
        liczba = int(liczba/2)
    else:
        lst.append(1)
        liczba = int((liczba-1)/2)
print(''.join(list(reversed(list(map(str,lst))))))
liczba = '11100011111'
x = list(reversed([liczba[i] for i in range(len(liczba))]))
lst = [((2**i)*int(x[i])) for i in range(len(x))]
print(sum(lst))