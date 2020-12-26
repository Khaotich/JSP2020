import xml.etree.ElementTree as et

class waluty:
    def __init__(self, path):
        self.path = path

    def lista_walut(self):
        try:
            xml = et.parse(self.path).getroot()
            texts = []
            for i in xml.findall('pozycja/nazwa_waluty'):
                texts.append(i.text)
            return texts
        except:
            return 'Błąd otwarcia pliku'

    def wartosc(self, value):
        xml = et.parse(self.path).getroot()
        for v in xml.findall('pozycja'):
            for n in v.findall('nazwa_waluty'):
                if n.text == value:
                    for c in v.findall('kurs_sredni'):
                        return c.text

    def convertPLN(self):
        ar = self.lista_walut()
        money = float(input('Podaj kwotę do konwertowania: '))
        nameOfCurrency = input('Podaj nazwę waluty do konwertowania: ')

        if nameOfCurrency in ar and type(ar) == list:
            value = float(self.wartosc(nameOfCurrency))

            while True:
                choice = input('Jeśli chcesz konwertować na PLN wpisz 1, a jeśli z PLN wpisz 2: ')

                if choice == '1':
                    return round(money * value, 2)
                elif choice == '2':
                    return round(money / value, 2)
                else:
                    print('Wybrano złą opcję!')
        else:
            return "Podano złą walutę!"

    def convert(self):
        ar = self.lista_walut()
        money = float(input('Podaj kwotę do konwertowania: '))
        first = input('Podaj nazwę waluty, którą posiadasz: ')

        if first in ar and type(ar) == list:
            second = input('Podaj nazwę waluty, którą chcesz: ')

            if second in ar and type(ar) == list:
                money *= float(self.wartosc(first))
                money /= float(self.wartosc(second))
                return round(money, 2)
            else:
                return "Podano złą walutę!"
        else:
            return "Podano złą walutę!"

    def menu(self):
        while True:
            print('Dostępne opcje:')
            print('0. Zakończ')
            print('1. Lista dostępnych kursów')
            print('2. Konwersja dowolnej waluty na PLN')
            print('3. Konwersja wybranej waluty na wybraną walute')
            choice = input('Wybierz opcje: ')
            print()

            if choice == '0':
                break
            elif choice == '1':
                namesOfCurrency = self.lista_walut()
                if type(namesOfCurrency) == list:
                    print('Lista dostępnych kursów:')
                    for element in namesOfCurrency:
                        print(element)
                else:
                    print(namesOfCurrency)
            elif choice == '2':
                print(self.convertPLN())
            elif choice == '3':
                print(self.convert())
            else:
                print('Nie ma takiej opcji!')

exchangeRates = waluty('kursy.xml')
exchangeRates.menu()