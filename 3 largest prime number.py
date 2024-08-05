import math
import time

def divides(n, i):
    int(n)
    int(i)
    if n%i == 0:
        returnValue = True
    else:
        returnValue = False
    return returnValue

def isPrime(number):
    for i in range(3, round(math.sqrt(number))+1,2):
        if number%i == 0:
            return False
    return True

n = 600851475143
n = 10000000

start = time.time()
print(start)
primesList = []
for i in (range(3,n+1,2)):
    if isPrime(i):
        primesList.append(i)

end = time.time()

print(end - start)