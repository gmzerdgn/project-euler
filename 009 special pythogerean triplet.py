# a < b < c where a2+b2=c2
# a + b + c = 1000 triplets
import math 


# a = 1


# print(math.sqrt(1000))
# triplet = False
# while not triplet:
#     b = 0
#     c = math.sqrt(a**2 + b**2)
#     while a >= b:
#         if a + b + c == 1000:
#             triplet = True
#         else:
#             b += 1
#             c = math.sqrt(a**2 + b**2)
#     a += 1

a = 1
b = 1
while b < 1000:
    a = 1
    while a < 1000:
        c = math.sqrt(a**2 + b**2)
        if a + b + c == 1000:
            print(a)
            print(b)
            print(c)
            print(a*b*c)
            b = 100000
        a += 1
    b += 1

    

        
