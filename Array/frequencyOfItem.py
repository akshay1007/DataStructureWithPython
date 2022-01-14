def frequency(list):
    dict = {}
    for item in list:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    return dict


if __name__ == '__main__':
    random_list = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']
    print('Total Iteam in list are : ', frequency(random_list))
