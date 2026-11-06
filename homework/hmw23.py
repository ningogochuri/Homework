




import requests
import aiohttp
import asyncio
import time


BASE_URL = 'https://jsonplaceholder.typicode.com/todos/{id}'


def fetch_data(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


start = time.time()

sync_results = []

for i in range(1, 11):
    url = BASE_URL.format(id=i)
    response = fetch_data(url)
    sync_results.append(response)

end = time.time()

sync_time = end - start

print("Synchronous time:", sync_time, "seconds")


async def fetch_async(session, url):
    timeout = aiohttp.ClientTimeout(total=10)

    async with session.get(url, timeout=timeout) as response:
        response.raise_for_status()
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:

        urls = [BASE_URL.format(id=i) for i in range(1, 11)]

        async_results = await asyncio.gather(
            *[fetch_async(session, url) for url in urls]
        )

        return async_results


start = time.time()

async_results = asyncio.run(main())

end = time.time()

async_time = end - start

print("Asynchronous time:", async_time, "seconds")

if async_time < sync_time:
    difference = sync_time - async_time
    print(f"ასინქრონულმა ვერსიამ {difference:.4f} წამით უფრო სწრაფად იმუშავა!")
else:
    difference = async_time - sync_time
    print(f"ასინქრონული ვერსია {difference:.4f} წამით უფრო ნელა მუშაობდა!")

print("Results are equal:", sync_results == async_results)
