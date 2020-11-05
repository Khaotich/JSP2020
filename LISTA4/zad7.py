n=int(input('Proszę wprowadzić liczbę wierszy: '))
trojkat=[]

def netwon(n,k):
    import math
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

for i in range(n):
    z=[]
    for x in range(i+1):
        z.append(netwon(i,x))
    trojkat.append(z)

for i in trojkat:
    print(str(i).strip('[]'))