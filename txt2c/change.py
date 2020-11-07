from txt import TxT
from word import Word
import os
'''change.py和txt.py两个文件放在一个文件夹下(可以直接使用txt2c这个总文件夹)，并
   在同一个文件夹下创建两个子文件夹，这两个子文件夹分别命名为origin和result，字面
   意思，把源.txt和.c文件放到origin文件夹下，编译运行change，就可以在result文件
   夹下得到结果，路径可以任选。
'''

if __name__ == '__main__':
    origin=os.getcwd() + '\\origin'      #在这改路径
    result=os.getcwd() + '\\result'      #修改与上面一样

    Word(origin).convert()         #先把word文档转换成txt存在原来目录下
    test=TxT(origin,result)        #然后将所有原目录下的txt文本全部复制到目的目录下并转为.c文件
    try:
        test.copy()
    except BaseException as e:
        #若出现这条信息，则检查一下是否占用了origin或result文件夹。若是则关闭它们，否则用管理员身份运行change.py，
        #或者把总文件夹放到非系统盘中
        print('复制文件失败:',e)    
    else:
        print('copy down')
        test.change_encoding()
        test.change_namesuffix()