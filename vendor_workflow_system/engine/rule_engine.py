import json

RULES_FILE = "config/rules.json"

def load_rules():
with open(RULES_FILE, "r") as file:
return json.load(file)

def evaluate_rule(field_value, operator, rule_value):
if operator == "<":
return field_value < rule_value
elif operator == ">":
return field_value > rule_value
elif operator == "==":
return field_value == rule_value
elif operator == "!=":
return field_value != rule_value
elif operator == "in":
return field_value in rule_value
elif operator == "not_in":
return field_value not in rule_value
else:
return False

def evaluate_rules(vendor_request):
rules = load_rules()

```
for rule in rules:
    field = rule["field"]
    operator = rule["operator"]
    value = rule["value"]
    action = rule["action"]

    field_value = getattr(vendor_request, field)

    if evaluate_rule(field_value, operator, value):
        return action, f"Rule triggered: {field} {operator} {value}"

return "approve", "All rules passed"
```
