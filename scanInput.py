def main():
    '''
    while(1):
        try:
            line = int(input())
            print(line)
        except EOFError:   
            break
    '''
    numOfID = int(input()) 
    numOftrxn = int(input())
    
    counter1 = 0
    ids = []
    while counter1 < numOfID:
        id = int(input())
        ids.append(id)
        counter1 += 1
    
    counter2 = 0
    while counter2 < numOftrxn:
        counter2 += 1
        line = input()
        #map(int, line.split(' '))
        n , identity = [int(i) for i in line.split()]
        #print(identity)
        #identity = line[1]
        if identity in ids:
            index = ids.index(identity)
            ids.pop(index)
    
    #print(ids)
    string = ' '.join([str(x) for x in ids])
    print(string)
    
if __name__ == "__main__":
    main()
