import aiohttp
import asyncio
import time
URL = "http://httpbin.org/get?a={}"
NUMBERS = 12
async def fetch_async(a):
    async with aiohttp.request('GET',URL.format(a)) as r:
        data = await r.json()
    return data['args']['a']

start = time.time()
event_loop = asyncio.get_event_loop()
tasks = [fetch_async(num) for num in range(NUMBERS)]
results = event_loop.run_until_complete(asyncio.gather(*tasks))


for num, result in zip(range(NUMBERS), results):
    print('fetch{} = {}'.format(num, result))
end = time.time()
print(end-start)
