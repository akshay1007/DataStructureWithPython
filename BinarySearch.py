def binary_search(card, query):
    card.sort()
    lo = 0
    hi = len(card) - 1

    while lo <= hi:
        mid = (lo + hi) //2
        # check if querry is present at mid
        if card[mid] == query:
            return mid
        # if query is greater then mid then move to righ
        if card[mid] < query:
            lo = mid + 1
        # if query is smaller then mid move to left
        else:
            hi = mid - 1

    return -1


if __name__ == '__main__':
    tests = [
        {
            'name': '1. card found at first place',
            'input': {
                'card': [10, 20, 30, 40, 50],
                'query': 10
            },
            'output': 0
        },
        {
            'name': '2.card should found at 4th place',
            'input': {
                'card': [10,20,30,40,50,60,70],
                'query': 60
            },
            'output': 5
        },
        {
            'name': '3. function should return -1 not found',
            'input': {
                'card': [],
                'query': 10
            },
            'output': -1

        }, {
            'name': '4. Element is  present at middle ',
            'input': {
                'card': [10, 20, 30, 40, 50],
                'query': 30
            },
            'output': 2

        },
        {
            'name': '5. Bigger input',
            'input': {
                'card': list(range(10000000, 0, -1)),
                'query': 9999999
            },
            'output': 9999998
        }
    ]

    for ele in tests:
        card = ele.get("input").get("card")
        query = ele.get("input").get("query")
        output = ele.get("output")
        name = ele.get("name")
        test_output = binary_search(card, query)
        # locate_card(card, query)
        print(card,query,output,name)
        print('Test Case : ', name)
        print('Test Case output  : ',test_output)
        print('Test Case Expected Output : ', output)
        print('Result : ', output == test_output)
        print("=======================================================")
