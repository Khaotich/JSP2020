from time import time as t
#Ciąg Fibbonaciego
def rec_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)

def fibb(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = int(input("Proszę wprowadzić liczbę wyrazów ciagu do wygenerowania: "))

start_iter = t()
print(list(fibb(n)))
stop_iter = t()-start_iter

start_rek = t()
print(rec_fib(n-1))
stop_rek = t()-start_rek

print("Czas iteracyjny:",stop_iter)
print("Czas rekurencyjny:",stop_rek)