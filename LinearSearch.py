def locate_card(card, query):
    # Check card is present at starting occurrences
    occurrences = 0
    # Set up a loop for repetition
    while occurrences < len(card):
        # when card is found
        if card[occurrences] == query:
            return occurrences

        # Increase the occurrences
        occurrences += 1

        # Check if we reached the end of the array
        if occurrences == len(card):
            return -1

    return -1


if __name__ == '__main__':
    # Program starting point
    tests = [{
        # card found at first place
        'input': {
            'card': [10, 20, 30, 40, 50],
            'query': 10
        },
        'output': 0
    }, {
        # card should found at 6th place
        'input': {
            'card': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 1
        },
        'output': 6
    }, {
        # function should return -1 not found
        'input': {
            'card': [],
            'query': 10
        },
        'output': -1

    }, {
        # Element is not present
        'input': {
            'card': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 55
        },
        'output': -1

    },
        {
            # Duplicate element in cards
            'input': {
                'card': [13, 11, 10, 7, 4, 3, 1, 0, 7, 4, 3, 1, 0],
                'query': 7
            },
            'output': 3

        }
    ]
    for ele in tests:
        print('Test Case output  : ', locate_card(ele.get("input").get("card"), ele.get("input").get("query")),
              'Test Case Expected Output : ', ele.get("output"),
              'Result : ', ele.get("output")==locate_card(ele.get("input").get("card"), ele.get("input").get("query"))


              )
