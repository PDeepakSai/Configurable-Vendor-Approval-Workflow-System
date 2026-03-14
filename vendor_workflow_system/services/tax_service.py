import random
import time

def verify_tax_id(tax_id, max_retries=3):
"""
Simulates an external tax verification service.
Possible outcomes:
- valid
- invalid
- failure (service unavailable)
"""

```
for attempt in range(1, max_retries + 1):
    result = simulate_external_service(tax_id)

    if result == "valid":
        return "valid"

    if result == "invalid":
        return "invalid"

    if result == "failure":
        print(f"Tax service failure (attempt {attempt})... retrying")
        time.sleep(1)

return "failure"
```

def simulate_external_service(tax_id):
"""
Randomly simulate external API behaviour.
"""

```
outcomes = ["valid", "invalid", "failure"]
return random.choice(outcomes)
```
