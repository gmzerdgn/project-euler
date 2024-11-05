# count = 1
# primeList = [2]
# while count < 11:
#     i = primeList[-1] + 1
#     prime = False
#     while not prime:
#         for j in primeList:
#             if i%j == 0:
#                 prime = True
#                 print(i)
#                 count += 1
#                 print("if")
#                 break
            
#             print(j + "for")
#         print(prime + "inner while")
#     print(count + "outer while")

# print(primeList)

# prime = True
# print(i)
# count += 1

def isPrime(number, primes):
    for prime in primes:
        if number%prime == 0:
            return False
    return True

count = 1
primeList = [2] 
for count in range(1,10001):
    i = primeList[-1] + 1
    while not isPrime(i,primeList):
        i += 1
    primeList.append(i)
    count += 1

print(primeList[-1])

