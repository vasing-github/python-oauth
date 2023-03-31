import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

def run(q):
    # 创建浏览器对象
    browser = webdriver.Chrome()

    # 进入指定网址
    browser.get("http://59.225.209.96/oauthui/portal")

    # 等待页面加载并找到账号登录框
    username = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, "username")))
    username.send_keys("平昌县社会保险事业管理局")

    password = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys("oauth@12#$")

    # 获取当前窗口句柄
    current_window = browser.current_window_handle

    element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/dl/dt[16]')))
    browser.execute_script('arguments[0].click();', element)
    print('综合受办元素已被点击')
    q.put('综合受办元素已被点击')

    # 获取所有窗口句柄
    all_windows = browser.window_handles

    # 切换到新窗口
    for window in all_windows:
        if window != current_window:
            browser.switch_to.window(window)
            break

    elementbanjian = WebDriverWait(browser, 100).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div/div[2]/ul/li[3]')))
    browser.execute_script('arguments[0].click();', elementbanjian)
    print('办件人员元素已被点击\n')
    q.put('办件人员元素已被点击\n')

    elementzonghe = WebDriverWait(browser, 100).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div/section/aside/div/ul/li[8]/a')))
    browser.execute_script('arguments[0].click();', elementzonghe)
    print('综合查询元素已被点击\n')
    q.put('综合查询元素已被点击\n')
    time.sleep(3)
    elementdaiban = WebDriverWait(browser, 100).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/section/aside/div/ul/li[5]')))
    browser.execute_script('arguments[0].click();', elementdaiban)
    print('代办任务元素已被点击\n')
    q.put('代办任务元素已被点击\n')

    time.sleep(3)

    key = 'pro__Authorization'
    value = browser.execute_script(f'return window.localStorage.getItem("{key}");')
    data = json.loads(value)
    pro_auth_value = data['value']
    print(pro_auth_value)
    q.put(('key', pro_auth_value))
    q.put("\n")
    # 在程序的最后添加一个循环来检查浏览器窗口的状态
    while True:
        try:
            # 尝试获取浏览器窗口的标题
            browser.title
        except WebDriverException:
            # 如果获取失败，说明浏览器窗口已经关闭
            print('Browser window closed')
            break