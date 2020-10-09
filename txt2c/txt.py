from shutil import copy
import os 
from chardet import detect

class TxT(object):
	def __init__(self,origin,result):
		#获取转移文件的源目录和目的目录,只能利用传入的参数初始化,不能干别的
		self.__origin=origin
		self.__result=result
		
	def copy(self):   #复制文件
		os.chdir(self.__origin)   #移动到源目录
		self.__list_file=[i for i in os.listdir('.') if os.path.isfile(i) and \
			os.path.splitext(i)[1] in ('.c','.txt')]   #获取.c和.txt文件到一个列表中，可以重复使用

		try:
			for item in self.__list_file:
				copy(item,self.__result)   #复制每一个文件到目的目录
		except :
			raise    #文件复制不成功，肯定是路径或权限有问题

	def change_encoding(self):  #修改编码
		os.chdir(self.__result)   #移动到目的目录
		for item in self.__list_file:
			tag=True    #编码为utf-8的标志
			with open(item,'rb') as f:
				enc=detect(f.read())['encoding']   #判断是否是utf-8编码
				if enc!='utf-8':
					tag=False
			if not tag:    #如果上面检测到某个文件不是utf-8编码的话，就转化。方式是先读出来，再用utf-8格式写
				text=''
				with open(item,'r') as f:
					text=f.read()
				with open(item,'w',encoding='utf-8') as f:
					f.write(text)
	
	def change_namesuffix(self):   #修改后缀名
		list_txt=[i for i in self.__list_file if os.path.splitext(i)[1] == '.txt']    #存储所有.txt文件
		for item in list_txt:
			os.rename(item,os.path.splitext(item)[0]+'.c')   #把每个txt文件重组成名字+.c后缀的文件
		print('文件转换成功！')