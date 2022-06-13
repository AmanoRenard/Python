def is_kazu(num): #自定义函数
    if type(num) is not str: #判断num是否为字符串，如果不是：报错。
        raise ValueError('传入的参数必须是字符串！')
    if len(num) > 2 and num.count('.',1,-1) == 1: #判断字符串的长度是否大于2，大于2的话才接着判断有无小数点。
        num=num.replace('.','',1) #替换掉小数点.（如果有的话。最多替换一次）
    if num.isnumeric(): #判断num是否由数字组成，如果是，返回True；如果不是，返回False。
        return True
    else:
        return False

class Item:
    "这是一个商品"
    amount = 0
    def __init__(self):
        Item.amount += 1
        self.id = Item.amount
        print('请输入商品名称与售价！格式：商品名称|售价\n')
        while True:
            msg = str(input('>'))
            try:
                if msg[1:-1].count('|') == 1:
                    msg = msg.split('|')
                    if is_kazu(msg[1]):
                        self.name,self.price = msg[0],eval(msg[1])
                        print('商品录入成功！\n')
                        break
                    else:
                        print('[错误] 商品价格有误，请检查输入！\n')
                else:
                    print('[错误] 格式有误，请重新输入！\n')
            except:
                print('[错误] 无效的商品名称与售价！\n')
    def info(self):
        print('【商品编号】%03d\n【商品名称】%s\n【商品售价】%.2f￥\n' % (self.id,self.name,self.price))

pencil = Item()
eraser = Item()

pencil.info()
eraser.info()