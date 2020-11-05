def usun(x):
    lista = []
    for i in x:
        if i not in lista: lista.append(i)
    return lista

lista = [1,1,2,5,5,8,9,9,9,9]
print(usun(lista))