import szyfr_cezara
import datetime as t
import os

path_file_to_decrypt = ""
path_file_to_save = ""

while not os.path.exists(path_file_to_decrypt):
    path_file_to_decrypt = input("Proszę podać ścieżkę do folderu z zaszyfrowanymi plikami: ")

files = os.listdir(path_file_to_decrypt)
files_to_decrypt = []

for i in files:
    if i[0:17] == 'plik_zaszyfrowany': files_to_decrypt.append(i)

texts = []
keys = []

for i in files_to_decrypt:
    try:
        file = open(path_file_to_decrypt + '/' + i,'r',encoding="utf-8")
    except:
        print("Błąd otwarcia pliku!")
    else:
        key = int(i[18:i.index("_",18)])
        keys.append(key)
        text = ''
        for j in file.readlines():
            text += szyfr_cezara.deszyfr(j,key)
        texts.append(text)
    finally:
        file.close()

for i in texts: print(i)
print(len(texts))

while not os.path.exists(path_file_to_save):
    path_file_to_save = input("Proszę podać ścieżkę do zapisania odszyfrowanych plików: ")

for i in range(len(keys)):
    name = 'plik_deszyfrowany_' + str(keys[i]) + "_" + str(t.datetime.now().year) \
           + str(t.datetime.now().month) + str(t.datetime.now().day)

    if os.path.exists(path_file_to_save + '/' + name + '.txt'):
        if os.path.exists(path_file_to_save + '/' + name + '_1.txt'):
            pliki = os.listdir(path_file_to_save)
            z = 1
            for j in pliki:
                if name + '_' + str(z) + '.txt' in pliki:
                    z += 1
            name = name + '_' + str(z)
        else:
            name = name + '_1'

    name = path_file_to_save + '/' + name + '.txt'

    try:
        file1 = open(name,'w',encoding="utf-8")
    except:
        print("Błąd zapisu pliku!")
    else:
        file1.write(texts[i])
        print('Plik', i+1, 'zapisano!')
    finally:
        file1.close()
