# Experiment: Asynchronous Web Crawler Using `asyncio`, `aiohttp` and Retry

## 1. Algorithm / Procedure

1. Take a list of URLs.
2. In sequential crawling, visit URLs one by one.
3. In asynchronous crawling, visit URLs at the same time.
4. Use `aiohttp` to send web requests.
5. Use `asyncio` to run requests concurrently.
6. If a request fails, try again.
7. Compare the execution time.

---

## 2. Simple Python Program

```python
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
```

---

## 3. Data & Result

**Data:**

```text
URLs = 3
```

**Sample Result:**

```text
Sequential: 200
Sequential: 200
Sequential: 200

Async: 200
Async: 200
Async: 200

Sequential Time: 1.5 seconds
Async Time: 0.6 seconds
```

*The actual time may be different depending on the internet.*

---

## 4. Inference

* Sequential crawling visits one website at a time.
* Asynchronous crawling visits multiple websites together.
* `asyncio` manages the tasks.
* `aiohttp` sends web requests.
* Retry handles failed requests.

---

## 5. Analysis

| Method       | Speed                        | Working                   |
| ------------ | ---------------------------- | ------------------------- |
| Sequential   | Slower                       | One by one                |
| Asynchronous | Faster for many I/O requests | Multiple at the same time |

**Time Complexity:**

* Sequential: `O(n)`
* Asynchronous: approximately `O(1)` with respect to the number of URLs when requests overlap.

**Conclusion:** `asyncio` and `aiohttp` make web crawling faster by handling multiple network requests concurrently.
