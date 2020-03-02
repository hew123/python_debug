def isPossible(calCounts, requiredCals):
    # Write your code here
    for cal in calCounts:
        if cal == requiredCals:
            return True
        elif cal > requiredCals:
            calCounts.remove(cal)
        else:
            pass
    if not calCounts:
        #check empty list
        return False
    else:
        #return recursiveFunc(calCounts, requiredCals)
        return itertoolsRecursive(calCounts,requiredCals)

def recursiveFunc(calCounts, requiredCals):
    
    total = sum(calCounts)

    if total == requiredCals:
        return True
    elif total > requiredCals:
        #pop cal
        if len(calCounts) <= 2:
            return
        else:
            for i ,cal in enumerate(calCounts):
                value = calCounts.pop(i)
                recursiveFunc(calCounts, requiredCals)
                calCounts.insert(i,value)
    else:
    #sum is smaller than requiredCals
        return
    
    return False

def itertoolsRecursive(calCounts,requiredCals):
    from itertools import combinations
    combi = []
    for i in range(2,len(calCounts)):
        result = combinations(calCounts,i)
        for item in result:
            combi.append(list(item))

    for x in combi:
        if sum(x) == requiredCals:
            return True

    return False


def main():
    calCounts = [2,6,3,4,5,1]
    requiredCals = 7
    print(isPossible(calCounts,requiredCals))

main()