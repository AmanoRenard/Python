def select_sort_simple(li): #愚蠢的选择排序
    li_new=[]
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


li=[5,1,2,7,3,8,2]
print(select_sort_simple(li))


def select_sort(li):
    for i in range(len(li)-1):
        min_ind=i
        for j in range(i+1,len(li)):
            if li[j]<li[min_ind]:
                min_ind=j
        if li[i] != li[min_ind]:
            li[i],li[min_ind] = li[min_ind],li[i]

li2=[5,1,2,7,3,8,2]
select_sort(li2)
print(li2)