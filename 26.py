'''
	编写函数，能在当前目录以及子目录下查找文件名包含指定字符串的文件，并打印出完整路径
'''

import os, json

def search(a,b,l):
	for x in os.listdir(a):
		path = os.path.join(a,x)
		if os.path.isdir(path):
			search(path,b,l)
		else:
			if os.path.splitext(path)[1] == b:
				l.append(path)
	return l


if __name__ == '__main__':
	l = []
	a = os.path.abspath('.')
	b = '.py'
	print(search(a,b,l))
	try:
		f = open('./Docs/path.txt' ,'a')
		for i in l:
			f.write(i + '\n')
	finally:
		if f:
			f.close()
