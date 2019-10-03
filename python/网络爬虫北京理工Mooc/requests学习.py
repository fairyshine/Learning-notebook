# In[]
requests库入门
# In[]  
import requests
r=requests.get("http://www.baidu.com")  #get方法

print(r.status_code) #状态码 200成功，404失败
print(type(r))
print(r.headers)

r.encoding="utf-8"  #网页的编码方式
# r.apparent_encoding  备选编码方式
#r.content 响应内容的二进制形式  图片等
print(r.text)  #页面的字符串形式
#status_code,text,encoding,apparent_encoding,content均为Response对象的属性

# In[]  
#ConnectionError,HTTPError,URLRequired,TooManyRedirects,ConnectTimeout,Timeout
#6种异常
#raise_for_status方法
# In[] 通用代码框架
import requests

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"
    
if __name__ =="__main__":
    url="http://www.baidu.com"
    print(getHTMLText(url))

# In[] HTTP协议及requests库方法
#request，get,head,post,put,patch,delete 7个方法
#url  http://host[:port][path]
requests.request(method,url,**kwargs)
#method 请求方式 6种+options
# In[] robots协议
import requests

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"
    
url="http://www.jd.com/robots.txt"
print(getHTMLText(url))    
url="http://www.qq.com/robots.txt"
print(getHTMLText(url)) 

# In[]
import requests
kv = {"user-agent":"Mozilla/5.0"}
url=""
try:
    r = requests.get(url,headers = kv)  
    r.encoding = r.apparent_encoding
    print(r.text)   
except:
    print("爬取失败")    
# In[]  爬图片了
import requests
kv = {"user-agent":"Mozilla/5.0"}
path = "D:\\pypachong\\wz\\1.png"
url = "http://wspic.iyingdi.cn/card/magic/series/ELD/card/1.png"
r = requests.get(url,headers=kv)
print(r.status_code)
with open(path,'wb') as f:
    f.write(r.content)
    f.close()
# In[]

    

