def biggerIsGreater(w):
    index = None
    last_index = None
    for i in range(len(w) -1, -1, -1):
        last = w[i]
        for j in range(len(w) -i-1, -1, -1):
            if w[j] < last:
                index = j
                last_index = i
                break
        
        else:
            continue
        break

    if index == None:
        return "no answer"
    else:
        temp = w[index]
        swap = w[last_index]
        array = list(w)
        array[index] = swap
        array[last_index] = temp

        return "".join(array)

def main():
    word = "dkhc"
    ans = "hcdk"
    #print(biggerIsGreater(word))
    print(convert(word))
    print(convert(ans))

def convert(word):
    return [ord(x) for x in word]

main()
