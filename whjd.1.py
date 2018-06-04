#!/usr/bin/env python3
# -*- coding: utf-8 -*-python
import json
import urllib 
from urllib import parse, request
from bs4 import BeautifulSoup
import time

listUrl = 'http://www.whjd.sh.cn/frontIndex/activityQueryList.do?'\
+'tagId=&activityName=&activityReportingUnit=33ac3be459f34d13ae29a4d6f2959b47&'\
+'page=1&activityLocation=&activityArea=57&chooseType=&bookType=&sortType=8'

header_dict = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "register_captcha=5aWz; JSESSIONID=2FB8DF7A6200E375BD09D6A3C404ECC8-n2; Hm_lvt_eec797acd6a9a249946ec421c96aafeb=1515659008; Hm_lpvt_eec797acd6a9a249946ec421c96aafeb=1515659400; Hm_lvt_522dc691323a30767cdac92bab378b53=1515658996; Hm_lpvt_522dc691323a30767cdac92bab378b53=1515661875",
    "Origin": "http://www.whjd.sh.cn",
    "Referer": "http://www.whjd.sh.cn/frontActivity/frontActivityBook.do?activityId=04a3bccace124ce1af644099ce08a366",
    "Accept": "application/json, text/javascript, */*; q=0.01",
}

req = request.Request(url=listUrl, headers=header_dict)
res = request.urlopen(req)
res = res.read()
# print(res)

jj = json.loads(json.loads(res))
#print(jj['list'][0]['activityStartTime'])

for item in jj['list']:
	print(item['activityStartTime']+' '+item['activityTime'])
	#print(item['activityAddress'])
	#print(item['activityName'])
	now=time.time()
	localtime1=time.mktime(time.strptime(item['activityStartTime'],'%Y-%m-%d'))
	showTime=time.mktime(time.strptime(item['activityStartTime'],'%Y-%m-%d'))
	if showTime<=now and item['activityName']=='非遗亲子课堂之“陶艺时光”陶艺画胚专场':
		# quertString = parse.quote_plus(notifyDict).encode(encoding='utf-8')
		params = urllib.parse.urlencode({'text': item['activityName']
		, 'desp': item['activityAddress']+'Time:'+item['activityStartTime']+'T'+item['activityTime']}) 
		print(params)
		notifyUrl='https://sc.ftqq.com/SCU27040Ta23ffe27503031b9c1124950acd00e455b0971b014986.send?'+params
		req = request.Request(url=notifyUrl ,headers=header_dict)
		res = request.urlopen(req)
		res = res.read()
		print(res)
		

		
		



'''url = "http://www.whjd.sh.cn/frontActivity/checkFrontActivityBook.do"
quertString = "seatInfo=&maintananceInfo=&vipInfo=&activityId=04a3bccace124ce1af644099ce08a366&selectSeatInfo=&eventId=&eventDateTime=&canNotEventStrs=2018-01-07&maxColumn=&orderPhoneNo=13671514268&bookCount=1"
# quertString = "tagId=&activityName=&activityReportingUnit=33ac3be459f34d13ae29a4d6f2959b47&page=1&activityLocation=&activityArea=57&chooseType=&bookType=&sortType="
# json串数据使用
# textmod = json.dumps(textmod).encode(encoding='utf-8')
# 普通数据使用
quertString = parse.quote_plus(quertString).encode(encoding='utf-8')
#print(quertString)

# url = "http://www.whjd.sh.cn/frontIndex/activityQueryList.do"

req = request.Request(url=url, data=quertString, headers=header_dict)
res = request.urlopen(req)
res = res.read()
print(res)

jj = json.loads(json.loads(res))
print(type(jj))
print(jj)'''
