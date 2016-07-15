import requests

s = requests.Session()

url = "http://www.infestationmmo.com.cn/forgot_password.php"

headers = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"en-US,en;q=0.8",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Content-Length":76,
"Content-Type":"application/x-www-form-urlencoded",
# "Cookie":"PHPSESSID=fgda8cgg1g7ds4mmhe2ntr4947",
"Host":"www.infestationmmo.com.cn",
"Origin":"http://www.infestationmmo.com.cn",
# "Referer":"http://www.infestationmmo.com.cn/forgot_password.php?act=step&CustomerID=1175&code=1468&time=1468089461",
"Upgrade-Insecure-Requests":1,
"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
}

data = {
"act":"save",
"CustomerID":1175,
"password":"dHydra110",
"confirm_password":"dHydra110"
}
res = s.post( url = url, data = data )
print( res.text )
