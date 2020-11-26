from random import randint
from time import time as t

def sort(n):
    for i in range(1, len(n)):
        key = n[i]
        j = i - 1
        while j >= 0 and n[j] > key:
            n[j + 1] = n[j]
            j -= 1
        n[j + 1] = key

list100 = [randint(0,20) for _ in range(100)]
list200 = [randint(0,20) for _ in range(200)]
list300 = [randint(0,20) for _ in range(300)]

time_now = t()
sort(list100)
time_100 = t()-time_now

time_now = t()
sort(list200)
time_200 = t()-time_now

time_now = t()
sort(list300)
time_300 = t()-time_now

print("Czas działania funkcji dla 100 elementów:", time_100)
print("Czas działania funkcji dla 200 elementów:", time_200)
print("Czas działania funkcji dla 300 elementów:", time_300)