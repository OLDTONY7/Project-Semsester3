import random
number=random.randint(1,10)
print(number)
found =0
print("Guess a Number: ")
x= input("Enter Number")
while found ==0:
    if int(x)==number:
        found =1
    else:
        x=input("Enter Number: ")
        print("Congratulations!")
