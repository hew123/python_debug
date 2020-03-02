def compute_population(n):
    time = 0
    #dict of reapers with id and time 
    reapers={}
    #num of reapers
    count = 1
    id = 1
    #keep track of active reapers
    active = []

    reapers[id] = 0
    active.append(id)

    while n > time:
        #time starts
        time +=1
        to_add = []
        for id in active:
            reapers[id] += 1
            if reapers[id] > 8:
                #retire
                active.remove(id)
            elif reapers[id] <= 4:
                #still hibernate
                pass
            else:
                #replicate
                id +=1
                reapers[id] = 0
                to_add.append(id)
                count +=1
                break
        for x in to_add:
            active.append(x)
    return count

def main():
    n = 10
    print(compute_population(n))

main()