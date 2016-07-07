# -*- coding: utf-8 -*-
import requests

url = "http://123.206.68.31/api/api_BuyItem3.aspx"

s = requests.Session()

headers = {
    "Content-Type": "application/x-www-form-urlencoded;",
    "charset": "utf-8",
    "Host"  : "123.206.68.31",
    "Content-Length" : 65
}

"""
# 向仓库存一把全新沙漠
s_id=1175&s_key=-1423155737&CharID=3639&op=10&v1=0&v2=8&v3=2

# 登陆
POST /api/api_LoginSessionPoller.aspx HTTP/1.1..Content-Type: application/x-www-form-urlencoded;... charset="utf-8"..Host: 103.41.55.244..Content-Length: 25....s_id=1175&s_key=852311736

POST /api/api_GetShop2.aspx HTTP/1.1..Content-Type: application/x-www-form-urlencoded;... charset="utf-8"..Host: 103.41.55.244..Content-Length: 25....s_id=1175&s_key=852311736

POST /api/api_GPConvert.aspx HTTP/1.1..Content-Type: application/x-www-form-urlencoded;... charset="utf-8"..Host: 103.41.55.244..Content-Length: 36....s_id=1175&s_key=852311736&func=rates

POST /api/api_GetItemsInfo.aspx HTTP/1.1..Content-Type: application/x-www-form-urlencoded;... charset="utf-8"..Host: 103.41.55.244..Content-Length: 25....s_id=1175&s_key=852311736

POST /api/api_GetProfile1.aspx HTTP/1.1..Content-Type: application/x-www-form-urlencoded;... charset="utf-8"..Host: 103.41.55.244..Content-Length: 25....s_id=1175&s_key=852311736u
"""

"""
取沙漠到5格
84 DD 01 00 60 00 E8 EC 01 00 E5 01 00 00 86 37 04 00 8A 4F 2A 00 00 00 00 00 FF 01 00 00 00 00 00 00 00 00 00 61 8B 01 00 01 00
84 3D 02 00 60 00 E8 21 02 00 01 02 00 00 86 37 04 00 8A 4F 2A 00 00 00 00 00 FF 01 00 00 00 00 00 00 00 00 00 61 8B 01 00 01 00
取物品到第6格
84 90 03 00 60 00 E8 12 03 00 C4 02 00 00 86 37 04 00 78 17 2D 00 00 00 00 00 FF 01 00 00 00 00 00 00 00 00 00 D3 8B 01 00 01 00
84 B6 03 00 60 00 E8 27 03 00 D2 02 00 00 86 37 04 00 7C 47 2A 00 00 00 00 00 FF 01 00 00 00 00 00 00 00 00 00 C7 8A 01 00 01 00
取AUG到6格子
84 DC 03 00 60 00 E8 3C 03 00 E0 02 00 00 86 37 04 00 94 91 2B 00 00 00 00 00 FF 01 00 00 00 00 00 00 00 00 00 CE 8A 01 00 01 00
取全新沙漠到6格
84 7F 02 00 60 00 E8 42 02 00 16 02 00 00 86 37 04 00 F1 D4 2D 00 00 00 00 00 FF 01 00 00 00 00 00 00 00 00 00 61 8B 01 00 01 00
取全新沙漠到7格
84 27 04 00 60 00 E8 61 03 00 F6 02 00 00 86 37 04 00 58 D6 2D 00 00 00 00 00 FF 01 00 00 00 00 00 00 00 00 00 61 8B 01 00 01 00
84 7D 04 00 60 00 E8 8D 03 00 12 03 00 00 86 37 04 00 58 D6 2D 00 00 00 00 00 FF 01 00 00 00 00 00 00 00 00 00 61 8B 01 00 01 00
取另一把沙漠
84 36 0E 00 60 00 E8 E6 0C 00 1C 0C 00 00 86 37 04 00 65 5C 26 00 00 00 00 00 FF 01 00 00 00 00 00 00 00 00 00 61 8B 01 00 01 00

取沙漠多次
84 67 0E 00 60 00 E8 FF 0C 00 2B 0C 00 00 86 37 04 00 65 5C 26 00 00 00 00 00 FF 01 00 00 00 00 00 00 00 00 00 61 8B 01 00 01 00
84 6C 0E 00 60 00 E8 03 0D 00 2F 0C 00 00 86 37 04 00 65 5C 26 00 00 00 00 00 FF 01 00 00 00 00 00 00 00 00 00 61 8B 01 00 01 00

？？？
84 7E 04 00 60 00 E8 8E 03 00 13 03 00 00 86 81 00 00 F0 82 D7 46 D6 1F EA BD 00 00 00 00 DD 97 8F 41 00 00 00 00 00 C8 4D 52 D6

存沙漠
84 21 02 00 60 00 78 11 02 00 F8 01 00 00 86 38 04 00 02 01 00 00 00 61 8B 01 00 01 00

移动物品位置
84 C5 02 00 60 00 30 65 02 00 2C 02 00 00 86 2D 04 00 03 0C

站立不动
发送包：

接收

捡东西
84 3B 16 00 60 00 58 E7 18 00 DE 18 00 00 86 70 04 00 4F 99 51 3E 44 00 00 60 00 E0 E8 18 00 DF 18 00 00 86 71 04 00 65 09 A0 45 01 9F 37 43 03 93 EA 45 B6 F4 44 3F F2 48 23 BF 9C 3C 11 3D

"""

