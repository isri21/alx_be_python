size = int(input("Enter the size of the pattern: "))
n = 0
while n < size:
	for i in range (0, size):
		print("*", end="")
	print(end='\n')
	n += 1
