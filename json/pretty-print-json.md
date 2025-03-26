# Pretty-print JSON blobs

To format/pretty-print a blob of JSON in your clipboard, following methods are available:

## vscode

Hit `CMD+N` to create a new document, paste the JSON blob in there, hit `CMD+K` then `M` and change the language to JSON.  
Hit `CMD+Shift+P` and type and select Format Document.

## terminal

`pbpaste | jq`  
or  
`pbpaste | json_pp`

## python

```python
import json
s = """<JSON blob>"""
print(json.dumps(json.loads(s), indent=2))
```

## duckduckgo

Search for json formatter.
