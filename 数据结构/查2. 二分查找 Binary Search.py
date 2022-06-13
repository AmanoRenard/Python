def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:    #候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None


li = [1,4,16,42,66,85,93,102]
print(binary_search(li, 93))