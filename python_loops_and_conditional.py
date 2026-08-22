numbers = [1,2,3,4,5,6,7,8,9,10]
output = []
for number in numbers:
	if number % 2 == 0:
		if number % 4 == 0:
			output.append(f"{number} is divisible by 4 ")
		else:
			output.append(f"{number} is even")
print(output)

output:
['2 is even', '4 is divisible by 4 ', '6 is even', '8 is divisible by 4 ', '10 is even']