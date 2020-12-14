import szyfr_cezara
import datetime as t
import os

def pozycje(tekst,znak):
    indexy = []
    for i in range(len(tekst)):
        if tekst[i] == znak:
            indexy.append(i)
    return indexy

path_file_to_crypt = ""
path_file_to_save = ""

while not os.path.exists(path_file_to_crypt):
    path_file_to_crypt = input("Proszę podać ścieżkę do szyfrowanego pliku wraz z jego rozszerzeniem: ")

try:
    file = open(path_file_to_crypt,'r',encoding="utf-8")
except:
    print("Błąd otwarcia pliku!")
else:
    key = -1
    while  not(key > 0 and key < 11):
        key = int(input('Proszę podać klucz szyfrowania z przedziału (1-10): '))
    text = ''
    for i in file.readlines():
        text += szyfr_cezara.szyfruj((i),key)
finally:
    file.close()

while not os.path.exists(path_file_to_save):
    path_file_to_save = input("Proszę podać ścieżkę do zapisania zaszyfrowanego pliku: ")

####
name = 'plik_zaszyfrowany_'+str(key)+"_"+str(t.datetime.now().year)\
       +str(t.datetime.now().month)+str(t.datetime.now().day)

if os.path.exists(path_file_to_save+'/'+name+'.txt'):
    if os.path.exists(path_file_to_save+'/'+name+'_1.txt'):
        pliki = os.listdir(path_file_to_save)
        z = 1
        for i in pliki:
            if name+'_'+ str(z) +'.txt' in pliki:
                z += 1
        name = name + '_' + str(z)
    else: name = name + '_1'

name = path_file_to_save + '/' + name + '.txt'

try:
    file1 = open(name,'a',encoding="utf-8")
except:
    print("Błąd otwarcia pliku!")
else:
    file1.write(text)
    print('Plik zapisano w lokalizacji:', name)
finally:
    file1.close()