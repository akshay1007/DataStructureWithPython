# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from pprint import pprint
from jovian.pythondsa import evaluate_test_cases


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def locate_card(card, query):
    # create a variable position with the value 0
    position = 0

    # Set up a loop for repetition
    while True:
        print('position: ', position)
        # Check if element at the current position match the query
        if card[position] == query:
            # Answer found! Return and exit
            return position

        # Increase the position
        position += 1

        # Check if we reached the end of the array
        if position == len(card):
            return -1

        # Number not found, return -1
        return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    card = [13, 11, 10, 7, 4, 3, 1, 0]
    query = 7
    output = 3
    tests = []
    # query for random number
    test = {
        'input': {
            'card': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 7
        },
        'output': 3
    }
    tests.append(test)
    # query appear in the middle
    tests.append({
        'input': {
            'card': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 1
        },
        'output': 6
    })

    # query appear in the first place
    tests.append({
        'input': {
            'card': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 13
        },
        'output': 0
    })

    # query appear in the last
    tests.append({
        'input': {
            'card': [13, 11, 10, 7, 4, 3, 1, 0, -127],
            'query': 0
        },
        'output': 7
    })
    # card does not contain query
    tests.append({
        'input': {
            'card': [13, 11, 10, 7, 4, 3, 1, 0, -127],
            'query': 88
        },
        'output': -1
    })

    # card array is empty
    tests.append({
        'input': {
            'card': [],
            'query': 88
        },
        'output': -1
    })

    # numbers can repeat in the cards
    tests.append({
        'input': {
            'card': [13, 11, 10, 7, 4, 3, 1, 0, -127, 10, 7, 4, 3, 1, 0, -127, 10, 10, 7, 4, 3, 1, 0, -127],
            'query': 10
        },
        'output': 2
    })

    # numbers can repeat in the cards
    tests.append({
        'input': {
            'card': [13, 11, 10, 7, 4, 3, 1, 55, 0, -127, 10, 7, 4, 3, 1, 0, -127, 10, 10, 7, 4, 3, 1, 0, -127],
            'query': 55
        },
        'output': 7
    })

    for test in tests:
        evaluate_test_cases(locate_card, tests)

# print(locate_card(**test['input']) == test['output'])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
