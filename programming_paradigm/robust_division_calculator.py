def safe_divide(numerator, denominator):
	try:
		ans = int(numerator) / int(denominator)
	except ValueError:
		print("Error: Please enter numeric values only.")
		exit()
	except ZeroDivisionError:
		print("Error: Cannot divide by zero.")
		exit()
	else:
		return f"The result of the division is {ans}"                                   
