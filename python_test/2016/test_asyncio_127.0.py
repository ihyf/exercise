import asyncio
import aiohttp
import time
import json

NUMBERS = range(1)
URL = "http://118.178.191.211:8089/hollywant/pay"
sema = asyncio.Semaphore(10)
async def fetch_async(datas):
    headers = {'content-type': 'application/json'}
    async with aiohttp.request('post', URL, data=json.dumps(datas), headers=headers) as r:
        response = await r.json()
    return response


async def print_result(datas):
    with (await sema):
        response = await fetch_async(datas)
        print(response)


def get_data_dict(i):
    data = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "call",
            "params": {
                "method": "pay_qrcode",
                "hollywant_payment_id": "1",
                "hollywant_secret_key": "43a5f1eb68b572b09e758a737ba334d6",
                "payment_type": "alipay",
                "payment_order": {
                    "order_id": "13861002",
                    "total_amount": 1
                }
            }
        }
    data['params']['payment_order']['order_id'] = str(int(data['params']['payment_order']['order_id'])+i)
    return data

start = time.time()
loop = asyncio.get_event_loop()
tasks = []
for i in range(20):
    tasks.append(print_result(get_data_dict(i)))
f = asyncio.wait(tasks)
loop.run_until_complete(f)
loop.close()
end = time.time()
print(end-start)

