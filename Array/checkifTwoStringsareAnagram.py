from collections import Counter


# method 1 using sort method
def checkAnagram(str1, str2):
    if len(str1) != len(str2):
        return -1
    if sorted(str1) == sorted(str2):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


# method 2 using set
def checkAnagarmSet(str1, str2):
    if len(str1) != len(str2):
        return -1
    if set(str1) == set(str2):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


# method 3 using counter funtion
def checkAnagarmCounter(str1, str2):
    if Counter(s1) == Counter(s2):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


if __name__ == '__main__':
    str1 = 'bad'
    str2 = 'dad'
    s1 = "listen"
    s2 = "silent"
    checkAnagram(str1, str2)
    checkAnagarmSet(str1, str2)
    checkAnagram(s1, s2)
    checkAnagarmSet(s1, s2)
    checkAnagarmCounter(s1, s2)
