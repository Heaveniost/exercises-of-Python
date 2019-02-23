import os, json, xlwt 

def a():
	with open('./Docs/numbers.txt', 'r') as f:
		content = f.read()
	d = json.loads(content)
	file = xlwt.Workbook()
	table = file.add_sheet('test')
	for row,i in enumerate(list(d)):
		for col,j in enumerate(i):
			table.write(row, col, j)
	file.save('./Docs/numbers.xls')

if __name__ == '__main__':
	a()
