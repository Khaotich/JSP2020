def permutacje(*args):
    from itertools import permutations
    if len(args) > 1:
        for i in permutations(args):
            print(i)
    else:
        print('Lista jest pusta')

print(permutacje(1,2,3))