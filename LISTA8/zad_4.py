try:
    file = open('PESEL.txt', 'r')
except:
    print('Błąd otwarcia pliku!')
else:
    pesele = []
    linie = file.readlines()
    tabela = [1,3,7,9,1,3,7,9,1,3,1]
    for i in linie:
        i = i.strip()
        suma = 0
        for j in range(11): suma += int(i[j]) * tabela[j]
        if suma % 10 == 0:
            if int(i[2:4]) > 20:
                rok = '20'+i[0:2]
                miesiac = str(int(i[2:4])-20)
                if len(miesiac)<2: miesiac = '0'+ miesiac
                dzien = i[4:6]
                if int(i[9]) % 2 == 0:
                    plec = 'kobieta'
                else: plec = 'mężczyzna'
            else:
                rok = '19' + i[0:2]
                miesiac = i[2:4]
                dzien = i[4:6]
                if int(i[9]) % 2 == 0:
                    plec = 'kobieta'
                else:
                    plec = 'mężczyzna'
            pesele.append(i+' : data urodzenia '+dzien+'.'+miesiac+'.'+rok+'; płeć '+ plec + ';\n')
        else:
            print('Niepoprawny pesel!')
finally:
    file.close()

try:
    file = open('PESELE_dane.txt', 'w', encoding='utf-8')
except:
    print('Błąd zapisu pliku!')
else:
    file.writelines(pesele)
finally:
    file.close()