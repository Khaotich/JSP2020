x = input("Wprowadź tekst: ")
if len(x)<4:
    print("Nie ma możliwości utworzenia nowego tekstu, za mało liter.")
else:
    x = x[:2]+x[len(x)-2:len(x)]
    print(x)