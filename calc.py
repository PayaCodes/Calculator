num1 = input(int())
inbetween = input("Enter an operator: ")
num2 = input(int())
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
  number = (num1 // num2)
else:
  print("Invalid calculation")

print(number)
