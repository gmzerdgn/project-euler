# 2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 - 20

# totalDivisors = []
# primeList = []
# def findDivisors(n):
# def findPrimes(n):
    

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

totalDivisors = []
total = 1
#  loop through all the numbers between 1-20. for each number, see if its factors are in the list, if so, divide it by that number
for i in range(2,21):
    for divisor in totalDivisors:
        if i%divisor == 0:
            i = i / divisor
    i = int(i)
    totalDivisors.append(i)
    total = total * i
    
print(totalDivisors)
print(total)

