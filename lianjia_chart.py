#!/usr/bin/env python3
# -*- coding: utf-8 -*-python
from pymongo import MongoClient
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

n = 12
X = np.arange(n)
XX=[{'_id': '东方豪园(别墅)', 'avg_unitPrice': 50330.0, 'num': 2}, {'_id': '保利天鹅语(别墅)', 'avg_unitPrice': 48226.0, 'num': 1}, {'_id': '嘉宝紫提湾(别墅)', 'avg_unitPrice': 47772.0, 'num': 2}, {'_id': '领峰华庭', 'avg_unitPrice': 43730.0, 'num': 1}, {'_id': '好世皇马苑', 'avg_unitPrice': 43663.57142857143, 'num': 14}, {'_id': '保利家园(别墅)', 'avg_unitPrice': 43628.8, 'num': 5}, {'_id':\
'绿地颐景嘉园', 'avg_unitPrice': 42355.57142857143, 'num': 7}, {'_id': '绿地秋霞坊(公寓)', 'avg_unitPrice': 41390.933333333334, 'num': 15}, {'_id': '恒大御景湾', 'avg_unitPrice': 41063.0, 'num': 2}, {'_id': '保利星海屿', 'avg_unitPrice': 40963.833333333336, 'num': 12}, {'_id': '骏丰玲珑坊', 'avg_unitPrice': 40907.75, 'num': 4}, {'_id': '嘉宝梦之缘景庭', 'avg_unitPrice': 40533.125, 'num': 8}, {'_id': '佳兆业壹号', 'avg_unitPrice': 40262.72222222222, 'num': 18}, {'_id': '新城香溢璟庭(一期)', 'avg_unitPrice': 40179.833333333336, 'num': 12}, {'_id': '安高东方御府', 'avg_unitPrice': 39783.75, 'num': 4}, {'_id': '嘉宝紫提湾(公寓)', 'avg_unitPrice': 39783.666666666664, 'num': 15}, {'_id': '旭辉华庭', 'avg_unitPrice': 39649.5, 'num': 8}, {'_id': '龙湖郦城', 'avg_unitPrice': 39587.913043478264, 'num': 23}, {'_id': '新城香溢澜庭', 'avg_unitPrice': 39465.666666666664, 'num': 6}, {'_id': '常发豪庭国际', 'avg_unitPrice': 39151.27272727273, 'num': 11}, {'_id': '新城金郡', 'avg_unitPrice': 39069.166666666664, 'num': 54}, {'_id': '龙湖蔚澜香醍', 'avg_unitPrice': 39064.0, 'num': 9}, {'_id': '中信泰富又一城', 'avg_unitPrice': 38784.26666666667, 'num': 15}, {'_id': '绿地远香湖1号', 'avg_unitPrice': 38589.0, 'num': 1}, {'_id': '东方豪园(公寓)', 'avg_unitPrice': 38229.5, 'num': 4}, {'_id': '臻品嘉园(公寓)', 'avg_unitPrice': 38193.833333333336, 'num': 6}, {'_id': '保利天\
鹅语(公寓)', 'avg_unitPrice': 37938.46666666667, 'num': 15}, {'_id': '盘古天地', 'avg_unitPrice': 37926.06896551724, 'num': 29}, {'_id': '白银时代', 'avg_unitPrice': 37821.5, 'num': 2}, {'_id': '\
远香舫新苑', 'avg_unitPrice': 37549.25, 'num': 4}, {'_id': '新城香溢璟庭(二期)', 'avg_unitPrice': 37500.0, 'num': 1}, {'_id': '阳光城新界', 'avg_unitPrice': 37445.2, 'num': 5}, {'_id': '上实海上荟(公寓)', 'avg_unitPrice': 37426.0, 'num': 1}, {'_id': '风荷丽景尚城', 'avg_unitPrice': 37067.4, 'num': 10}, {'_id': '保利家园(公寓)', 'avg_unitPrice': 36883.75, 'num': 24}, {'_id': '保利天琴宇舍', 'avg_unitPrice': 36739.666666666664, 'num': 3}, {'_id': '保利湖畔阳光苑', 'avg_unitPrice': 35643.65625, 'num': 32}, {'_id': '盘古嘉德', 'avg_unitPrice': 35298.666666666664, 'num': 3}, {'_id': '远香舫嘉苑', 'avg_unitPrice': 31581.75, 'num': 8}, {'_id': '马陆清水湾', 'avg_unitPrice': 31161.9, 'num': 10}, {'_id': '马陆街130弄', 'avg_unitPrice': 31146.0, 'num': 1}, {'_id': '远香舫庭苑', 'avg_unitPrice': 30207.0, 'num': 1}, {'_id': '马陆街248弄', 'avg_unitPrice': 29218.5, 'num': 2}, {'_id': '樱花小区', 'avg_unitPrice': 28750.5, 'num': 2}, {'_id': '育兰二村', 'avg_unitPrice': 28386.166666666668, 'num': 6}, {'_id': '荷花新村', 'avg_unitPrice': 27681.0, 'num': 1}, {'_id': '绿地秋霞坊(别墅)', 'avg_unitPrice': 27286.0, 'num': 1}, {'_id': '龙湖蓝湖郡(别墅)', 'avg_unitPrice': 27242.285714285714, 'num': 7}, {'_id': '育兰社区', 'avg_unitPrice': 26610.0, 'num': 1}, {'_id': '马陆街220弄', 'avg_unitPrice': 26495.0, 'num': 1}, {'_id': '育兰支路20弄', 'avg_unitPrice': 26310.0, 'num': 1}]
# print(X)



#b=[x[0] for x in a]
conn = MongoClient('127.0.0.1', 27017)
db = conn.HouseDB  # 连接mydb数据库，没有则自动创建
my_set = db.sell_house_jiadingxincheng  # 使用test_set集合，没有则自动创建

pipeline = [
     {"$group": {"_id": "$village", "avg_unitPrice": {"$avg": "$unitPrice"}, "num": {"$sum": 1}}},
     {"$sort": {"avg_unitPrice": -1}}
]

dataList = list(my_set.aggregate(pipeline))
# print(ll)

houseName =[x["_id"] for x in dataList][0:50]
housePrice =[x["avg_unitPrice"] for x in dataList][0:50]
houseNum =[x["num"] for x in dataList][0:50]
# print(b)

fig, ax = plt.subplots()  
#coding:utf-8
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#有中文出现的情况，需要u'内容'
# error = np.random.rand(20)
plt.barh(houseName, housePrice)
# plt.xticks(rotation=-45,fontsize = 8,ha='left')
plt.tight_layout()

for i, v in enumerate(housePrice):
    print(i)
    print(v)
    ax.text(v + 10, i  -0.2, "%s(%s套)" % (int(v),houseNum[i]), color='blue', fontweight='bold')

# for xy in zip(b, c):  
    # print(xy)
    # plt.annotate("%s" % int(xy[1]), xy=xy, xytext=(-10, 10), textcoords='offset points')  


plt.title('嘉定新城二手房Top50(数据来源:链家网2018.5)')
# plt.xlabel('小区')
plt.xlabel('均价(万)')
plt.show()

