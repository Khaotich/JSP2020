x = input("Wprowadź tekst: ")
x = x[0]+x.replace(x[0],"$")[1:]
print(x)