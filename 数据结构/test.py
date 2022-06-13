import random
import time
from cal_time import *

myli = list(range(10000))
myli2 = list(range(10000))
random.shuffle(myli)
random.shuffle(myli2)

@cal_time
def n_sort(li):
    li.sort()

@cal_time
def insert_sort(li):
    for i in range(1, len(li)): #初始第一张牌就是有序区
        tmp = li[i]
        j = i - 1   #j就是手里的牌
        while j>=0 and li[j] > tmp:
            li[j+1] = li[j]
            j-=1
        li[j+1]=tmp

n_sort(myli2)
insert_sort(myli)