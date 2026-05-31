# Async API Consumption #

An example of how we can leverage Python's `asyncio` standard library and `aiohttp` to make multiple HTTP requests concurrently.

## Rationale ##

Making HTTP requests is an I/O-bound operation that can take a significant amount of time. When using a library such as `requests`, we do not take advantage of one of Python's most powerful features: `asyncio`.

`asyncio` allows us to execute I/O operations concurrently. While waiting for the response from one request, control can be returned to the event loop, allowing other tasks to be execute. As a result, our code becomes more efficient and overall execution time is reduced.

## How to execute ##
To execute this code follow the next steps.
1. Create your virtual enviroment (for example in my case with conda):
> `$ conda create -n "async_api_consumption_venv" python=3.14`

2. Activate your virtual enviroment (in my case with conda):
> `$ conda activate async_api_consumption_venv`

3. Install the dependencies:
> `$ pip install -r requirements.txt`

By default `FastAPI` runs on port `8000`. You can change it using `--port` parameter.

4. Run the api:
> `$ fastapi dev ./api/main.py`

5. Run the client api (we set the port because we are already using the default port):
> `$ fastapi dev ./client/main.py --port 3000`

