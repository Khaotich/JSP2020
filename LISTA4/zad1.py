def suma(x):
    return sum(x)

def iloczyn(z):
    x = 1
    for i in z: x *= i
    return x

lista = [2,5,8,7,4,1,3,6,9,4,85,21,25]
print("Proszę wybrać opcje: ")
print('1. Suma listy')
print('2. Iloczyn listy')

n = int(input('Opcja: '))

if n==1:
    print('Suma listy wynosi: ', suma(lista))
elif n==2:
    print('Iloczyn listy wynosi: ', iloczyn(lista))
else:
    print('Wybrano nie poprawną opcję')