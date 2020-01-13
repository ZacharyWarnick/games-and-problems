'''
File: EvenMagicSquare.py

Description: recursively finds a number of magic squares of size 4
'''


import sys

maximum = 1
count = 0

def permute (a, lo):

	global count
	global maximum
	if count == maximum:
		sys.exit()

	hi = len(a)

	square = convertDimension(a,4)

	if lo == hi:
		if (checkSquare4(square)):
			printSquare(square)
			count += 1


	else:
		for i in range (lo, hi):

			a[lo], a[i] = a[i], a[lo]
			permute (a, lo + 1)
			a[lo], a[i] = a[i], a[lo]

def checkSquare4(square):
	maximumList = []
	#print(square)

	#column check
	colcheck = 0
	colTotal = 0
	for col in range(len(square)):
		#print(square[col])
		if int(sum(square[col])) == 34:
			colTotal = 34
			col34 = True
		else:
			col34 = False
			break

	#row check
	rowCheck = 0
	n = 0
	for col in range(4):	
		rowCheck = 0
		for idx in range(0,len(square)):
			rowCheck += square[idx][n]

		if rowCheck == 34:
			row34 = True
		else:
			row34 = False
			break
		n += 1


	#LR diag check
	LRtotal = 0
	for idx in range(0,len(square)):
		LRtotal += square[idx][idx]
	if  LRtotal == 34:
		lr34 = True
	else:
		lr34 = False
		

	#RL diag check 
	RLtotal = 0
	topRight = len(square)-1
	for idx in range(0,len(square)):
		RLtotal += square[topRight-idx][idx]
	if RLtotal == 34:
		rl34 = True
	else:
		rl34 = False




	#print(colTotal,rowCheck,RLtotal,LRtotal)
	return col34 and row34 and rl34 and lr34

def convertDimension(nums,size):

  return [nums[i:i+size] for i in range(0, len(nums), size)]

def printSquare(square):
	start = 0
	for num in range(0,len(square)):
		for k in square:
			print(str(k[start]).rjust(3),end=" ")
		print()	
		start += 1
	print()

def main():
	global maximum
	maximum = 11

	print()
	while maximum > 10 or maximum < 1:
		maximum = eval(input("Enter number of magic squares (1 - 10): "))
	print()


	integerSet = [1,2,15,16,12,14,3,5,13,7,10,4,8,11,6,9]


	(permute(integerSet,0))


if __name__ == '__main__':
  main()