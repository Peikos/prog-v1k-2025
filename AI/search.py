def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

def linear_search_sorted(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
        elif target < lst[i]:
            return -1
    return -1



print(linear_search([1,3,8,2], 3))
print(linear_search_sorted([1,2,3,8,11,13], 3))
print(linear_search([1,3,8,2], 5))
print(linear_search_sorted([1,2,3,8,11,13], 5))