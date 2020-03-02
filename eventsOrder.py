#
# Complete the 'getEventsOrder' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING team1
#  2. STRING team2
#  3. STRING_ARRAY events1
#  4. STRING_ARRAY events2
#

def getEventsOrder(team1, team2, events1, events2):

    dict = {}
    clashed = {}
    times= []
    for event in events1:
        temp = event.split(' ')
        time = 0
        for string in temp:
            if '+' in string:
                temp_time = string.split('+')
                time = int(temp_time[0])
            elif isInt(string) == True:
                time = int(string)
        
        event_name = team1 + ' ' + event
        if time not in times:
            dict[time] = event_name
            times.append(time)
        else:
            #events' time clash
            if time not in clashed.keys():
                clashes = []
                clashes.append(dict[time])
                clashes.append(event_name)
                clashed[time] = clashes
            else:
                array = clashed[time]
                array.append(event_name)


    for event in events2:
        temp = event.split(' ')
        time = 0
        for string in temp:
            if '+' in string:
                temp_time = string.split('+')
                time = int(temp_time[0])
            elif isInt(string) == True:
                time = int(string)
        
        event_name = team2 + ' ' + event
        if time not in times:
            dict[time] = event_name
            times.append(time)
        else:
            #events' time clash
            if time not in clashed.keys():
                clashes = []
                clashes.append(dict[time])
                clashes.append(event_name)
                clashed[time] = clashes
            else:
                array = clashed[time]
                array.append(event_name)

    #sort out clashes
    for time, array in clashed.items():
        array.sort()
        new_time = time
        for event in array:
            dict[new_time] = event
            if new_time not in times:
                times.append(new_time)
            new_time += 0.001
     
    times.sort()
    output = []
    for time in times:
        output.append(dict[time])

    return output


def isInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
