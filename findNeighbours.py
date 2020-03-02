arr = [[1,2,3],[4,5,6],[7,8,9]]

Xsize = len(arr)
Ysize = len(arr[0])

def main():
	#neighbours(1,1)
	for x in arr:
		print(x)
	neighbours(0,0)

def neighbours(x,y):

	'''
	for x2 in range(x-1, x+2):
		for y2 in range(y-1,y+2):
			if (0<=x2<Xsize)  and (0<=y2<Ysize) and (x2!=x or y2!=y):
				print(arr[x2][y2])
	'''
	
	neighbours = [arr[x2][y2] for x2 in range(x-1, x+2)
								for y2 in range(y-1,y+2)
									if (0<=x2<Xsize)  and (0<=y2<Ysize) and (x2!=x or y2!=y)]

	print("neighbours of [" + str(arr[x][y]) + "] are: ")
	print(neighbours)

main()