m = int(input('Proszę wprowadzić m: '))
n = int(input('Proszę wprowadzić n: '))
lista = []

for i in range(m):
    temp = []
    for j in range(n):
        temp.append((i+1)*(j+1))
    lista.append(temp)

for i in lista:
    print(i)