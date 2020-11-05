def dziel(n,m):
    maks = 0
    for i in range(1,n+1):
        if n%i == 0 and m%i == 0: maks = i
    return maks

n = int(input('Proszę wprowadzić mniejszą liczbę do sprawdzanie największego wspólnego dzielnika: '))
m = int(input('Proszę wprowadzić większą liczbę do sprawdzanie największego wspólnego dzielnika: '))

print(dziel(n,m))