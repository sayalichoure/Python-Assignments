investors = [
    {"name": "Rahul",  "folio_id": "MF001", "status": "ACTIVE"},
    {"name": "Priya",  "folio_id": "MF002", "status": "INACTIVE"},
    {"name": "Sahili", "folio_id": "MF003", "status": "ACTIVE"},
    {"name": "Amit",   "folio_id": "MF004", "status": "INACTIVE"},
    {"name": "Neha",   "folio_id": "MF005", "status": "ACTIVE"},
]

def active_folios(investors):
    active_folios = []
    for investor in investors:
        if investor["status"] == "ACTIVE":
            active_folios.append(investor["folio_id"])
    return active_folios
print(active_folios(investors))