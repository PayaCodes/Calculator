import math, random
choice = input("Choose 1 for square root, 2 for a calculation and 3 for a dice roll: ")

def dice():
    diceCount = input("Please choice a maximum number for your dice: ")
    diceCount = int(diceCount)
    count = random.randint(0, diceCount)
    print(f"The number that got rolled is {count}")

def mainCalc():    
    baseNumber = input("What is your first number? : ")
    baseNumber = float(baseNumber)
    amountOfNumbers = input("How many more numbers are there in your calculation? : ")
    amountOfNumbers = int(amountOfNumbers)
    
    for i in range(amountOfNumbers):
        op = input("What is your operator? : ")
        num = input("Pick another number: ")
        num = float(num)
        if op == "+":
            baseNumber = baseNumber + num
        elif op == "-":
            baseNumber = baseNumber - num
        elif op == "*":
            baseNumber = baseNumber * num
        elif op == "/":
            baseNumber = baseNumber / num
        elif op == "**":
            baseNumber = baseNumber ** num
        elif op =="//":
            baseNumber = baseNumber // num
        else:
            print("Error")
        
    print(f"Your answer to your calculation is {baseNumber}")

def sqrtFun():
    sqrtNum = input("Please choose a number to Square root: ")
    sqrtNum = float(sqrtNum)
    sqrtNum = math.sqrt(sqrtNum)
    print(f"Your answer is {sqrtNum}")

if choice == "1":
    sqrtFun()
elif choice == "2":
    mainCalc()
elif choice == "3":
    dice()
