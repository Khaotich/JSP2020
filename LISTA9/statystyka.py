from sys import argv
from numpy import average, var, std

if len(argv)<2:
    print('Nie podano żadnych argumentów!')

elif len(argv) == 2:
    try:
        file = open(argv[1], 'r', encoding='utf-8')
    except:
        print('Błąd otwarcia pliku!')
    else:
        values = []
        for i in file.readlines(): values.append(int(i.strip()))
        a = average(values)
        v = var(values)
        s = std(values)
        print('Średnia to {}\nWariacja to {}\n'
              'Odchylenie standardowe to {}'.format(a, v, s))
    finally:
        file.close()

elif len(argv) > 2:
    values = []
    for i in range(1,len(argv)): values.append(int(argv[i].strip()))
    a = average(values)
    v = var(values)
    s = std(values)
    print('Średnia to {}\nWariacja to {}\n'
          'Odchylenie standardowe to {}'.format(a, v, s))