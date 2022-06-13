import time
codes='217122989310268465506250195'

codefile = open('orderforgoods.txt','a',encoding='utf-8')

ms = int(codes[-8:])
ymd = int(codes[:10])
snl = int(codes[10])

if snl <5:
    pricelock = int(codes[11:-8])
    ms //= 7
    ymd -= ms*600
    pricelock = pricelock//3 - ms

    fulltime = eval(str(ymd)+'.'+str(ms))
    gettime = time.localtime(fulltime)

    print('\n\n\n——————————————————————————————————————————————————————————\n【订单数据】\n订单号：{}\n下单时间：{}年{}月{}日 {:0>2}:{:0>2}:{:0>2}\n下单金额：{}￥\n——————————————————————————————————————————————————————————\n\n\n'.format(codes, gettime.tm_year, gettime.tm_mon, gettime.tm_mday, gettime.tm_hour, gettime.tm_min, gettime.tm_sec, pricelock))
else:
    ms //= 7
    ymd -= ms*600
    fulltime = eval(str(ymd)+'.'+str(ms))
    gettime = time.localtime(fulltime)
    print('\n\n\n——————————————————————————————————————————————————————————\n【订单数据】\n订单号：{}\n下单时间：{}年{}月{}日 {:0>2}:{:0>2}:{:0>2}\n该订单为大额单，订单信息以书面形式由顾客和商家共同保存。{}￥\n——————————————————————————————————————————————————————————\n\n\n'.format(codes, gettime.tm_year, gettime.tm_mon, gettime.tm_mday, gettime.tm_hour, gettime.tm_min, gettime.tm_sec))