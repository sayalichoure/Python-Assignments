investor = {"name": "Sahili", "pan": "ABCDE1234F"}

def get_investor_email(investor):
    try:
        return investor["email"]
    except KeyError:
        return "Email not found"
print(get_investor_email(investor))
#-----------------------------------------------------
investor = {"name": "Sahili", "pan": "ABCDE1234F"}
def get_investor_email_v2(investor):
    return investor.get("email", "Email not found")

print(get_investor_email_v2(investor))