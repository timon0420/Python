nr = 12345
login = 'xyz'
class Bankomat():
    def __init__(self, stankonta = 1000):
        self.stankonta = stankonta
    def wpłata(self, wpłata):
        self.stankonta += wpłata
        print('Po wpłacie masz na koncie: {}'.format(self.stankonta))
    def wypłata(self, wypłata):
        if wypłata <= self.stankonta:
            self.stankonta -= wypłata
            print('Po wypłacie na koncie pozostało: {}'.format(self.stankonta))
        elif wypłata >= self.stankonta:
            print('Nie możesz tyle wypłacić. Masz na koncie: {}'.format(self.stankonta))
    def waluty(self):
        print('W funtach brytyjskich stan twojego konta to: {}'.format(round((self.stankonta/5.6), 2)))
        print('W dolarach amerykańskich stan twojego konta to: {}'.format(round((self.stankonta/4.3), 2)))
        print('W euro stan twojego konta to: {}'.format(round((self.stankonta/4.7), 2)))
bankomat = Bankomat()
print("Obecnie masz na koncie: {}".format(bankomat.stankonta))
bankomat.waluty()
# if wybory == 1: bankomat.wpłata(int(input('Podaj ile chcesz wpłacić: '))), bankomat.waluty()
# elif wybory == 2: bankomat.wypłata(int(input('Podaj ile chcesz wypłacić: '))), bankomat.waluty()
i = 3
while i > 0:
    if login == input('Podaj login: '):
        if nr == int(input('Podaj nr: ')):
            wybory = int(input('1. wpłata, 2. wypłata: '))
            if wybory == 1: bankomat.wpłata(int(input('Podaj ile chcesz wpłacić: '))), bankomat.waluty()
            elif wybory == 2: bankomat.wypłata(int(input('Podaj ile chcesz wypłacić: '))), bankomat.waluty()
            break
    i -= 1
