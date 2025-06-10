# File type: Python (.py)
# Purpose: Perform asynchronous web scraping using aiohttp.

import asyncio
import aiohttp
from typing import List

# Async function to fetch the content of a given URL
async def fetch_page(session: aiohttp.ClientSession, url: str):
    print(f"🌐 Fetching: {url}")
    async with session.get(url) as response:
        html = await response.text()
        print(f"✅ Done: {url} ({len(html)} characters)")
        return html

# Function to scrape multiple pages concurrently
async def scrape_all(urls: List[str]):
    async with aiohttp.ClientSession() as session:
        # ⬇️ We create and await tasks all inside the session context
        tasks = [fetch_page(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results
