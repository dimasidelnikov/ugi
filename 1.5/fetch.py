import asyncio
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ["https://example.com", "https://www.python.org"]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for i, result in enumerate(results):
        print(f"Сайт {urls[i]}: {len(result)} символів отримано")

asyncio.run(main())
