def collatz(num):
	print(num)
	x = True
	while x == True:
		if num == 1:
			x = False
		elif num % 2 == 0:
			print(num/2)
			num  = num/2
		else:
			print((3*num)+1)
			num = ((3*num)+1)

collatz(3)