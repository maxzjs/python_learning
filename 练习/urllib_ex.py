# 2018.12.13
# maxzjs
# -*- coding:utf-8 -*-
'''
利用urllib读取json，然后将json解析为python对象

'''
from urllib import request
import json
import ssl

def fetch_data(url):
    with request.urlopen(url, context=ssl._create_unverified_context()) as f:
        urldata = f.read()
        print(type(urldata))
    return json.loads(urldata)

#测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')
