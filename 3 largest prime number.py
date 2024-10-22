# Largest Prime Factor

def prime_number(b):
    c1 = 0
    for i in range(1,int(b/2)+1):
        if b % i == 0:
            c1 += 1
    if c1 < 2:
        return(True)
    else:
        return(False)

def prime_factor(a):
    n = 0
    count = 1
    prime = 0
    while n < a+1:
        n += 1
        if a % n == 0:
            if prime_number(n) == True:
                prime = n
                print(prime)
print(prime_factor(600851475143))