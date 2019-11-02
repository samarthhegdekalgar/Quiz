"""
Question: Given an array ['a', 'b', 'c', ' ', 'd', ' ', 'e', 'f', 'g']
convert it into ['e', 'f', 'g', ' ', 'd', ' ','a', 'b', 'c']
"""


def reverse_arr(array):
    return array[::-1]


def reverse_element(arr):
    new_arr = []
    start = 0
    for value in range(len(arr)):
        if arr[value] == ' ' or value == len(arr) - 1:
            element = arr[start:value + 1]
            new_arr.append(reverse_arr(element))
            start = value
    new_arr = [value for sublist in new_arr for value in sublist]
    new_arr.pop()
    new_arr.pop(0)
    return new_arr


input_arr = ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ]
result = reverse_arr(input_arr)
print(reverse_element(result))
