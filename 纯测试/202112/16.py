def select_sort(li):
    for i in range(len(li) - 1):
        min_ind = i
        for o in range(i+1,len(li)):
            if li[min_ind] > li[o]:
                min_ind = o
        li[min_ind],li[i] = li[i],li[min_ind]


def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for o in range(i,len(li)-i-1):
            if li[o]>li[o+1]:
                li[o],li[o+1] = li[o+1],li[o]
                exchange = True
        if exchange == False:
            return

def insert_sort(li):
    for i in range(1,len(li)):
        ind = i-1
        tmp = li[i]
        while ind >= 0 and li[ind]>tmp:
            li[ind+1] = li[ind]
            ind-=1
        li[ind+1] = tmp


li=[1,6,52,2,6,7,8,32,4,7,1,65,76,2]
insert_sort(li)
print(li)
