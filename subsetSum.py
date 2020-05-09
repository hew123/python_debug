def subsetSum(arr,sum_, ans):

    #print(arr)

    if sum(arr) == sum_:
        ans.append(arr)
    elif len(arr) == 1 or sum_ > sum(arr):
        pass
    else:
        for index in range(len(arr)):
            temp = arr[:index] + arr[index+1:]
            ans = subsetSum(temp, sum_, ans)

    return ans

def isSubsetSum(arr,sum_, found):

    #print(arr)

    if sum(arr) == sum_:
        return True
    elif len(arr) == 1 or sum_ > sum(arr) or found:
        return False
    else:
        index = 0
        while not found and index < len(arr):
            temp = arr[:index] + arr[index+1:]
            found = isSubsetSum(temp, sum_, found)
            index += 1

    return found

def main():
    array = [1,2,3,4]
    sum_ = 5
    print(subsetSum(array, sum_, []))
    print(isSubsetSum(array, sum_, False))

main()

