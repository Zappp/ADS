import math
import random
from time import time
import matplotlib.pyplot as plt


def cheap_sort(n):
    A = []
    for i in range(0, n):
        A.append(i)
    random.shuffle(A)

    x = len(A)
    for i in range(x):
        y = len(A)
        w = math.floor((y - 2) / 2)  # wezel -->iteracja po wartościach listy
        for j in range(w, -1, -1):
            lk = 2 * j + 1  # lewy korzen
            pk = 2 * j + 2  # prawy korzen

            if pk < y and A[pk] > A[lk]:
                A[lk], A[pk] = A[pk], A[lk]
            if A[lk] > A[j]:
                A[j], A[lk] = A[lk], A[j]
        A[0], A[y - 1] = A[y - 1], A[0]
        del A[y - 1]


limit = int(input('Ilość wyszukiwań: '))

boool = True
nums = []
times = []
n = 1

while boool:
    if limit == 0:
        boool = False
        break

    timeA = time()
    cheap_sort(n)
    timeB = time()

    nums.append(n)
    times.append(timeB - timeA)

    limit -= 1
    n += 2

if True:
    times = [x for _, x in sorted(zip(nums, times))]
    nums.sort()

    plt.plot(nums, times)
    plt.ylabel('time')
    plt.xlabel('nums')
    plt.show()
