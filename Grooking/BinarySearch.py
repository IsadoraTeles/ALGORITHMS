def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else :
            low = mid + 1
    return None

m = [1,3,5,6,8,9,13]
i = 8
print ("The index of", i, "in the list is", binary_search(m,i))
