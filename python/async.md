# async

`async` and `await` keywords are used to define asynchronous functions. The `async` keyword is used to define a function that returns a **coroutine** object. The `await` keyword is used to wait for the result of a coroutine object.

## Running async functions

Python

```python
import asyncio

async def main():
    print(1)

asyncio.run(main())
```

Jupyter

```python
async def main():
    print(1)

await main()
```

## Understanding `gather` vs `as_completed`

The `gather` method is used to run multiple tasks concurrently and return the results as a `list`. The `as_completed` returns a iterable is used to run multiple tasks concurrently and return the results as they complete. The following examples are adapted from [this great Blogpost](https://jxnl.github.io/instructor/blog/2023/11/13/learn-async/):

```python
import re

dataset = [
    "My name is John and I am 20 years old",
    "My name is Mary and I am 21 years old",
    "My name is Bob and I am 22 years old",
]

async def extract_person_name(text: str):
    return re.search(r"My name is (\w+)", text).group(1)
```

### `for loop`: Running tasks sequentially

```python
persons = []
for text in dataset:
    person = await extract_person_name(text)
    persons.append(person)
```

Even though there is an `await` keyword, we still have to wait for each task to finish before starting the next one. This is because we're using a `for` loop to iterate over the dataset. This method, which uses a `for` loop, will be the slowest among the four methods discussed.

### `asyncio.gather`: Running tasks concurrently

```python
async def gather():
    tasks_get_persons = [extract_person_name(text) for text in dataset]
    persons = await asyncio.gather(*tasks_get_persons)
```

Using `asyncio.gather` allows us to return all the results at once. It is an effective way to speed up our code, but it's not the only way. Particularly, if we have a large dataset, we might not want to wait for everything to finish before starting to process the results. This is where `asyncio.as_completed` comes into play.

### `asyncio.as_completed`: Handling tasks as they complete

```python
async def as_completed():
    persons = []
    tasks_get_persons = [extract_person_name(text) for text in dataset]
    for person in asyncio.as_completed(tasks_get_persons):
        persons.append(await person)
```

This method is a great way to handle large datasets. We can start processing the results as they come in, especially if we are streaming data back to a client.

It is important to note that the order of the results will not be the same as the order of the dataset. This is because the tasks are completed in the order they finish, not the order they were started. If you need to preserve the order of the results, you can use `asyncio.gather` instead.

### `Rate-Limited Gather`: Using semaphores to limit concurrency

The above methods aim to complete as many tasks as possible as quickly as possible. This can be problematic if we want to be considerate to the server we're making requests to. This is where rate limiting comes into play.

```python
async def rate_limited_extract_person(text: str, sem: Semaphore) -> Person:
    async with sem:
        return await extract_person(text)

sem = asyncio.Semaphore(2)

async def rate_limited_gather(sem: Semaphore):
    tasks_get_persons = [rate_limited_extract_person(text, sem) for text in dataset]
    persons = await asyncio.gather(*tasks_get_persons)
```

### `Rate-Limited As Completed`: Using semaphores to limit concurrency

```python
async def rate_limited_extract_person(text: str, sem: Semaphore) -> Person:
    async with sem:
        return await extract_person(text)

async def rate_limited_as_completed(sem: Semaphore):
    persons = []
    tasks_get_persons = [rate_limited_extract_person(text, sem) for text in dataset]
    for person in asyncio.as_completed(tasks_get_persons):
        persons.append(await person)
```

### Other options

It is important to also note that here we are using a `semaphore` to limit the number of concurrent requests. However, there are other ways to limit concurrency especially since we have rate limit information from the `openai` request. You can imagine using a library like `ratelimit` to limit the number of requests per second. OR catching rate limit exceptions and using `tenacity` to retry the request after a certain amount of time.

- [tenacity](https://github.com/jd/tenacity)
- [aiolimiter](https://github.com/mjpieters/aiolimiter)

### Practical implications

The choice of approach depends on the task's nature and the desired balance between speed and resource utilization.

Here are some guidelines to consider:

- Use `asyncio.gather` for handling multiple independent tasks quickly.
- Apply `asyncio.as_completed` for large datasets to process tasks as they complete.
- Implement rate-limiting to avoid overwhelming servers or API endpoints.
