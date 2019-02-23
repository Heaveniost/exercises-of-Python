# coding=utf-8

import os, json, xlwt 

def a():
	with open('txt', 'r') as f:
		content = f.read
	d = json.loads(content)
	file = xlwt.Workbook()
	table = file.add_sheet('test')
	for row, i in enumerate(list(d)):
		table.write(row, 0, i)
		for col, j in enumerate(d[i]):
			table.write(row, col+1, j)
	file.save('./Docs/student.xls')

if __name__ == '__main__':
	a()