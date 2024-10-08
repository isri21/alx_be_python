FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
	return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
	return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
	temprature = input("Enter the temperature to convert: ")

	try:
		temp_int = float(temprature)
		type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

		if type == "C":
			print(f"{temp_int}°C is {convert_to_fahrenheit(temp_int)}°F")
		elif type == "F":
			print(f"{temp_int}°F is {convert_to_celsius(temp_int)}°C")
		else:
			print("Please enter the correct type.")

	except ValueError:
		print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
	main()
