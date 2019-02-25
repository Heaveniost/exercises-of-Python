# coding=utf-8

import xlrd, re
import time


def cal(s):
    if '时' in s:
        m = re.match(r'(.+)时(.+)分(.+)秒', s)
        seconds = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
    elif '分' in s:
        m = re.match(r'(.+)分(.+)秒', s)
        seconds = int(m.group(1)) * 60 + int(m.group(2)) 
    else:
        m = re.match(r'(.+)秒', s)
        seconds = int(m.group(1))
    return seconds 

def cal2(s):
    k = s // 3600
    v = (s % 3600) // 60
    z = s - 3600 * k - 60 * v 
    return k,v,z

def run():
    # 存放文件的路径
    filepath = '/Users/Heaven/hh3/test/exercises/Docs/语音通信.xls'
    # 打开表格
    xls = xlrd.open_workbook(filepath)
    sheet = xls.sheet_by_index(0)
    ini_call = 0
    pas_call = 0
    # 遍历表格，查到类型为被叫或主叫的行，记录通话时长
    for i in range(1, sheet.nrows):
        row = sheet.row(i)
        if row[4].value == u'被叫':
            pas_time = row[3].value
            pas_call += cal(pas_time)
        else:
            ini_time = row[3].value
            ini_call += cal(ini_time)
    total_call = pas_call + ini_call
    print('主叫时长：%3d小时%02d分钟%02d秒 ' % (cal2(ini_call)))
    print('被叫时长：%3d小时%02d分钟%02d秒 ' % (cal2(pas_call)))
    print('通话总长：%3d小时%02d分钟%02d秒 ' % (cal2(total_call)))

if __name__ == '__main__':
    run()