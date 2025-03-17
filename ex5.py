def factorial_while(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

number = int(input("Enter a number to calculate its factorial: "))
print("Result of the factorial:", factorial_while(number))
