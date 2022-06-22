# Asynchronous HTTP requests in Python

Running HTTP asynchronously means, I can drastically increase the amount of requests processed in a certain time.

When running in a loop, a request is not waiting for the response before starting the next request. This non-blocking nature makes it possible to run multiple requests in a fraction of the time it takes compared to a synchronous request flow.

```python
import asyncio
import httpx

async def get_pokemon(client, url):
    resp = await client.get(url)
    pokemon = resp.json()
    return pokemon['name']

async def main():
    async with httpx.AsyncClient() as client:
        tasks = []
        for number in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_pokemon(client, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)
```

Use the following command to run the tasks:

```python
asyncio.run(main())
```

In a Jupyter notebook you can call the function directly, as it already has a running loop.

```python
await main()
```
