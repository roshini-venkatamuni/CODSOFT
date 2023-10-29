def add(num1, num2):
	return num1 + num2
def subtract(num1, num2):
	return num1 - num2
def multiply(num1, num2):
	return num1 * num2
def divide(num1, num2):
	return num1 / num2
print("Please select operation") 
print("1. Add")
print("2. Subtract") 
print("3. Multiply")
print("4. Divide")
select = int(input("Select operations form 1, 2, 3, 4 :"))
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
if select == 1:
	print("The addition of", num1, "+", num2, "is", add(num1, num2))
elif select == 2:
	print("The subtraction of", num1, "-", num2, "is", subtract(num1, num2))
elif select == 3:
	print("The multiplication of", num1, "*", num2, "is", multiply(num1, num2))
elif select == 4:
	print("The division of", num1, "/", num2, "is",	divide(num1, num2))
else:
	print("Invalid input")
