lista = [x for x in range(3,100,3)]

for i in range(5,len(lista),3):
    try:
        del lista[i]
    except:
        break

srednia = sum(lista)/len(lista)
print(srednia)