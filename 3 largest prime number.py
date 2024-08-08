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

def isPrime(number, primes):
    for prime in primes:
        if number%prime == 0:
            return False
    return True

n = 600851475143
n = 10000000

start = time.time()
print(start)
primesList = [2]
for i in (range(3,n+1,2)):
    if isPrime(i, primesList):
        primesList.append(i)

end = time.time()
print(end - start)
print(primesList)

