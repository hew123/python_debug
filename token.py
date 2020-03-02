def numberOfTokens(expiryLimit, commands):
    # Write your code here
    #create dict
    tokens = {}
    popped = []
    for command in commands:
        instruction = command[0]
        token_id = command[1]
        time = command[2]

        if instruction==0:
            #get token
            if token_id in tokens or (token_id in popped):
                pass
            else:
                expiry_time = time + expiryLimit
                tokens[token_id] = expiry_time
        else:
            #reset token
            if token_id not in tokens:
                pass
            else:
                if time > tokens[token_id]:
                    #token has expired
                    popped.append(token_id)
                    tokens.pop(token_id)
                    pass
                else:
                    #reset token expiry time
                    tokens[token_id] = tokens[token_id] + expiryLimit
    #end of command stream
    current_time = commands[-1][2]
    count = 0
    for x in tokens:
        if tokens[x] > current_time:
            count +=1
    return (count)

def main():
    expiryLimit = 3
    commands = [[0, 1, 1],[1,1,5]]
    print(numberOfTokens(expiryLimit, commands))


main()