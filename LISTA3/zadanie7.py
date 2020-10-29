n = int(input('Proszę wprowadzić n: '))
ciag = [0,1]
print(ciag[0])
print(ciag[1])

for i in range(n-2):
    ciag.append(ciag[i]+ciag[i+1])
    print(ciag[i+2])