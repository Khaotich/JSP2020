def ciag(n):
    if n == 1:
        return ["1"]
    elif n == 2:
        return ["1","11"]
    else:
        string = "11"
        lista = ["1","11"]
        for i in range(3, n + 1):
            string += '$'
            l = len(string)
            c = 1
            temp = ""

            for j in range(1, l):
                if (string[j] != string[j - 1]):
                    temp += str(c + 0)
                    temp += string[j - 1]
                    c = 1
                else:
                    c += 1

            string = temp
            lista.append(string)
        return lista

n = int(input("Proszę wprowadzić ilość wyrazów ciągu: "))
print(ciag(n))