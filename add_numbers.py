def add(num1, num2):
	return int(num1) + int(num2)

def subtract(num1, num2):
	return int(num1) - int(num2)

def multiply(num1, num2):
	return int(num1) * int(num2)

def divide(num1, num2):
	return int(num1)/int(num2)

num_1 = input("Please enter a number: ")
num_2 = input("Please enter a second number: ")
operator = input("Select an operation to perform [+, -, *, /]: ")

if operator == "+":
	result = add(num_1, num_2)
elif operator == "-":
	result = subtract(num_1, num_2)
elif operator == "*":
	result = multiply(num_1, num_2)
elif operator == "/":
	if int(num_1) == 0 or int(num_2) == 0:
		result = False
		print("Cannot divide by 0!")
	else: 
		result = divide(num_1, num_2)
else:
	result = False
	print("Invalid operator!")

if result != False:
	print("Your result is: " + str(result))

