# "p1 sell s1 1500 200"

seller_list = []
buyer_list = []


def convert(string):
    li = list(string.split(" "))
    return li


def objCreation(li):
    obj = {
        'stock': li[2],
        'person': li[0],
        'trade': li[1],
        'qty': li[3],
        'price': li[4]
    }
    return obj


def seller(obj):
    seller_list.append(obj)


def buyer(obj):
    buyer_list.append(obj)

def trade(obj,p):
    print('-------------------------')
    print(p)
    print(obj)
    print('-------------------------')
if __name__ == '__main__':
    arr = ["p1 sell s1 1500 200",
           "p3 buy s1 600 250"]
    for data in arr:
        li = convert(data)
        print(li)
        obj = objCreation(li)
        key = obj['trade']
        print(key)
        if key == 'sell':
            seller(obj)
        else:
            buyer(obj)
        for p in buyer_list:
            if p['stock'] == obj['stock']:
                print(obj['person'] ,' buyer is interested ', obj['stock'])
                trade(obj,p)

    print(buyer_list)
    print()
    print(seller_list)
