import os, json, xlwt 

def a():
	with open('./Docs/city.txt', 'r') as f:
		content = f.read()
	data = json.loads(content)
	file = xlwt.Workbook()
	table = file.add_sheet('test')
	for row, i in enumerate(list(data)):
		table.write(row, 0, i)
		table.write(row, 1, data[i])
	file.save('./Docs/city.xls')

if __name__ == '__main__':
	a()