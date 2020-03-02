def main():
	print("hello world")
	arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
	result = hourglassSum(arr)
	print("the result is "+ str(result))

def hourglassSum(arr):
    maxSum = -1000
    counter1 = 0
    while counter1<len(arr)-2:
        counter2 = 0
        while counter2<len(arr)-2:
            threeD = findhourglass(arr,counter1,counter2)
            sum = calculatehourglass(threeD)
            if sum > maxSum:
                maxSum = sum
            counter2 = counter2 + 1
        counter1 = counter1 +1
        
    return maxSum

def findhourglass(arr,n,m):
    #threeD = [[arr[0][0],arr[0][1],arr[0][2]],[arr[1][0],arr[1][1],arr[1][2]],[arr[2][0],arr[2][1],arr[2][2]]]
    threeD = [[arr[n][m],arr[n][m+1],arr[n][m+2]],[arr[n+1][m],arr[n+1][m+1],arr[n+1][m+2]],[arr[n+2][m],arr[n+2][m+1],arr[n+2][m+2]]]
    return threeD

def calculatehourglass(arr):
    sum = 0
    for index1, x in enumerate(arr):
        for index2, y in enumerate(x):
            if index1== 1:
                if index2==0 or index2==2:
                    pass
                else:
                    sum = sum + y
            else:
                sum = sum + y
    return sum


if __name__ == '__main__':
    main()