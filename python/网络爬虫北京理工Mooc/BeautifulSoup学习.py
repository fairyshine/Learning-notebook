from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>data</p>','html.parser')
# In[] BS库的基本元素
<p class="title">...</p>
名称  属性

解析器
html.parser
lxml
xml
html5lib

BS类5个基本元素
Tag 标签
Name 标签名字
Atributes 标签属性
Navigating 非属性字符串
Comment 标签内字符串的注释部分


# In[]
from bs4 import BeautifulSoup
import requests
r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup = BeautifulSoup(demo,'html.parser')

# In[]
标签树的下行遍历
.contents
.children
.descendants
上行遍历
.parent
.parents






