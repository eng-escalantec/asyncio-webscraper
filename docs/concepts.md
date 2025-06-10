<!--
File type: Markdown (.md)
Purpose: Contains bilingual explanations of all key asyncio concepts.
-->

# Asyncio Concepts Guide

## ✅ What is asyncio?

`asyncio` is a library in Python that lets you write code that runs many tasks at the same time, without using threads or processes. It is perfect for tasks that spend time waiting, like downloading data from the internet or reading files.

---

## 🌀 What is the Event Loop?

The **event loop** is the brain behind `asyncio`. It:

- Keeps track of running tasks (coroutines)
- Switches between them when one is paused (e.g., waiting for a delay or a response)
- Makes sure the program keeps doing useful work instead of sitting idle

You don’t see the loop most of the time, but it’s always there, managing tasks in the background.

---

## 🧠 What is a Coroutine?

A **coroutine** is a special type of function defined using `async def`. It can be paused using `await`.

When you call a coroutine, it returns a **coroutine object**, not the final result. You must `await` it to actually run it.

### Example:
```python
async def my_task():
    print("Starting...")
    await asyncio.sleep(2)
    print("Finished!")
