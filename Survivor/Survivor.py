import requests

class Player():
    def __init__( self, ip = "103.41.55.244", username = None, password = None, proxies = None ):
        self.ip = ip
        self.base_url = "http://" + self.ip
        self.session = requests.Session()
        self.is_login = False
        self.proxies = proxies

    def get_proxy(self):
        return self.proxies

    def random_mac(self):
        """
        生成随机mac地址
        """
        import random
        mac_list = []
        for i in range(1,7):
            rand_str = "".join(random.sample("0123456789abcdef",2))
            mac_list.append(rand_str)
        mac_addr = ":".join(mac_list)
        return mac_addr

    def get_headers(self, content_length = None):
        """
        生成请求头部
        """
        if content_length is None:
            return {
                "Content-Type": "application/x-www-form-urlencoded;",
                "charset": "utf-8",
                "Host"  : self.ip,
            }
        else:
            return {
                "Content-Type": "application/x-www-form-urlencoded;",
                "charset": "utf-8",
                "Host"  : self.ip,
                "Content-Length" : content_length
            }

    def get_item( self, name ):
        item_dict = {
            "gc_500" : { "item_id": 100996, "idx": 4 },     # gc棒500，
            "nato_60" : { "item_id": 400010, "idx": 8 },    # 北约60，
            "nato_45" : { "item_id": 400015, "idx": 8 },    # 北约45，
            "nato_30" : { "item_id": 400016, "idx": 8 },    # 北约30
            "nato_100" : { "item_id": 400017, "idx": 4 },   # 北约100
            "dx"    : { "item_id" : 101262, "idx": 8 },     # dx绷带
            "svd_bullets" : {"item_id" : 400048, "idx" : 8 },   #
            "wooden_shield": { "item_id": 101317, "idx": 8  },
            "steel_shield": { "item_id": 101318, "idx": 8 },
            "grenade" : {"item_id": 101310, "idx":8 },
            "ak_100": {"item_id" : 400100, "idx": 8}
        }
        return item_dict[ name ]

    # qty在美刀时候单位是万，在gc时候单位是百
    def cheating( self, ex_type = "dollar", qty = 100 ):
        pass

    def mystery_box( self, item_id = 301150 ):
        url = self.base_url + "/api/api_Mysterybox.aspx"
        headers = self.get_headers( content_length = 66 )
        data_mysterybox = {
            "s_id" : self.id,
            "s_key": self.s_id,
            "func" : "roll",
            "ItemID": item_id,
            "BuyIdx": 4,
            "Qty" : 1
        }
        res = self.session.post( url = url, headers = headers, data = data_mysterybox, proxies = self.get_proxy() )
        if res.text.find( "loot box is empty" ) == -1:
            print( "item_id:{}\t response:{}\n".format( item_id, res.text ) )


    def register( self, username, password, with_gc = False, with_dollar = False ):
        url = self.base_url + "/api/api_AccRegister.aspx"
        headers = self.get_headers( content_length = 75 )
        data = {
            "username"  : username,
            "password"  : password,
            "serial"    : "",
            "email"     : "not@used.anymore"
        }
        res = self.session.post( url = url, data = data, headers = headers, proxies = self.get_proxy()  )
        print( "注册结果：{}".format( res.text ) )
        self.login( username = username, password = password )

    def buy( self, item_name, qty):
        while self.is_login == False:
            print( "你还没有登陆呢 >_<" )
            self.login()

        item = self.get_item( item_name )

        data = {
            "s_id" : self.id,
            "s_key" : self.s_id,
            "ItemID": item[ "item_id" ],
            "BuyIdx": item[ "idx" ],
            "Qty"   : qty,
        }
        url = self.base_url + "/api/api_BuyItem3.aspx"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded;",
            "charset": "utf-8",
            "Host"  : self.ip ,
            "Content-Length" : 65
        }
        res = self.session.post( url= url, data = data, headers = headers, proxies = self.get_proxy() )
        print( res.text )

    def login(self, username = None, password = None):
        """
        登陆接口
            返回：
            True
            False
        """
        if username is None:
            username = input("请输入账号: ")
        if password is None:
            password = input("请输入密码: ")

        url = self.base_url + "/api/api_Login.aspx"
        mac_addr = self.random_mac().upper()
        data = {
            "username"  : username,
            "password"  : password,
            "mac"       : mac_addr
        }
        res = self.session.post( url, proxies = self.get_proxy() ,data = data, headers = self.get_headers() )
        if res.status_code == 200:
            print( "登陆返回信息：{}".format(res.text) )
            result = res.text.split(' ')
            if len( result ) == 3:
                self.s_id = result[1] # Session_id
                self.id = result[0][-4:]
                if result[2] == '100':
                    self.is_login = True
                    print( "登陆成功" )
                    self.username = username
                    self.password = password
                    return True
                else:
                    print( "登录失败" )
                    return False
            else:
                print( "登陆失败，无法识别的返回信息" )
                return False
        else:
            print( res.status_code )

    def auto_login(self, username):
        # 自动登录accounts.json中的帐号
        import json
        import os
        f = open( os.getcwd() + "/" + accounts, 'r' , encoding="utf-8" )
        accounts = json.load( f )
        f.close()
        if username in accounts.keys():
            password = accounts[ "username" ]
            self.is_login = self.login( username = username, password = password )
            if self.is_login == False:
                self.is_login = self.login( username = username, password = username )
            if self.is_login == False:
                print( "{}: 该帐号密码错误，请更新accounts.json".format( username ) )
        else:
            print( "找不到该帐号" )

    def disguise_all(self, accounts = "accounts.json"):
        import json
        import os
        f = open( os.getcwd() + "/" + accounts, 'r' , encoding="utf-8" )
        accounts = json.load( f )
        f.close()
        print(accounts)

    def register_all(self, accounts = "accounts.json"):
        import json
        import os
        import time
        f = open( os.getcwd() + "/" + accounts, 'r' , encoding="utf-8" )
        accounts = json.load( f )
        f.close()
        for username in accounts.keys():
            print( "即将注册:\t{}:\t{}".format( username, accounts[username] ) )
            res = self.register( username = username, password = accounts[username] )
            self.login( username = username, password = accounts[username] )

    # def init_all( self, accounts = "accounts.json" ):
    #     import json
    #     import os
    #     import time
    #     f = open( os.getcwd() + "/" + accounts, 'r' , encoding="utf-8" )
    #     accounts = json.load( f )
    #     f.close()
    #     for username in accounts.keys():
    #         res = self.login( username = username, password = accounts[username] )
    #         print(res)
    #         self.buy( "" )

    def change_pwd(self, pwd = None):
        if pwd is None:
            pwd = self.username
        headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"en-US,en;q=0.8",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Content-Length":76,
            "Content-Type":"application/x-www-form-urlencoded",
            "Host":"www.infestationmmo.com.cn",
            "Origin":"http://www.infestationmmo.com.cn",
            "Upgrade-Insecure-Requests":1,
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
        }
        url = "http://www.infestationmmo.com.cn/forgot_password.php"
        data = {
            "act":"save",
            "CustomerID": self.id,
            "password": pwd,
            "confirm_password": pwd
        }
        res = self.session.post( url, proxies = self.proxies, data = data, headers = headers )
        print( res.text )

    def improve_one(self, username,password = None, accounts = "accounts.json", dx = True, steel_shield = True, nato_30 = True, nato_100 = False, gc_500 = False, ak_100 = True, grenade = True, dollars = True):
        import json
        import os
        import time
        import random
        if password is None:
            f = open( os.getcwd() + "/" + accounts, 'r' , encoding="utf-8" )
            accounts = json.load( f )
            f.close()
            password = accounts[username]
        res = self.login( username = username, password = password )
        if res == True:
            if dollars:
                rand = int(random.random()*1000+100)
                self.buy( "steel_shield", rand*(-1) )
                print( "{} -> 增加美金:{}".format(username, 10000*rand ) )
            if steel_shield:
                rand = int(random.random()*500+100)
                self.buy( "steel_shield", rand*(-1) )
                for i in range( 0, int(rand/20) ):
                    self.buy( "steel_shield", 20 )
                    print( "{} -> 购买100钢盾".format( username ) )
            if nato_30:
                rand = int(random.random()*1000+100)
                self.buy( "nato_30", rand*(-1) )
                for i in range( 0, int(rand/20) ):
                    self.buy( "nato_30", 20 )
                    print( "{} -> 购买20个北约30".format( username ) )
            if ak_100:
                rand = int(random.random()*50+100)
                self.buy( "ak_100", rand*(-1) )
                for i in range( 0, int(rand/20) ):
                    self.buy( "ak_100", 20 )
                    print( "{} -> 购买20个ak弹鼓".format( username ) )
            if grenade:
                rand = int(random.random()*100+100)
                self.buy( "grenade", rand*(-1) )
                for i in range( 0, int(rand/20) ):
                    self.buy( "grenade", 20 )
                    print( "{} -> 购买20个手榴弹".format( username ) )
            if nato_100:
                rand = int(random.random()*500+100)
                self.buy( "nato_100", rand*(-1) )
                for i in range( 0, int(rand/20) ):
                    self.buy( "nato_100", 20 )
                    print( "{} -> 购买20个北约100".format( username ) )
            if gc_500:
                rand = int(random.random()*100+100)
                self.buy( "gc_500", rand*(-1) )
                for i in range( 0, int(rand/20) ):
                    self.buy( "gc_500", 20 )
                    print( "{} -> 购买20个500gc".format( username ) )
        else:
            print( "{}: 登录失败", username )

    def improve_all(self, accounts = "accounts.json", dx = True, steel_shield = True, nato_30 = True, nato_100 = False, gc_500 = False, ak_100 = True, grenade = True, dollars = True):
        import json
        import os
        import time
        import random
        f = open( os.getcwd() + "/" + accounts, 'r' , encoding="utf-8" )
        accounts = json.load( f )
        f.close()
        for username in accounts.keys():
            self.improve_one( username = username, password = accounts[username], dx = True, steel_shield = True, nato_30 = True, nato_100 = False, gc_500 = False, ak_100 = False, grenade = False, dollars = True )
