def main():
	
	input = ['a','b','c','d','c','a']

	print(findDuplicate(input))


def findDuplicate(arr):

	output = []

	'''
	for x in arr:	
		count = 0
		for y in arr:

			if  x == y:
				count += 1
				arr.remove(y)
			
		if count > 1:
			output.append(x)
		'''
	for x in arr:
		if arr.count(x)>1:
			output.append(x)
			arr.remove(x)

	return output

def findDuplicate2(arr):

	arr2 = []
	output = []

	for x in arr:
		if x not in arr2:
			arr2.append(x)
		else:
			if x not in output:
				output.append(x)

	return output

def findDuplicate3(arr):

	output = []

	for x in arr:
		temp = x
		arr.remove(x)
		if temp in arr and temp not in output:
			output.append(temp)

	return output 

def findDuplicate4(arr):

	output = arr
	arr2 = list(set(arr))

	for x in arr2:
		output.remove(x)

	output = list(set(output))

	return output

main()