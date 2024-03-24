# Parallel HTTP requests in Python

When running in a regular loop, a request is not waiting for the response before starting the next request.
Running HTTP in parallel means, I can drastically increase the amount of requests processed in a certain time.

## `concurrent.futures`

Using threads makes it possible to run multiple requests in a fraction of the time it takes compared to a synchronous request flow.

```python
import concurrent.futures
import requests

def get_pokemon(url):
    response = requests.get(url)
    pokemon = response.json()
    print(pokemon['name'])

urls = [f'https://pokeapi.co/api/v2/pokemon/{number}' for number in range(1,151)]

with concurrent.futures.ThreadPoolExecutor() as executor:
   executor.map(get_pokemon, urls)
```

## `fastcore.parallel`

The `fastcore` library has a `parallel` function that can be used to run multiple requests in parallel.

```python
from fastcore.parallel import parallel

def get_pokemon(url):
    response = requests.get(url)
    pokemon = response.json()
    print(pokemon['name'])

urls = [f'https://pokeapi.co/api/v2/pokemon/{number}' for number in range(1,151)]

parallel(get_pokemon, urls, n_workers=8)
```
