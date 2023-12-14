userInput1 = int(input("Enter First Number: "))
userInput2 = int(input("Enter Second Number: "))
userInput3 = int(input("Enter Third Number: "))


def sumall():
    print('Result is:', userInput1 + userInput2 + userInput3)

def multiply():
    print('Result is:', userInput1 * userInput2 * userInput3)

def multiply2():
    print('Result is:', userInput1 * userInput2 + userInput3)

def multiply3():
    print('Result is:', userInput1 + userInput2 * userInput3)

if userInput1 == userInput2 == userInput3:
    multiply()
elif userInput1 == userInput2 > userInput3:
    multiply2()
elif userInput1 == userInput2 < userInput3:
    multiply2()
elif userInput1 < userInput2 == userInput3:
    multiply3()
elif userInput1 > userInput2 == userInput3:
    multiply3()
elif userInput1 > userInput2 > userInput3:
    sumall()
elif userInput1 < userInput2 < userInput3:
    sumall()
elif userInput1 < userInput2 < userInput3:
    sumall()
elif userInput1 > userInput2 < userInput3:
    sumall()
elif userInput1 < userInput2 > userInput3:
    sumall()

