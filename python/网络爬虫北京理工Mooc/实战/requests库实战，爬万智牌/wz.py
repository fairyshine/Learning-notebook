import requests
kv = {"user-agent":"Mozilla/5.0"}
for i in range(392):
    num=i+1
    path = "wz\\"+str(num)+".png"
    url = "http://wspic.iyingdi.cn/card/magic/series/ELD/card/"+str(num)+".png"
    r = requests.get(url,headers=kv)
    print(r.status_code)
    with open(path,'wb') as f:
        f.write(r.content)
        f.close()
    