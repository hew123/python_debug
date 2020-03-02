def disjoint_network(m, n): 
        """
        :type m: List[List[int]]
        :type n: int
        :rtype: int
        """
        unvisited = []
        for x in range(0,n):
            unvisited.append(x)
        count = 0
      
        while len(unvisited)>1:
            v = unvisited.pop()
            for i, x in enumerate(m[v]):
                if x >2 and (i in unvisited):
                    unvisited.remove(i)
            count+=1
            
        return count

def main():
    m = [[ 0, 3, 0 ],[ 3, 0, 0 ],[ 0, 0, 0 ]]
    m2 =[ [ 0, 3, 0 ],[ 3, 0, 5 ],[ 0, 5, 0 ]]
    n = 3
    print(disjoint_network(m2,n))

main()