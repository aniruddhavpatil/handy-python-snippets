I = [
		[1,2,3,4],
		[5,6,7,8],
		[9,10,11,12]
	]

I = [ [ i for i in row[::-1]] for row in I[::-1]]
# I = [ [ i^1 for i in row for row in I[::-1]] // In terms of binary flip


print(I)
