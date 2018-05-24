#!/usr/bin/env python3
# -*- coding: utf-8 -*-python
import json
import urllib
from urllib import parse, request
from bs4 import BeautifulSoup
import http.cookiejar
from pymongo import MongoClient

url = "https://sh.lianjia.com/ershoufang/jiadingxincheng/pg"

header_dict = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "Content-Type":
    "",
    "Cookie":
    "lianjia_uuid=4c44c566-acd3-4c96-afd4-226cd40e7508; UM_distinctid=1638bd124a417c-0c3f88ea75963c-6b1b1279-1aeaa0-1638bd124a5695; select_city=310000; all-lj=762328e22710c88ff41f391dedabbc6f; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1527059136; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1527071613; _smt_uid=5b0512bf.2176687a; CNZZDATA1253492439=562411044-1527055815-https%253A%252F%252Fwww.lianjia.com%252F%7C1527066763; CNZZDATA1254525948=682867250-1527056393-https%253A%252F%252Fwww.lianjia.com%252F%7C1527069698; CNZZDATA1255633284=1638755711-1527058203-https%253A%252F%252Fwww.lianjia.com%252F%7C1527070917; CNZZDATA1255604082=441002172-1527054426-https%253A%252F%252Fwww.lianjia.com%252F%7C1527068735; CNZZDATA1256793290=13591002-1527054999-https%253A%252F%252Fwww.lianjia.com%252F%7C1527066588; _ga=GA1.2.1946455734.1527059132; _gid=GA1.2.1949653079.1527059132; lianjia_ssid=03bc2d49-5966-4317-b07f-79c30dd25f0e",
    "Origin":"",
    "Referer":"",
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}

conn = MongoClient('127.0.0.1', 27017)
db = conn.HouseDB  # 连接mydb数据库，没有则自动创建
my_set = db.sell_house_jiadingxincheng  # 使用test_set集合，没有则自动创建
_id = 1
for i in range(15):
    pageUrl = url+str(i+1)
    print("loop:", pageUrl)

    req = request.Request(url=pageUrl, data=None, headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    html = res.decode('utf-8')

    # print(html)

    soup = BeautifulSoup(html, "html.parser")
    resultCount = int(soup.find("div", attrs={'class': 'resultDes'}).find("span").get_text().replace(" ",""))

    sellListContent = soup.find("ul", attrs={'class': 'sellListContent'})
    # print(sellListContent)
    lists = sellListContent.find_all("li")
 
    for item in lists:
        if i > resultCount:
            break

        sellHouseInfo = {}
        houseInfo = item.find("div", attrs={'class': 'houseInfo'})
        sellHouseInfo["_id"] = _id
        sellHouseInfo["village"] = houseInfo.find("a").get_text().rstrip()
       
        sellHouseInfo["totalPrice"] = float(item.find("div", attrs={'class': 'totalPrice'}).get_text().replace("\u4e07",""))
        sellHouseInfo["unitPrice"] = float(item.find("div", attrs={'class': 'unitPrice'}).get_text().replace("\u5355\u4ef7","").replace("\u5143/\u5e73\u7c73",""))
        # sellHouseInfo["area"] = (sellHouseInfo["totalPrice"]/sellHouseInfo["unitPrice"])

        my_set.insert(sellHouseInfo)
        _id = _id + 1
        # print(json.dumps(sellHouseInfo))
        print(_id)