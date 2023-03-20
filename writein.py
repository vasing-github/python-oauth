import asyncio

import requests
import time
import conf
import tools

writeNum = 0
Authorization=''

def input_zwsj(q):
    '''
    第一步获取id 和 affaricode
    '''

    url = 'http://59.225.201.162:8086/api/approval/dth/affair/createAffair?eventCode=51201401800006-511923000000-000-12513723452465052E-1-00&sysLabel=911555276011371'

    headers ={
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': Authorization,
    'Connection': 'keep-alive',
    'Host': '59.225.201.162:8086',
    'Referer': 'http://59.225.201.162:8086/medium_search',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    #print(response.text)
    aff = response.json()['data']['affair']
    id = aff['id']
    affairCode = aff['affairCode']
    applyDate = aff['applyDate']
    createTime = aff['createTime']
    updateTime = aff['updateTime']
    print("第一步创建的id:"+id+"，affcode:"+affairCode+",applydate:"+applyDate+",createTime:"+createTime+",updatetime:"+updateTime)
    q.put("第一步创建的id:"+id+"，affcode:"+affairCode+"\n")
    q.put("休眠13秒\n")
    time.sleep(13)


    '''
    第二步受理材料确认
    载荷数据  json
    表单数据  字典
    '''

    url = 'http://59.225.201.162:8086/api/approval/dth/affair-material/auditResultAll?id='+id
    headers ={
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': Authorization,
    'Connection': 'keep-alive',
    'Host': '59.225.201.162:8086',
    'Referer': 'http://59.225.201.162:8086/medium',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    print("第二步受理材料确认："+response.text)
    q.put( "第二步受理材料确认："+response.text+'\n')
    time.sleep(2)
    '''
    第三步验证
    载荷数据  json
    表单数据  字典
    '''

    url = 'http://59.225.201.162:8086/api/approval/wf/proc-definition/verification-definition'
    data = '{"busiCode":"51201401800006-511923000000-000-12513723452465052E-1-00"}'
    headers ={
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': Authorization,
    'Connection': 'keep-alive',
    'Content-Length': '70',
    'Content-Type': 'application/json;charset=UTF-8',
    'Host': '59.225.201.162:8086',
    'Origin': 'http://59.225.201.162:8086',
    'Referer': 'http://59.225.201.162:8086/medium',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    response = requests.post(url,headers=headers,data=data)
    print("第三步验证："+response.text)
    q.put("第三步验证："+response.text+'\n')

    '''
    第4步提交数据
    '''

    card,name = tools.randExcel()
    sex = str(tools.get_sex(card))

    strid = str(id)
    applicantName = name
    legalPerson = name
    applicantIdCard = card
    legalpersonIdCard =card
    applicantPhone = "13545124578"
    year = 2022


    data = '{"affair":{"id":"'+strid+'","page":1,"rows":10,"limit":10,"start":0,"affairCode":"'+affairCode+'","affairName":"个人参保证明查询打印","applyType":"0","busiType":"1","isParallel":null,"isMultilevel":"0","implListId":"4322529724914106368","eventCode":"51201401800006-511923000000-000-12513723452465052E-1-00","eventName":"个人参保证明查询打印","eventType":"20","appoveTimeLimit":"1","legalTimeLimit":1,"promiseTimeLimit":1,"daysType":"1","onlineType":"2","acceptTime":null,"acceptDeptId":4157479408904773600,"acceptDeptCode":"4157479408904773632","acceptDeptName":"平昌县社会保险事业管理局","status":"-1","nodeStatus":null,"bizStatus":"01","wfTemplateId":"4157514719190253568","wfTemplateKey":"process20210514131911941_4157514719181864960","wfTemplateName":"process20210514131911941_4157514719181864960","wfTemplateVersion":null,"wfInstanceId":null,"createDeptId":4157479408904773600,"createDeptCode":"4157479408904773632","createDeptName":"平昌县社会保险事业管理局","implDeptId":0,"implDeptCode":"4157479408904773632","implDeptName":"平昌县社会保险事业管理局","implAreaCode":"511923000000","seriesNumber":"'+strid+'","applicantType":"2","applyDate":"'+applyDate+'","cardType":"111","applicantName":"'+applicantName+'","applicantSex":"'+sex+'","applicantIdCard":"'+applicantIdCard+'","applicantPhone":"15412457845","applicantEmail":null,"applicantAddress":null,"applicantPostalCode":null,"legalPerson":"'+legalPerson+'","applicantPhotoId":null,"contactName":null,"contactSex":null,"contactIdCard":null,"contactPhone":null,"contactEmail":null,"contractAddress":null,"contractPostalCode":null,"contractPhotoId":null,"remark":null,"isCharge":"0","isMaterial":"1","isResult":"0","isSpecial":"0","isSynergy":"0","isEleform":"0","isPickup":"0","materialAudit":null,"materialCheck":null,"deliveryType":null,"pickupType":"1","pickupStatus":"83","creatorId":29928,"creatorName":"吴晓龙","createTime":"'+createTime+'","updateTime":"'+updateTime+'","shardKey":"5119","year":2022,"deleteFlag":"0","performDeptCode":"4157479408904773632","tripleReviewLevelCode":null,"tripleReviewLevelName":null,"isJointTrail":null,"isThread":null,"jointTrailCode":null,"affairParallelName":null,"affairParallelCode":null,"affairIdList":null,"applyNum":1,"deadlineForBzbq":null,"due":null,"totalDue":null,"applicantPostalAddress":null,"explains":null,"endUserId":null,"endDateTime":null,"endUserName":null,"endOpinion":null,"legalpersonIdCard":"'+legalpersonIdCard+'","licenseStartTime":null,"licenseEndTime":null,"licenseType":null,"licenseDocumentsCode":null,"licenseDocumentsNeme":null,"licenseCertificateCode":null,"licenseCertificateNeme":null,"licenseRemark":null,"decisionRemark":null,"sysCode":"zwfw","legalPersonCardType":"111","contactCardType":null,"materialVersion":"1","careerFormCode":null,"orgName":null,"orgAddress":null,"appoveObject":"2","handleType":null,"sysSource":null,"topicInfo":null,"projectInfo":null,"eleFormUrl":null,"orgCardType":null,"orgIdCard":null,"isFire":null,"isSign":"0","businessType":null,"sendMesgFlag":"1","fgProjectInfo":null,"pretrialResult":"0"},"affariLogistical":{}}'

    url = 'http://59.225.201.162:8086/api/approval/dth/affair/storageAffair'
    # 先转成Json字符串
    # data = json.dumps(data)

    # 按照utf-8编码成字节码
    data = data.encode("utf-8")
    headers ={
    'Accept': 'application/json, text/plain, */*',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': Authorization,
    'Connection': 'keep-alive',
    'Content-Length': '3172',
    'Content-Type': 'application/json;charset=UTF-8',
    'Host': '59.225.201.162:8086',
    'Origin': 'http://59.225.201.162:8086',
    'Referer': 'http://59.225.201.162:8086/medium',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    response = requests.post(url,headers=headers,data=data)
    code = response.json()['code']
    success = response.json()['success']

    print("第四步提交数据,code:",code,"success:",success)
    q.put(f"第四步提交数据,code:{code}\n")

    '''
    第五步受理通知书
    '''

    url = 'http://59.225.201.162:8086/api/approval/dth/affair/submitAffair'
    data = '{"affairId":"'+strid+'","shardKey":"5119","handleType":"1","auditAdvice":"1"}'
    headers ={
    'Accept': 'application/json, text/plain, */*',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': Authorization,
    'Connection': 'keep-alive',
    'Content-Length': '87',
    'Content-Type': 'application/json;charset=UTF-8',
    'Host': '59.225.201.162:8086',
    'Origin': 'http://59.225.201.162:8086',
    'Referer': 'http://59.225.201.162:8086/medium',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    response = requests.post(url, headers=headers, data=data)
    print(response.json())
    code = response.json()['code']
    success = response.json()['success']

    print("第五步受理通知书,code:", code,"success:",success)
    q.put(f"第五步受理通知书,code:{code}\n\n")
    print("\n")


def run(q,num,key):
    i = 1
    j = 0

    global Authorization,writeNum
    Authorization = key
    writeNum = int(num)
    while i <= writeNum :
        print(f"本次运行共需录入{writeNum}条，正在录第{i}条数据")
        q.put(f"本次运行共需录入{writeNum}条，正在录第{i}条数据\n")
        try:
            input_zwsj(q)
        except Exception as e:
            j += 1
            print('错了几个？', j)
            q.put('错了几个？', j)
        i += 1



def printSomething(i):
    print("Hey whatsup bro, i am doing something very interesting.",i)
    # trigger the custom event on root window object
    root.event_generate("<Print>")
    root.update()