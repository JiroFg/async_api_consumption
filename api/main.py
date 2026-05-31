from fastapi import FastAPI
from fastapi.responses import JSONResponse
import asyncio

app = FastAPI()

@app.get("/")
async def get_element():
    await asyncio.sleep(1)
    return JSONResponse(
        status_code=200,
        content={
            "name": "element"
        }
    )