"""
批量购买防爆盾
"""
# data = {
#     "s_id" : 1175,
#     "s_key" : 161469790,
#     "ItemID": 101318,
#     "BuyIdx": 8,
#     "Qty"   : -10,
# }
# ItemID 500gc: 100996
#       防爆盾：101318

item = {
    "aa" : 100996,  #
    "Beiyue60" : 400010,
    "Beiyue45" : 400015,
    "svd_bullets" : 400048,
    "dx" : 101262,
    "wooden_shield" : 101317
}

data = {
    "s_id" : 1175,
    "s_key" : -940817711,
    "ItemID": 400015,
    "BuyIdx": 8,
    "Qty"   : 500,
}

# url_gp_convert = "http://123.206.68.31/api/api_GPConvert.aspx"
# data_gp_convert = {
#     "s_id" : 1593,
#     "s_key" : 3391408,
#     "func" : "convert",
#     "GP" : -100
# }
# headers_gp_convert = {
#     "Content-Type": "application/x-www-form-urlencoded;",
#     "charset": "utf-8",
#     "Host"  : "123.206.68.31",
#     "Content-Length" : 45,
# }
"""
批量购买dx
"""
# data = {
#     "s_id" : 1175,
#     "s_key" : 435602464,
#     "ItemID": 101318,
#     "BuyIdx": 8,
#     "Qty"   : 20,
# }
#
# url_api_GetItemsInfo = "http://103.41.55.244/api/api_GetItemsInfo.aspx"
# data_api_GetItemsInfo = {
#     "s_id": 1175,
#     "s_key": 852311736
# }
url_mysterybox = "http://123.206.68.31/api/api_Mysterybox.aspx"
data_mysterybox = {
    "s_id" : 1593,
    "s_key": 1341860170,
    "func" : "roll",
    "ItemID": 301150,
    "BuyIdx": 4,
    "Qty" : 1
}
headers_mysterybox = {
    "Content-Type": "application/x-www-form-urlencoded;",
    "charset": "utf-8",
    "Host"  : "123.206.68.31",
    "Content-Length" : 66,
}

"""
学习技能
"""


# res = s.post(url, data=data, headers = headers)
# res = s.post(url = url_mysterybox, data = data_mysterybox, headers = headers_mysterybox)
# res = s.post( url_gp_convert, data = data_gp_convert, headers = headers_gp_convert )
pwd_headers = {
    "Accept"    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    # "Accept-Language":"zh-CN,zh;q=0.8",
    "Cache-Control":"max-age=0",
    "Content-Length":"85",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie":"PHPSESSID=8u414sfvls08m6adjiggpfkk06",
    "Host":"www.infestationmmo.com.cn",
    "Origin":"http://www.infestationmmo.com.cn",
    "Proxy-Connection":"keep-alive",
    "Referer":"http://www.infestationmmo.com.cn/password_edit.php",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"
}
res = s.post( url = "http://www.infestationmmo.com.cn/password_edit.php", data = { "act" : "save", "password" : "emptyset110", "new_password": "emptyset110.", "confirm_password":"emptyset110." }, headers = pwd_headers )
print( type(res.text) )
s = res.text
# s.decode('gbk','ignore')
print( s )
