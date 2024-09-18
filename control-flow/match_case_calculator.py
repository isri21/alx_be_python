num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")


if num2 == 0 and operation == "/":
	print("Cannot divide by zero.")
else:
	match operation:
		case "+":
			print(f"The result is {num1 + num2}")
		case "-":
			print(f"The result is {num1 - num2}")
		case "*":
			print(f"The result is {num1 * num2}")
		case "/":
			print(f"The result is {num1 / num2}")
