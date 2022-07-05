# Simultaneous HTTP requests in Python

Running HTTP in parallel means, I can drastically increase the amount of requests processed in a certain time.

When running in a loop, a request is not waiting for the response before starting the next request. This non-blocking nature makes it possible to run multiple requests in a fraction of the time it takes compared to a synchronous request flow.

```python
import concurrent.futures
import requests

def get_pokemon(client, url):
    response = client.get(url)
    pokemon = response.json()
    print(pokemon['name'])

urls = [f'https://pokeapi.co/api/v2/pokemon/{number}' for number in range(1,151)]

with concurrent.futures.ThreadPoolExecutor() as executor: 
   executor.map(get_pokemon, urls)
```
