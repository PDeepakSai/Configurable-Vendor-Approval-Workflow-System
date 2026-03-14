class VendorRequest:
def **init**(self, request_id, vendor_name, tax_id, company_age, country, category):
self.request_id = request_id
self.vendor_name = vendor_name
self.tax_id = tax_id
self.company_age = company_age
self.country = country
self.category = category

```
def to_dict(self):
    return {
        "request_id": self.request_id,
        "vendor_name": self.vendor_name,
        "tax_id": self.tax_id,
        "company_age": self.company_age,
        "country": self.country,
        "category": self.category
    }
```
