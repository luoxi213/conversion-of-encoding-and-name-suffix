from win32com.client import Dispatch, constants
import glob
import os

class Word(object):
	def __init__(self,path):
		#获取需要转换的word文档的目录
		self.__path=path

	def convert_to_text(self,wordapp, wordfile):
		name, ext = os.path.splitext(wordfile)     #分离word文件名和后缀名
		txtfile = name + '.txt'                    #保存为文件名+.txt的格式
		wordapp.Documents.Open(wordfile)      #打开文件 
		wordapp.ActiveDocument.SaveAs(os.path.abspath(txtfile), 3)    #将打开的文件保存为文本文件，第二个参数表示的就是txt的意思
		wordapp.ActiveDocument.Close()           #关闭文件

# 该方法是源目录下所有word文档的生成器，它检索出所有的doc和docx文档
	def next_doc(self):
		for d in glob.glob(self.__path + '/*.doc'):
			yield d
		for d in glob.glob(self.__path + '/*.docx'):
			yield d
 
# 取出每一个word文档，然后调用函数将它生成txt文本
	def convert(self):
		word = Dispatch("kwps.Application")  #这里使用的kwps是金山wps软件，有些使用word也行，但是要确保有word软件      
		for doc in self.next_doc():
			print('converting ' + doc +' to txt')
			try:
				self.convert_to_text(word, doc)        #word转存为txt
				os.remove(doc)        #将成功转化的word文档删除，使文件夹只剩下txt文档
			except BaseException as e:
				print('fail to convert ' + doc + ', please check the reason')
		word.Quit()	   #用完关闭对象

if __name__ == '__main__':
    test = Word(os.getcwd() + '\\origin')
    test.convert()	