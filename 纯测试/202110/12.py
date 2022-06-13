products = [['phone',6888],['MacPro',14800],['小米6',2499],['Coffee',31],['Book',60],['Nike',699]]
buylist=[]

while True:
    print('------  商品列表  ------')
    for i in range(0, len(products)):
        print('{0:^2}   {1:{3}^20}  {2}'.format(i, products[i][0], products[i][1], chr(12288)))
    x=input('what do you want to buy?')
    if x != 'q':
        x = int(x)
        buylist.append(products[x][0])
    else:
        buylist.sort()
        print(buylist)
        break