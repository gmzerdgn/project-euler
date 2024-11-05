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

# # Largest Prime Factor

# def prime_number(b):
#     c1 = 0
#     for i in range(1,int(b/2)+1):
#         if b % i == 0:
#             c1 += 1
#     if c1 < 2:
#         return(True)
#     else:
#         return(False)

# def prime_factor(a):
#     n = 0
#     count = 1
#     prime = 0
#     while n < a+1:
#         n += 1
#         if a % n == 0:
#             if prime_number(n) == True:
#                 prime = n
#                 print(prime)
# prime_factor(600851475143)

