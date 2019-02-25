import xlrd
from xml.etree.cElementTree import Element, ElementTree, SubElement, Comment

wb = xlrd.open_workbook('./Docs/numbers.xls')
ws = wb.sheet_by_index(0)
content = list()
for xr in range(ws.nrows):
    row = ws.row(xr)
    num_list = list()
    for i in row:
        value = i.value
        num_list.append(value)
    content.append(num_list)
print(content)

root = Element('root')
comment = Comment('数字信息')
root.append(comment)
child = SubElement(root, 'numbers')
child.text = str(content)
tree = ElementTree(root)
tree.write('./Docs/numbers.xml', encoding='utf8')