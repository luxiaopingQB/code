import requests

url="http://localhost/cdantifraud/index.php/Home/Api/autifraud"

par={}
par['userid']="1"
par['qbtoken']="f2fe609abce5e4827a2c9c57a39e5461"
#par['cust_name']="李华"
#par['idcard']="430981199004050733"
#par['mobile']="13798437373"

par['cust_name']="黄长胜"
par['idcard']="130629199204030611"
par['mobile']="18801391543"

res=requests.post(url=url,data=par).content
print(res.decode('utf-8'))






