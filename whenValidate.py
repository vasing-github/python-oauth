
import conf
import requests
import tkinter as tk
Authorization = conf.Authorization
numOfPush = 0
def get_list():

    url = 'http://59.225.201.162:8086/api/approval/wf/task/upcoming'
    data = '{"page":1,"rows":'+str(numOfPush)+',"orderBy":{"updateTime":"desc"},"affairName":null,"likeMap":{},"between":{},"in":{"bizStatus":["21","22","23","24","25","26","27,","28","31","33"]}}'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': Authorization,
        'Content-Length':'168',
        'Content-Type':'application/json;charset=UTF-8',
        'Cookie':'route=7e955e553605b1ea9a7034e978d0c40a',
        'Host':'59.225.201.162:8086',
        'Origin': 'http://59.225.201.162:8086',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://59.225.201.162:8086/db_work',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    response = requests.post(url, headers=headers,data=data)
    records = response.json()['data']['records']
    ids = [x['busiId'] for x in records]
    return ids
def submitAffair(busiId,q):
    url = 'http://59.225.201.162:8086/api/approval/dth/affair/submitAffair'
    data = '{"affairId":"'+busiId+'","shardKey":"5119","handleType":6,"auditAdviceInfo":null,"base64Json":"","auditAdvice":1,"attIds":""}'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': Authorization,
        'Content-Length': '168',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'route=7e955e553605b1ea9a7034e978d0c40a',
        'Host': '59.225.201.162:8086',
        'Origin': 'http://59.225.201.162:8086',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://59.225.201.162:8086/db_work',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    response = requests.post(url, headers=headers, data=data)
    code = response.json()['code']
    succ = response.json()['success']
    name = response.json()['data']['affair']['applicantName']
    print("code:", code, "succ:", succ, "name:", name)
    q.put(f"code:{code},succ:{succ},name:{name}\n\n")

def run(q, num, key,shencha_button):
    global Authorization,  numOfPush
    numOfPush = int(num)
    Authorization =key
    ids = get_list()
    _a = 1
    j = 0
    for each in ids:
        print("star:", _a)
        q.put(f"开始推送：{_a}\n")
        try:
            submitAffair(each,q)
            _a += 1
        except Exception as e:
            j = +1
            print('错了几个？', j)
            q.put(f"错误：{j}\n")
        print("\n")
    shencha_button.config(state=tk.NORMAL)






