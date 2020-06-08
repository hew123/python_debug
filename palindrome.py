def isPalindrome(string):
    if len(string)%2 == 1:
        return False
    else:
        mid = int(len(string) /2)
        for x in range(mid):
            if string[x] != string[-(x+1)]:
                return False
        return True

def switchSequence(string):

    if isPalindrome(string):
        return string

    combi = string
    for x in range(len(string)):
        if x+2 >= len(string):
            return "NO"
        else:
            combi = combi[:x] + combi[x+2] + combi[x+1] + combi[x] + ("" if x+3 >= len(string) else combi[x+3:])
            
            if isPalindrome(combi):
                return combi
    

def main():
    _input = "CCABBA"
    print(switchSequence(_input))

main()