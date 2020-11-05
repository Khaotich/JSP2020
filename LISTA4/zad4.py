def ciag(n, a1=1, q=2):
    return a1*q**(n-1)

n = int(input('Proszę wprowadzić numer wyrazu ciągu geometrycznego: '))
a1 = float(input('Proszę wprowadzić wartość pierwszego wyrazu ciągu: '))
q = float(input('Proszę wprowadzić wartość iloczynu ciągu: '))

print(ciag(n, a1, q))