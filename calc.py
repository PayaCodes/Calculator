num1 = input("Enter a Number: ")
inbetween = input("Enter an operator: ")
num2 = input("Enter another Number: ")
number = 0

num1 = int(num1)
num2 = int(num2)

if inbetween == "+":
  number = (num1 + num2)
elif inbetween == "-":
  number = (num1 - num2)
elif inbetween == "*":
  number = (num1 * num2)
elif inbetween == "/":
  number = (num1 / num2)
elif inbetween == "**":
    number = (num1 ** num2)
elif inbetween == "//":
    number == (num1 // num2)
else:
  print("Invalid calculation")

print(f"The answer is : {number}")
