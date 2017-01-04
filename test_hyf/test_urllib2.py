#coding:utf-8
import urllib2
import json
import simplejson

data = {
    "jsonrpc":"2.0",
    "method":"call ",
    "params":{
    "order_id": "123456",
    "version": "xxxx"
}
}
headers = {'Content-Type': 'application/json'}
request = urllib2.Request(url='http://10.128.230.203:8069/app_api/pos/stock_picking', headers=headers, data=json.dumps(data))
response = urllib2.urlopen(request)
res = response.read()
res = simplejson.loads(res)
print type(res)



