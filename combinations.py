def combo(lst,n):
    if n==0:
        return [[]]
    l=[]
    for i in range(0,len(lst)):
        m=lst[i]
        remLst=lst[i+1:]
        for p in combo(remLst,n-1):
            l.append([m]+p)
    return l

def combo_random(lst,r):
    combo_r = []
    for i in range(r+1):
        temp = combo(lst,i)
        for arr in temp:
            combo_r.append(arr)
    return combo_r

def main():
    array = list('ABCD')
    n = 3 
    print(combo_random(array,n))

main()