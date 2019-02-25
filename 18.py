import xlrd
from xml.etree.cElementTree import Element, ElementTree, Comment, SubElement

wb = xlrd.open_workbook('./Docs/city.xls')
ws = wb.sheet_by_index(0)
data = dict()
for rx in range(ws.nrows):
    row = ws.row(rx)
    key = row[0].value
    value = row[1].value
    data[key] = value

root = Element('root')
comment = Comment('城市信息')
root.append(comment)
child = SubElement(root, 'citys')
child.text = str(data)
tree = ElementTree(root)
tree.write('./Docs/city.xml', encoding='utf8')