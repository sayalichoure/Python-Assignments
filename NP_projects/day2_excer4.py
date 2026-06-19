folios = {
    "MF001": {"investor": "Sahili", "balance": 50000, "fund": "HDFC Top 100"},
    "MF002": {"investor": "Rahul",  "balance": 75000, "fund": "SBI Bluechip"},
    "MF003": {"investor": "Priya",  "balance": 30000, "fund": "ICICI Pru"},
}

def  get_folio_details(folios, folio_ids):
    if not folio_ids in folios:
        return  "FOlio not found"
    return folios[folio_ids]
print(get_folio_details(folios, "MF001"))  # Returns folio details
print(get_folio_details(folios, "MF999"))  # Returns "Folio not found"