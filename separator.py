def separator(string):
    items = string.split(',')
    integers = []
    chars = []
    for item in items:
        if isInt(item):
            integers.append(item)
        else:
            chars.append(item)

    if len(integers)!= 0 and len(chars)!=0:
        result = ','.join(chars) + '|' + ','.join(integers)
    elif len(integers)!= 0 and len(chars)==0:
        result = ','.join(integers)
    elif len(integers)== 0 and len(chars)!=0:
        result = ','.join(chars)
    else:
        result = ''
    
    return result

def main():
    input = "aapplel,123,orangee,grapes,100,7000,exit"
    print(separator(input))

def isInt(item):
    try:
        int(item)
        return True
    except ValueError:
        return False

main()