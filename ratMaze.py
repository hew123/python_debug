def cellsAround(array, point):
    row = len(array)
    col = len(array[0])
    x, y = point
    #return [(a,b) for a in range(x-1,x+2)
    #                for b in range(y-1,y+2)
    #                    if a>=0 and a < col and b>=0 and b<row and (a!=x or b!=y)]
    return [(a,b) for (a,b) in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
                if a>=0 and a < col and b>=0 and b<row and (a!=x or b!=y)]

def pathAround(array, point):
    cells = cellsAround(array,point)
    return [(x,y) for x,y in cells if array[x][y] == 1]

def printVisited(matrix,visited):
    row = len(matrix)
    col = len(matrix[0])
    result = [[0 if (j,i) not in visited else 1 for i in range(col)] for j in range(row)]

    for line in result: print(line)    
    print()

def searchPath(array, current, goal, visited, found):
    
    printVisited(array, visited)

    paths = pathAround(array,current)
    f_paths = [path for path in paths if path not in visited]

    if current == goal:
        return True
    elif f_paths == []:
        return False
    else:
        index = 0
        while not found and index < len(f_paths):
            visited.append(f_paths[index])
            found = searchPath(array, f_paths[index], goal, visited, found)
            if not found: visited.pop() 
            index +=1
    return found

def searchPath2(array, current, goal, visited):
    
    visited.append(current)
    printVisited(array, visited)

    paths = pathAround(array,current)
    f_paths = [path for path in paths if path not in visited]

    if current == goal:
        return True
    elif f_paths == []:
        return False
    else:
        for path in f_paths:
            #visited.append(path)
            if searchPath2(array, path, goal, visited): return True
            visited.pop() 

def main():
    matrix = [[1,0,0,1],
              [1,1,0,1],
              [0,1,0,1],
              [1,1,1,1]]
    #print(pathAround(matrix, (0,0)))
    #printVisited(matrix,[(0,1),(1,0)])
    #print(searchPath(matrix, (0,0), (3,3), [(0,0)], False))
    print(searchPath2(matrix, (0,0), (3,0), []))

main()
