
def main():
    for number in range(1,101): 
        print(fizzbuzz2(number))

def fizzbuzz(number):
    if number % 15 == 0:
        return 'fizzbuzz'
    elif number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'
    else:
        return number     

def fizzbuzz2(number):
    output = ""
    if number % 3 == 0:
        output += "fizz"
    if number % 5 == 0:
        output += "buzz"
    return output or number
    

main()