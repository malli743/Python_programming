numbers = [12,7,25,8,14,44,43,98]
total = 0
even_count = 0
odd_count = 0
for number in numbers:
	total = total + number
	if number % 2 == 0:
		even_count += 1
	else:
		odd_count += 1
print(even_count)
print(odd_count)
print(total)