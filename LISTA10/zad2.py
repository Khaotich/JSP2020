from itertools import chain, combinations

class Lists:
    def __init__(self, list):
        self.list = list

    def podlisty(self):
        return list(chain.from_iterable(combinations(self.list, n) for n in range(len(self.list) + 1)))

lista = Lists([1,2,3])
print(lista.podlisty())