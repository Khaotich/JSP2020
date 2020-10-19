a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b taką że b jest większe od a: "))

if b < a:
    Z = b % a
    Z *= Z + 3
    print(Z)
else:
    print("Podano złą wartość b!")