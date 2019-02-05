import random
from time import time
import matplotlib.pyplot as wykres

boool = True
nums = []
times = []


def SzukBin(A, x):
    l = 0
    p = len(A) - 1
    i = 0

    while l <= p:
        i += 1
        k = int((l + p) / 2)
        if x > A[k]:
            l = k + 1
        elif x < A[k]:
            p = k - 1
        else:
            break

    if A[k] == x:
        return k
    else:
        return 0


limit = int(input('Podaj ilość list: '))
while boool:
    if limit == 0:
        boool = False
        break
    n = random.randrange(2, random.randrange(3, 100))  # długość początkowa listy

    A = []
    B = []
    i = 0
    for i in range(0, n):
        A.append(1 + i)
        i += 1

    for i in range(0, random.randint(1, len(A) - 1)):  # ile wartości wyjetych (max n - 1)
        z = random.randint(0, len(A) - 1)
        B.append(A[z])
        del A[z]

    x = random.randint(1, A[len(A) - 1])

    timeA = time()
    b = SzukBin(A, x)
    timeB = time()

    nums.append(len(A))
    times.append(timeB - timeA)

    limit -= 1

if True:
    times = [x for _, x in sorted(zip(nums, times))]
    nums.sort()

    wykres.plot(nums, times)
    wykres.ylabel('time')
    wykres.xlabel('nums')
    wykres.show()
