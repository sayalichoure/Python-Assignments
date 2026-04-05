#The code below has 3 bugs. Find and fix all of them. Bugs are related to types, conversion, 
# and the = vs == mistake.


# buggy code — find 3 mistakes
sip_amount = "5000"                 # came from a form field
gst_rate = 0.18
tax = int(sip_amount) * gst_rate            # bug 1

is_valid = int(sip_amount) > 1000         # bug 2

fund_name = "Axis Bluechip"
if fund_name == fund_name:        # bug 3
    print("Fund matched")
