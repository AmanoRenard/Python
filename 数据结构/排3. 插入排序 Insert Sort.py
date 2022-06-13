def insert_sort(li):
    for i in range(1, len(li)): #初始第一张牌就是有序区
        tmp = li[i]
        j = i - 1   #j就是手里的牌
        while j>=0 and li[j] > tmp:
            li[j+1] = li[j]
            j-=1
        li[j+1]=tmp

li=[5,1,2,7,3,8,2]
insert_sort(li)
print(li)