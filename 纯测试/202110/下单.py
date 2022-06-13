import time
import random
price = 13111
buytimes=time.time();buytime=str(buytimes).split('.');buytimes=time.localtime(buytimes)
t0=int(buytime[0]);t1=int(buytime[1])
if price < 10000:
    notecode = '{0:0>10}{1}{2:0>8}{3:0>8}'.format((t0+t1*600) , random.randint(0,4) , (price+t1)*3 , int(t1)*7)
    print('\n\n\n——————————————————————————————————————————————————————————\n下单成功！\n【订单数据】\n订单号：{}\n下单时间：{}年{}月{}日 {:0>2}:{:0>2}:{:0>2}\n下单金额：{}￥\n——————————————————————————————————————————————————————————\n\n\n'.format(notecode, buytimes.tm_year, buytimes.tm_mon, buytimes.tm_mday, buytimes.tm_hour, buytimes.tm_min, buytimes.tm_sec, price))
elif price >= 10000:
    notecode = '{0:0>10}{1}{2:0>8}{3:0>8}'.format((t0+t1*600) , random.randint(5,9) , random.randint(0,99999999) , int(t1)*7)
    print('\n\n\n——————————————————————————————————————————————————————————\n下单成功！\n【订单数据】\n订单号：{}\n下单时间：{}年{}月{}日 {:0>2}:{:0>2}:{:0>2}\n这是一笔大额订单，该订单记录仅供参考。\n请联系店主开出书面证明文件！\n——————————————————————————————————————————————————————————\n\n\n'.format(notecode, buytimes.tm_year, buytimes.tm_mon, buytimes.tm_mday, buytimes.tm_hour, buytimes.tm_min, buytimes.tm_sec))
notefile = open('orderforgoods.txt', 'a',encoding='utf-8');notefile.write('%s\n'%notecode);notefile.close()