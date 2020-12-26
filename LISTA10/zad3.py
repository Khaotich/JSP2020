class Lista:

    def __init__(self, list):
        self.list = list

    def podlisty(self):
        result = []
        for id, element in enumerate(self.list):
            try:
                for i, el in enumerate(self.list[id + 1:]):
                    try:
                        for n in self.list[id + i + 2:]:
                            if element + el + n == 0:
                                result.append([element, el, n])
                    except IndexError:
                        continue
            except IndexError:
                continue
        return result

lista = Lista([-8, 8, 0, 10, 6, -6])
print(lista.podlisty())