def factorial_for(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

number = int(input("Enter a number to calculate its factorial: "))
print("Factorial using for loop:", factorial_for(number))
