def validate_kyc(investor):
    if investor["kyc_status"] == "VERIFIED":
        return True, "KYC Verified"
    if investor["kyc_status"] == "PENDING":
        return False, "KYC Pending"
    if investor["kyc_status"] == "REJECTED":
        return False, "KYC REJECTED"
    return False, "Unknown KYC Status"
investor1 = {"name": "Sahili", "pan": "ABCDE1234F", "kyc_status": "VERIFIED"}
investor2 = {"name": "Rahul",  "pan": "PQRST5678K", "kyc_status": "PENDING"}
investor3 = {"name": "Priya",  "pan": "LMNOP9012Z", "kyc_status": "REJECTED"}
investor4 = {"name": "Shrey",  "pan": "LGHUP9012Z", "kyc_status": "sdujbhs"}


print(validate_kyc(investor1))
print(validate_kyc(investor2))
print(validate_kyc(investor3))
print(validate_kyc(investor4))
