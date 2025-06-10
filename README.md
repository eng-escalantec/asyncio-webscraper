# 🕸️ AsyncIO Web Scraper API (FastAPI + aiohttp)

This project is an asynchronous web scraper built with Python 3.8+ using:

- `aiohttp` for non-blocking HTTP requests
- `aiofiles` for async file saving
- `FastAPI` to expose a public API
- `asyncio` to run all tasks concurrently

## 🚀 How to Run

```bash
pip install -r requirements.txt
uvicorn api:app --reload
