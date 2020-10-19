import builtins
lista = dir(builtins)
for i in lista: print(i)
print(help(print))

print("Ala ma kota")
print(2+2)
print("{}\t{}\t{}".format(2**5,35//2,35%2))
print("{}\n{}\n{}".format(2**5,35//2,35%2))