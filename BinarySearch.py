def test_location(card, query, mid):
    mid_number = card[mid]
    print("mid:", mid, ", mid_number:", mid_number, 'query : ', query )
    if mid_number == query:
        if mid-1 >= 0 and card[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'right'
    else:
        return 'left'


def locate_card(cards, query):
    lo = 0
    hi = len(cards) - 1

    while lo <= hi:
        print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
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

        }
    ]

    for ele in tests:
        card = ele.get("input").get("card")
        query = ele.get("input").get("query")
        output = ele.get("output")
        name = ele.get("name")
        test_output = locate_card(card, query)
        # locate_card(card, query)
        print(card,query,output,name)
        print('Test Case : ', name)
        print('Test Case output  : ',test_output)
        print('Test Case Expected Output : ', output)
        print('Result : ', output == test_output)
        print("=======================================================")
