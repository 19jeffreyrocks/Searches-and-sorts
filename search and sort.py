def linear_search(list1, value):
    i = 0
    while list1[i] != value and i < len(list1):
        i += 1
    if i < len(list1):
        return i
    else:
        return None


def binary_search(list1, value):
    upper = len(list1)
    lower = 0
    while upper >= lower:
        mid = (lower + upper) // 2
        if list1[mid] == value:
            return mid
        elif list1[mid] > value:
            upper = mid - 1
        else:
            lower = mid + 1


def insertion_sort(list1):
    for i in range(1, len(list1)):
        while i > 0 and list1[i - 1] > list1[i]:
            list1[i - 1], list1[i] = list1[i], list1[i - 1]
            i = i - 1
    return list1


def selection_sort(list1):
    for i in range(0, len(list1) - 1):
        current_min = i
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[current_min]:
                current_min = j
        list1[i], list1[current_min] = list1[current_min], list1[i]
    return list1


def bubble_sort(list1):
    n = len(list1)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (list1[j] > list1[j + 1]):
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1


print(linear_search([2, 5, 6, 1, 4], 4))
print(binary_search([1, 3, 5, 6, 8], 5))
print(insertion_sort([1, 5, 2, 11, 7, 10, 9]))
print(selection_sort([1, 5, 2, 11, 7, 10, 9]))
print(bubble_sort([1, 5, 2, 11, 7, 10, 9]))
