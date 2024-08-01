import json

data = '{"name": "Alice", "age": 30}'
parsed = json.loads(data)
print(parsed["name"])  
