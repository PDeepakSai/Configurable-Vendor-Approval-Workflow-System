import json
import os

DATA_FILE = "data/requests.json"

def load_requests():
if not os.path.exists(DATA_FILE):
return []

```
with open(DATA_FILE, "r") as file:
    try:
        return json.load(file)
    except json.JSONDecodeError:
        return []
```

def save_requests(requests):
with open(DATA_FILE, "w") as file:
json.dump(requests, file, indent=4)

def save_request_state(request_id, status):
requests = load_requests()

```
request_entry = {
    "request_id": request_id,
    "status": status
}

requests.append(request_entry)

save_requests(requests)
```

def is_duplicate_request(request_id):
requests = load_requests()

```
for req in requests:
    if req["request_id"] == request_id:
        return True

return False
```
