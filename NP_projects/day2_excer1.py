investor1 = {"name": "Sahili", "is_us_person": False, "fatca_submitted": True}
investor2 = {"name": "Rahul",  "is_us_person": True,  "fatca_submitted": False}
investor3 = {"name": "Priya",  "is_us_person": True,  "fatca_submitted": True}

def fatca_validate (investor):
    if not investor["is_us_person"]:
        return True
    if investor["fatca_submitted"]:
        return True
print(fatca_validate(investor1))  # True
print(fatca_validate(investor2))  # False     
print(fatca_validate(investor3))  # True