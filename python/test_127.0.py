import requests
import json

URL = "http://118.178.191.211:8089/hollywant/pay"
headers = {'content-type': 'application/json'}
list_dict = []
for i in range(1000):
    data_dict = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "call",
        "params": {
            "method": "pay_qrcode",
            "hollywant_payment_id": "1",
            "hollywant_secret_key": "43a5f1eb68b572b09e758a737ba334d6",
            "payment_type": "alipay",
            "payment_order": {
                "order_id": "12221650",
                "total_amount": 1
            }
        }
    }
    data_dict['params']['payment_order']['order_id'] = str(int(data_dict['params']['payment_order']['order_id'])+i)
    list_dict.append(data_dict)
r = requests.session()
for data_dict in list_dict:
    respone = r.post(URL, data=json.dumps(data_dict), headers=headers).json()
    print respone
