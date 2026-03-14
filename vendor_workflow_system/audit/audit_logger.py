import json
import os
from datetime import datetime

LOG_FILE = "data/audit_logs.json"

def load_logs():
if not os.path.exists(LOG_FILE):
return {}

```
with open(LOG_FILE, "r") as file:
    try:
        return json.load(file)
    except json.JSONDecodeError:
        return {}
```

def save_logs(logs):
with open(LOG_FILE, "w") as file:
json.dump(logs, file, indent=4)

def log_event(request_id, message):
logs = load_logs()

```
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
entry = f"{timestamp} - {message}"

if request_id not in logs:
    logs[request_id] = []

logs[request_id].append(entry)

save_logs(logs)
```
