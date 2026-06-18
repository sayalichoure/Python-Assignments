transactions = [
    {"txn_id": "T001", "type": "SIP",        "amount": 5000,  "status": "SUCCESS"},
    {"txn_id": "T002", "type": "REDEMPTION", "amount": 10000, "status": "FAILED"},
    {"txn_id": "T003", "type": "SIP",        "amount": 3000,  "status": "SUCCESS"},
    {"txn_id": "T004", "type": "SWITCH",     "amount": 7000,  "status": "PENDING"},
    {"txn_id": "T005", "type": "SIP",        "amount": 4000,  "status": "SUCCESS"},
]

def validate_trxns(transactions):
    total_trxns = len(transactions)
    total_no_of_success_trxns = len([trx for trx in transactions if trx["status"] == "SUCCESS"])
    total_amount_of_success_trxns = sum(trx["amount"] for trx in transactions if trx["status"] == "SUCCESS")
    return total_trxns, total_no_of_success_trxns, total_amount_of_success_trxns

print(validate_trxns(transactions)) 


transactions = [
    {"txn_id": "T001", "type": "SIP",        "amount": 5000,  "status": "SUCCESS"},
    {"txn_id": "T002", "type": "REDEMPTION", "amount": 10000, "status": "FAILED"},
    {"txn_id": "T003", "type": "SIP",        "amount": 3000,  "status": "SUCCESS"},
    {"txn_id": "T004", "type": "SWITCH",     "amount": 7000,  "status": "PENDING"},
    {"txn_id": "T005", "type": "SIP",        "amount": 4000,  "status": "SUCCESS"},
]

def validate_trxns(transactions):
    total_success = 0
    total_succ_amount = 0
    total_trx = len(transactions) 
    for trx in transactions:
        if  trx["status"] == "SUCCESS":
            total_success += 1
            total_succ_amount += trx["amount"]
    return total_trx, total_success, total_succ_amount
total_trx, total_success, total_succ_amount = validate_trxns(transactions)
print(f"Total transactions: {total_trx}")
print(f"Total successful transactions: {total_success}")
print(f"Total amount of successful transactions: {total_succ_amount}")


