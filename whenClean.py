
import conf
import requests

Authorization = conf.Authorization

def get_list():

    url = 'http://59.225.201.162:8086/api/approval/dth/affair/storageAffairPage'

    data = '{"page":1,"rows":'+str(20)+',"status":0}'
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
    ids = [x['seriesNumber'] for x in records]
    return ids
def dellAffair(busiId,q):
    url = 'http://59.225.201.162:8086/api/approval/dth/affair/del?ids='+busiId

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': Authorization,
        'Cookie': 'route=7e955e553605b1ea9a7034e978d0c40a',
        'Host': '59.225.201.162:8086',
        'Origin': 'http://59.225.201.162:8086',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://59.225.201.162:8086/db_work',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    code = response.json()['code']
    succ = response.json()['success']
    print("code:",code,"succ:",succ,"name:")
    q.put(f"code:{code},succ:{succ}\n\n")


def run(q, key):
    global Authorization
    Authorization =key
    ids = get_list()
    _a = 1
    for each in ids:
        print("star:%d",_a)
        q.put(f"清理开始，第{_a}条\n")
        dellAffair(each,q)
        _a += 1
        print("\n")
    q.put("清理完了，看看还有没有")






