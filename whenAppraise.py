import requests


def pingjia(num,q):
    url = 'http://hcp.sczwfw.gov.cn/app/api/evaluationFileHandler'
    headers ={'Accept':'application/json, text/plain, */*',
    'Host':'hcp.sczwfw.gov.cn',
    'Origin':'http://hcp.sczwfw.gov.cn',
    'Referer': 'http://hcp.sczwfw.gov.cn/appEval/index.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

    files = {'content':(None,'{"anonymous":1,"busiCode":"'+num+'","evalChannel":"3","evalSource":"2","objType":"2","evaluationChildren":[],"instructions":"","objCode":"code-001","praise":[],"publish":1,"score":5,"maxBadClassifyFlag":""}')}

    r = requests.post(url, files=files)

    print("开始评价"+r.text)
    print("\n")
    q.put(f"开始评价：{r.text}\n\n")


def run(q, numOfthink, key):
    url = 'http://59.225.201.162:8086/api/approval/dth/affair-expand/zongHe/selectAffairList'
    data = '{"affairName":null,"beginTime":"","bizStatus":"","endTime":"","deptCode":"","bigBizStatus":"91","sfpj":"0","page":'+str(1)+',"rows":'+str(numOfthink)+'}'
    headers ={
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate',
    'Connection':'keep-alive',
    'Content-Type':'application/json;charset=UTF-8',
    'Authorization': key,
    'Host':'59.225.201.162:8086',
    'Origin':'http://59.225.201.162:8086',
    'Referer':'http://59.225.201.162:8086/ch_query',
    'Content-Length': '359',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    r = requests.post(url, headers=headers,data=data)
    data = r.json()['data']['records']
    a = 1
    for i in data:
        print("第几条了？",a)
        q.put(f"开始评价第{a}条")
        print("编号："+i['affairCode']+"，姓名："+i['applicantName'])
        q.put(f"编号：{i['affairCode']}，姓名：{i['applicantName']}\n")
        pingjia(i['affairCode'],q)
        a += 1

