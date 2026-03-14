from services.tax_service import verify_tax_id
from engine.rule_engine import evaluate_rules
from audit.audit_logger import log_event

def process_vendor_application(vendor_request):
request_id = vendor_request.request_id

```
# Step 1: Tax ID Verification
log_event(request_id, "Starting Tax ID verification")

tax_result = verify_tax_id(vendor_request.tax_id)

if tax_result == "invalid":
    log_event(request_id, "Tax ID invalid")
    return "REJECTED"

elif tax_result == "failure":
    log_event(request_id, "Tax service failure → manual review")
    return "MANUAL_REVIEW"

log_event(request_id, "Tax ID verified successfully")

# Step 2: Rule Evaluation
action, reason = evaluate_rules(vendor_request)

log_event(request_id, reason)

if action == "reject":
    return "REJECTED"

elif action == "manual_review":
    return "MANUAL_REVIEW"

# Step 3: Final Approval
log_event(request_id, "Vendor approved")
return "APPROVED"
```
