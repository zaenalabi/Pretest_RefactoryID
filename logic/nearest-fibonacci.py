def nearestFibonacci(num):
	
	# Base Case
	if (num == 0):
		print(0)
		return

	# Initialize the first & second
	# terms of the Fibonacci series
	first = 0
	second = 1

	# Store the third term
	third = first + second

	# Iterate until the third term
	# is less than or equal to num
	while (third <= num):
		
		# Update the first
		first = second

		# Update the second
		second = third

		# Update the third
		third = first + second

	# Store the Fibonacci number
	# having smaller difference with N
	if (abs(third - num) >=
		abs(second - num)):
		ans = second
	else:
		ans = third

	# Print the result
	print(ans)
	
abc = []
N = int(input("Masukkan jumlah bilangan array : "))

for i in range(0, N):
    urutan = int(input())
 
    abc.append(urutan) # adding the element
     
print("Daftar array ",abc)
jumlah = sum(abc)
print ("Jumlah", jumlah)

print ("Bilangan Fibonacci Terdekat :"), nearestFibonacci(N)

