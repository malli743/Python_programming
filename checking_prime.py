
num = int(input("Enter an number:"))
if num > 1:
	for i in range(2, int(num**0.5) + 1):
		if num % i == 0:
			print("Not a prime Number")
			break
			
	else:
		print("Given number is Prime Number")
else:
	print("Enter valid Number")