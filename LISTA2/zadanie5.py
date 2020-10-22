x = input("Wprowadź tekst: ")
x = x[:int(len(x)/2)] + 'Python' + x[int(len(x)/2):]
print(x)