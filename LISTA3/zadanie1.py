samogloski = ['a','e','y','i','o','ą','ę','u','ó']
a = input("Proszę wprowadzić literę: ")

if len(a)!=1 or  not a.isalpha():
    print('Wprowadzono za dużo znaków lub inny znak')
else:
    if a in samogloski:
        print('Podana litera jest samogłoską')
    else:
        print('Podana litera jest spółgłoską')