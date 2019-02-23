from bs4 import BeautifulSoup

html_doc = open("/Users/Heaven/hh3/test/exercises/Docs/base.html",'r',encoding='utf-8')



#读取html文件的句柄内容，因为beautifulsoup中的第一个参数是html文件的句柄内容而不是html文件

htmlhandle = html_doc.read()



#使用beautifulsoup解析功能，解析器使用lxml
soup = BeautifulSoup(htmlhandle,'html.parser')
#输出标题
print(soup.title)
#输出p标签的内容
print(soup.p)
#输出a链接
print(soup.a)
#输出body标签的内容也就是正文
print(soup.find_all('body'))
#输出整个html文件
print(soup.get_text)