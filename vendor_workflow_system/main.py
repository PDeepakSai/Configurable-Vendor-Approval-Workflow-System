import uuid
from models.vendor_request import VendorRequest
from engine.workflow_engine import process_vendor_application
from state.state_manager import save_request_state
from audit.audit_logger import log_event

def get_vendor_input():
print("\n--- Vendor Application ---")

```
vendor_name = input("Vendor Name: ")
tax_id = input("Tax ID: ")
company_age = int(input("Company Age (years): "))
country = input("Country: ")
category = input("Category: ")

request_id = str(uuid.uuid4())[:8]

vendor_request = VendorRequest(
    request_id=request_id,
    vendor_name=vendor_name,
    tax_id=tax_id,
    company_age=company_age,
    country=country,
    category=category
)

return vendor_request
```

def main():
print("\nVendor Approval Workflow System\n")

```
vendor_request = get_vendor_input()

log_event(vendor_request.request_id, "Request received")

decision = process_vendor_application(vendor_request)

save_request_state(vendor_request.request_id, decision)

log_event(vendor_request.request_id, f"Final decision: {decision}")

print("\n===== RESULT =====")
print(f"Request ID: {vendor_request.request_id}")
print(f"Decision: {decision}")
print("==================\n")
```

if **name** == "**main**":
main()
