import random as r

pesele = []
for i in range(10):

    rok = str(r.randint(0,99))
    if len(rok) < 2 : rok = '0'+rok

    miesiac = r.randint(1,12)
    if r.randint(0,1) % 2 == 0: miesiac += 20
    if miesiac < 10: miesiac = '0'+str(miesiac)
    else: miesiac = str(miesiac)

    dzien = ''
    if int(miesiac)%2==0 : dzien = r.randint(1,30)
    else: dzien = r.randint(1,31)
    if dzien < 10: dzien = '0'+ str(dzien)
    else: dzien = str(dzien)

    reszta = ''
    for j in range(5): reszta += str(r.randint(0,9))

    pesele.append(rok + miesiac + dzien + reszta + '\n')

try:
    file = open('PESEL.txt','w')
except:
    print('Błąd otwarcia pliku!')
else:
    file.writelines(pesele)
    print('Plik zapisano poprawnie!')
finally:
    file.close()