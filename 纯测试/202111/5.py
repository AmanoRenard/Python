def hanoi(n, a, b, c):
    if n>0:
        hanoi(n-1, a, c, b)
        print("%s 移到 %s"%(a,c),end=' ;')
        hanoi(n-1, b, a, c)

hanoi(9,"A","B","C")