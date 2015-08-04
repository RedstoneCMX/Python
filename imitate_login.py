# -*- coding: UTF-8 -*-
import urllib,urllib2,cookielib
from bs4 import BeautifulSoup
#登录的主页面
hosturl = "http://grdms.bit.edu.cn/yjs/login.jsp"

posturl = "http://grdms.bit.edu.cn/yjs/login.do"

#设置一个cookie处理器，负责从服务器下载cookie到本地
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
urllib2.install_opener(opener)

#打开登录主页面（他的目的是从页面下载cookie，这样我们在发送post数据时就有cookie了，否则发送不成功）
h = urllib2.urlopen(hosturl)

#构造header，一般header至少要包括两项
headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36',
	'Referer':'http://grdms.bit.edu.cn/yjs/login.jsp'
}

#构造post数据
postData = {
	'loginType':'0',
	'j_username':'2120140994',
	'j_password':'ashuaxin1991',
	'Submit':''
}
#需要给post数据进行编码
postData = urllib.urlencode(postData).encode(encoding = 'GBK')
#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程  
request = urllib2.Request(posturl, postData, headers)  
response = urllib2.urlopen(request)  
text = response.read().decode('GBK')

#再去浏览需要登录的页面

geturl2 = "http://grdms.bit.edu.cn/yjs/yanyuan/py/pychengji.do?method=enterChaxun"
#构造header，一般header至少要包括两项
headers2 = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36',
	'Referer':'http://grdms.bit.edu.cn/yjs/application/page_main.jsp?subsys='
}

request2 = urllib2.Request(url=geturl2, headers=headers2)  
response2 = urllib2.urlopen(request2)  
text2 = response2.read().decode('GBK')
soup = BeautifulSoup(text2)
mymark = soup.find('table',{'class':'tab_1'})
marktr = mymark.find_all('tr')
for onemarktr in marktr:
	marktd = onemarktr.find_all('td')
	for onemarktd in marktd:
		print onemarktd.get_text(),
	print('\n')
#print text2  

