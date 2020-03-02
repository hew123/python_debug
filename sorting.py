def main():
    x = "dcab"

    array = []

    for char in x:
    	array.append(char)

    final = sorted(array)
    combined = ''.join(final)

    print(combined)
  	


       

if __name__ == '__main__':
    main()