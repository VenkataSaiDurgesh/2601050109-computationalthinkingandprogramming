import asyncio
import aiohttp
import time

urls = [
    "https://example.com",
    "https://example.org",
    "https://example.net"
]

# Sequential
async def sequential():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        for url in urls:
            try:
                async with session.get(url) as r:
                    print("Sequential:", r.status)
            except:
                print("Failed")

    return time.time() - start


# Asynchronous with retry
async def get_page(session, url):
    for i in range(3):
        try:
            async with session.get(url) as r:
                print("Async:", r.status)
                return
        except:
            print("Retrying...")


async def asynchronous():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [get_page(session, url) for url in urls]
        await asyncio.gather(*tasks)

    return time.time() - start


async def main():

    seq = await sequential()
    async_time = await asynchronous()

    print("Sequential Time:", seq)
    print("Async Time:", async_time)


asyncio.run(main())
