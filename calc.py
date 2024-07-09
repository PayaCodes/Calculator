num1 = input("Enter a Number: ")
inbetween = input("Enter an operator: ")
num2 = input("Enter another Number: ")
number = 0

num1 = float(num1)
num2 = float(num2)

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

print(f"The calculation is {num1} {inbetween} {num2}")
print(f"The answer is : {number}")
