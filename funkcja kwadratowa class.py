class Funkcja():
    def __init__(self ,a = 1 ,b = 1, c = 1):
        self.a = a
        self.b = b
        self.c = c
        self.delta = 0
        self.x0 = 0
        self.x1 = 0
        self.x2 = 0
    def rozw(self):
        if self.a != 0:
            self.delta = (self.b ** 2) - (4*self.a*self.c)
            if self.delta == 0:
                self.x0 = (self.b*(-1))/(self.a*2)
                return self.x0
            if self.delta > 0:
                self.x1 = ((self.b*(-1))-(self.delta**0.5))/(self.a*2)
                self.x2 = ((self.b*(-1))+(self.delta**0.5))/(self.a*2)
                return 'miejsca zerowe funkcji: ', round(self.x1,2), round(self.x2,2)
            if self.delta < 0:
                return 'Delta jest mniejsza od zera i wynosi {}'.format(self.delta)
        else:
            return 'To nie jest funkcja kwadratowa ponieważ "a" jest równe 0'

func = Funkcja(int(input('Podaj "a": ')), int(input('Podaj "b": ')), int(input('Podaj "c": ')))
print(func.rozw())

func1 = Funkcja(10,4,2)
print(func1.rozw())
