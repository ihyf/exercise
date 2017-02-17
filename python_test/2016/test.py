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
            "order_id": "12221425",
            "total_amount": 1
        }
    }
}
list_dict = []

for i in range(3):
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
                "order_id": "12221425",
                "total_amount": 1
            }
        }
    }
    data_dict['params']['payment_order']['order_id'] = str(int(data_dict['params']['payment_order']['order_id'])+i)
    list_dict.append(data_dict)
print(list_dict)
