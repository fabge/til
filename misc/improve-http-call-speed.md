# improve http call speed

For any application that is *essentially* a piece of middleware linking together external calls (APIs, LLM calls, database queries), please ensure you have connection reuse/pooling on those requests

Probably one of the easiest performance improvements you can make

In Node.js, you can often do this by setting a custom HTTP agent with keepAlive: https://nodejs.org/api/http.html#class-httpagent

(from https://x.com/daniellockyer/status/1980956185571230140)
