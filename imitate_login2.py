# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

url_grade = "http://grdms.bit.edu.cn/yjs/yanyuan/py/pychengji.do?method=enterChaxun"
#构造header，一般header至少要包括两项
headers2 = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36',
	'Referer':'http://grdms.bit.edu.cn/yjs/application/page_main.jsp?subsys='
}

cookies = {
	'JSESSIONID':'65ACEC7CA3108DC3534EF28844422ABB',
	'SECURITY_AUTHENTICATION_COOKIE':'078356ca0dbcef62e1385cdd023dd790',
	'SECURE_AUTH_ROOT_COOKIE':'078356ca0dbcef62e1385cdd023dd790'
}

r2 = requests.get(url_grade,cookies=cookies,headers=headers2)
text2 = r2.text
soup = BeautifulSoup(text2)
mymark = soup.find('table',{'class':'tab_1'})
marktr = mymark.find_all('tr')
for onemarktr in marktr:
	marktd = onemarktr.find_all('td')
	for onemarktd in marktd:
		print onemarktd.get_text(),
	print('\n')
