import requests
from bs4 import BeautifulSoup

kv = {'key':'value','key2':'value2'}

r = requests.request('POST','http://www.baidu.com',data=kv)

body='ww'
r = requests.request('POST','http://www.baidu.com',data=body)



print(r)