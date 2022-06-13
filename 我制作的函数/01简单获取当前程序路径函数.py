import os

# 定义Rei_FilePath函数
def Rei01_GetFilePath():
    Rei01_Path = [__file__,]
    # 初始化
    Rei01_Int = int(-1)
    Rei01_GetPath = 1
    # 开始循环，检测是否有\号
    for Rei01_i, Rei01_e  in enumerate(Rei01_Path):
        for Rei01_x in range(1,64):
            if Rei01_e[Rei01_Int] != '\\':
                Rei01_Path[Rei01_i] = Rei01_Path[Rei01_i][:-1]
                Rei01_Int = Rei01_Int - 1
                Rei01_GetPath = str(Rei01_Path[Rei01_i])
        return Rei01_GetPath
# 输出结果保存在Rei01_GetFilePath()
# 要只需要用任意变量=Rei01_GetFilePath()即可，如：
# abc = Rei01_GetFilePath()
# print(abc)