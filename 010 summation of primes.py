def isPrime(number, primes):
    for prime in primes:
        if number%prime == 0:
            return False
    return True

i = 2
primeList = [2] 
total = 2
while i < 2000000:
    if isPrime(i,primeList):
        primeList.append(i)
        total += i
    i += 1
    print(i)

print(total)
    

