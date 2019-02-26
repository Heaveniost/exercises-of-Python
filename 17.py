import xlrd
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree


wb = xlrd.open_workbook('./Docs/student.xls')
sh = wb.sheet_by_index(0)

data = dict()
for rx in range(sh.nrows):
    row = sh.row(rx)
    # [text:'2', text:'李四', number:90.0, number:99.0, number:95.0]
    value_list = list()
    key = row[0].value
    for i in row[1:]:
        value = i.value
        value_list.append(value)

    data[key] = value_list
print(data)

root = Element('root')
comment = Comment('学生信息表"id" : [名字, 数学, 语文, 英文]')
root.append(comment)
child = SubElement(root, 'students')
child.text = str(data)
tree = ElementTree(root)
tree.write('./Docs/student.xml', encoding='utf8')