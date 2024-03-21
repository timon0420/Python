import pyttsx3 as tts
engine = tts.init()
engine.setProperty('rate', 150)


morse = {"A": ".-", "B": "-...", "C": "-.-", "D": "-..", "E": ".",
         "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
         "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
         "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
         "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
         "Z": "--..", "Ą": ".-.-", "Ć": "-.-..", "Ę": "..-..",
         "Ł": ".-..-", "Ń": "--.--", "Ó": "---.", "Ś": "...---...",
         "Ż": "--..-.", "Ź": "--..-", "1": ".----", "2": "..---",
         "3": "...--", "4": "....-", "5": ".....", "6": "-.....",
         "7": "--...", "8": "---..", "9": "----.", "0": "-----"}

def szyfr(x):
    kod = ''
    slowo = x
    for litera in slowo:
        for i,m in morse.items():
            if litera.upper() == i:
                kod += m
                kod += ' '
            elif litera == ' ':
                kod += '   '
    print(kod)
    def mowa(kod):
        engine.setProperty('rate', 300)
        engine.say(kod)
        engine.runAndWait()
    for i in kod:
        if i == '-':
            mowa('kreska')
        elif i == '.':
            mowa('kropka')
        elif i == ' ':
            mowa('spacja')


def deszyfr(x):
    kod = x
    slowo = ''
    for x in kod.split(' '):
        for i,m in morse.items():
            if x == m:
                slowo += i
            elif x == ' ':
                slowo += ''
            elif x == '   ':
                slowo += ' '
    print(slowo)
    engine.say(slowo)
    engine.runAndWait()


    
x = input('Podaj słowo lub szyfr: ')
wybory = int(input('1.szyfrowanie, 2.deszyfrowanie: '))
if wybory == 1:
    szyfr(x)
elif wybory == 2:
    deszyfr(x)
