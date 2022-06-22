# Running async functions

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