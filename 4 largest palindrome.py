numbers = [999]

def isPalindrome(pal):
    pal = str(pal)
    n = len(pal)
    for i in range(0, int(n/2)):
        if pal[i] != pal[n-1-i]:
            return False
    return True

palindromes = []
found = True
while found: 
    for number in numbers:
        currentNumber = number*numbers[-1]
        if isPalindrome(currentNumber):
            print(f'{number} * {numbers[-1]} = {currentNumber}')
            palindromes.append(currentNumber)
    numbers.append(numbers[-1] - 1)
    if numbers[-1] == 99:
        break

print(f'Largest palindrome: {max(palindromes)}')
