rzymskie = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
liczba = 2880
while liczba > 0:
    print(rzymskie[max(rzymskie, key=lambda x: x<=liczba)])
    liczba -= max(rzymskie, key=lambda x: x<=liczba)

