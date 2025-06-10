# 📁 File: api.py

from fastapi import FastAPI, Query
from typing import List
import asyncio
from app.scraper import scrape_all
from main import save_html, save_summary_json
from datetime import datetime
import os

app = FastAPI()

@app.get("/scrape")
async def scrape(urls: List[str] = Query(...)):
    """
    Endpoint to scrape multiple URLs concurrently.
    Example: /scrape?urls=https://example.com&urls=https://python.org
    """
    results = await scrape_all(urls)

    summary = []

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

    await save_summary_json(summary, "data/results.json")

    return {
        "message": "Scraping completed successfully!",
        "pages": summary
    }

# To run this:
# uvicorn api:app --reload
