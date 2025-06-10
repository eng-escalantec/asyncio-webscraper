# File type: Python (.py)
import asyncio
from app.scraper import scrape_all
import aiofiles
import os
import json
from datetime import datetime
from typing import List


# Save all scraping results to a JSON file
async def save_summary_json(results: List[dict], filepath: str):
    async with aiofiles.open(filepath, mode='w', encoding='utf-8') as f:
        json_string = json.dumps(results, indent=4)
        await f.write(json_string)
    print(f"\n🗂️  Summary saved to {filepath}")

# Async function to save HTML content to a file
async def save_html(content: str, filename: str):
    path = os.path.join("results", filename)
    async with aiofiles.open(path, mode='w', encoding='utf-8') as f:
        await f.write(content)
    print(f"💾 Saved: {filename}")

async def main():
    urls = [
        "https://httpbin.org/html",
        "https://example.com",
        "https://www.python.org"
    ]

    print("Starting async scrape...")
    results = await scrape_all(urls)

    summary = []

    print("\n📄 Saving and previewing results...")
    for i, html in enumerate(results):
        filename = f"page_{i+1}.html"
        await save_html(html, filename)

        url = urls[i]
        chars = len(html)
        timestamp = datetime.utcnow().isoformat()

        summary.append({
            "url": url,
            "file": filename,
            "chars": chars,
            "timestamp": timestamp
        })

        print(f"\n--- Page {i+1} Preview ---")
        print(html[:200])

    await save_summary_json(summary, "data/results.json")


if __name__ == "__main__":
    import asyncio
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())