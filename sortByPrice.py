import json

def sortByPrice(input):
    items = json.loads(input)
    arr = []
    for item in items:
        temp = tuple([item['price'],item['item']])
        arr.append(temp)
    from operator import itemgetter
    # itemgetter get the attrbiute out of the item[0] = price, item[1]=item
    new_sorted = sorted(arr,key=itemgetter(0,1))
    temp_arr = []
    for x in new_sorted:
        table = {}
        table["price"] = x[0]
        table["item"] = x[1]
        temp_arr.append(table)

    return json.dumps(temp_arr)

def main():
    input = '[{"price":1,"item":"blueberry"},{"price":2, "item":"orange"},{"price":1,"item":"apple"}]'
    #print(type(obj))
    #print(obj)
    print(sortByPrice(input))

main()
