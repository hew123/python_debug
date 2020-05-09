def findLowestMissingCharacter(array,char):
    # ASCII int of {a-z} are {97-122}
    ascii = ord(char)
    table = set(array)
    # O(n)
    for x in range(ascii+1, 123):
        lookfor_char = str(chr(x))
        # O(1) for search in set
        if lookfor_char not in table:
            return lookfor_char
    
    #no missing char
    return None

'''
def main():
    array = ['a', 'b', 'c']
    char = 'b'
    print(findLowestMissingCharacter(array, char))


main()
'''