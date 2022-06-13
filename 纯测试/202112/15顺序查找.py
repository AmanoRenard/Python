def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None


print(linear_search([1, 5, 4, 2, 1, 6, 2, 3], 6))