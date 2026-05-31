from fastapi import FastAPI
from fastapi.responses import JSONResponse
import asyncio
import requests
import aiohttp
import time

app = FastAPI()

@app.get("/")
def get_element():
    start = time.perf_counter()
    result = []
    for _ in range(0, 10):
        req_res = requests.get("http://127.0.0.1:8000")
        result.append(req_res.json())
    end = time.perf_counter()
    ex_time = end - start
    return JSONResponse(
        status_code=200,
        content={
            "execution_time": f"{ex_time:.2f}",
            "data": result
        }
    )

@app.get("/async/")
async def async_get_element():
    start = time.perf_counter()
    result = []
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, "http://127.0.0.1:8000") for _ in range(10)]
        result = await asyncio.gather(*tasks)
    end = time.perf_counter()
    ex_time = end - start
    return JSONResponse(
        status_code=200,
        content={
            "execution_time": f"{ex_time:.2f}",
            "data": result
        }
    )

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()