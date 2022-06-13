def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for o in range(len(li)-1-i):
            if li[o]> li[o+1]:
                li[o],li[o+1] = li[o+1],li[o]
                exchange = True
        if exchange == False:
            return

li=[5,1,2,7,3,8,2]
bubble_sort(li)
print(li)